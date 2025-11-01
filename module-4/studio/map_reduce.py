import operator
from typing import Annotated
from typing_extensions import TypedDict

from pydantic import BaseModel

from langchain_openai import ChatOpenAI 

from langgraph.constants import Send
from langgraph.graph import END, StateGraph, START

# Prompts we will use
subjects_prompt = """Generate a list of 3 sub-topics that are all related to this overall topic: {topic}."""
fact_prompt = """Share an interesting and scientifically accurate cosmic fact about {subject}.
Make it engaging, clear, and educational."""
best_fact_prompt = best_fact_prompt = """Below are several cosmic facts about {topic}.
Select the most interesting, accurate, and awe-inspiring one!
Return the ID of the best fact, starting 0 as the ID for the first fact.
Facts:
{facts}"""

# LLM
model = ChatOpenAI(model="gpt-4o", temperature=0) 

# Define the state
class Subjects(BaseModel):
    subjects: list[str]

class BestFact(BaseModel):
    id: int
    
class OverallState(TypedDict):
    topic: str
    subjects: list
    facts: Annotated[list, operator.add]
    best_selected_fact: str

def generate_topics(state: OverallState):
    prompt = subjects_prompt.format(topic=state["topic"])
    response = model.with_structured_output(Subjects).invoke(prompt)
    return {"subjects": response.subjects}

class FactState(TypedDict):
    subject: str

class Fact(BaseModel):
    fact: str

def generate_fact(state: FactState):
    prompt = fact_prompt.format(subject=state["subject"])
    response = model.with_structured_output(Fact).invoke(prompt)
    return {"facts": [response.fact]}

def best_fact(state: OverallState):
    facts = "\n\n".join(state["facts"])
    prompt = best_fact_prompt.format(topic=state["topic"], facts=facts)
    response = model.with_structured_output(BestFact).invoke(prompt)
    return {"best_selected_fact": state["facts"][response.id]}

def continue_to_facts(state: OverallState):
    return [Send("generate_fact", {"subject": s}) for s in state["subjects"]]

# Construct the graph: here we put everything together to construct our graph
graph_builder = StateGraph(OverallState)
graph_builder.add_node("generate_topics", generate_topics)
graph_builder.add_node("generate_fact", generate_fact)
graph_builder.add_node("best_fact", best_fact)
graph_builder.add_edge(START, "generate_topics")
graph_builder.add_conditional_edges("generate_topics", continue_to_facts, ["generate_fact"])
graph_builder.add_edge("generate_fact", "best_fact")
graph_builder.add_edge("best_fact", END)

# Compile the graph
graph = graph_builder.compile()
