from typing_extensions import TypedDict
from langgraph.errors import NodeInterrupt
from langgraph.graph import START, END, StateGraph
import re

class State(TypedDict):
    input: str

def step_1(state: State) -> State:
    print("---Step 1---")
    return state

def step_2(state: State) -> State:
    # Let's optionally raise a NodeInterrupt if the length of the input is longer than 5 characters
    if len(state['input']) > 5:
        # Keep original logic for step 2 interruption
        print(f"---Step 2 INTERRUPT (length > 5): Input '{state['input']}'---")
        raise NodeInterrupt(f"Received input that is longer than 5 characters: {state['input']}")

    print("---Step 2---")
    return state

def step_3(state: State) -> State:
# Check if the input contains any digit
    if re.search(r'\d', state['input']):
        print(f"---Step 3 INTERRUPT (contains number): Input '{state['input']}'---")
        raise NodeInterrupt(f"Input contains a number: {state['input']}")

    print("---Step 3---")
    return state


def step_4(state: State) -> State:
    print("---Step 4---")
    return state

builder = StateGraph(State)
builder.add_node("step_1", step_1)
builder.add_node("step_2", step_2)
builder.add_node("step_3", step_3)
builder.add_node("step_4", step_4) 

builder.add_edge(START, "step_1")
builder.add_edge("step_1", "step_2")
builder.add_edge("step_2", "step_3")
builder.add_edge("step_3", "step_4") 
builder.add_edge("step_4", END)  

graph = builder.compile()
