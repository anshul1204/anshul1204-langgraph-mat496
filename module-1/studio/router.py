from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from typing import Literal

# Tool
def translate(
    text_to_translate: str, 
    target_language: Literal["French", "Spanish", "German"]
) -> str:
    """Translates the input text to the specified target language.

    Args:
        text_to_translate: The text that needs to be translated.
        target_language: The language to translate the text into.
    """
    
    if target_language == "French":
        return f"'{text_to_translate}' in French is 'Bonjour'."
    elif target_language == "Spanish":
        return f"'{text_to_translate}' in Spanish is 'Hola'."
    elif target_language == "German":
        return f"'{text_to_translate}' in German is 'Hallo'."
    else:
        return "Sorry, I don't know that language."

# LLM with bound tool
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools([translate])

# Node
def tool_calling_llm(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", ToolNode([translate]))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges(
    "tool_calling_llm",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", END)

# Compile graph
graph = builder.compile()