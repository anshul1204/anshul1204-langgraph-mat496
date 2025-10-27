from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode

def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b


def convert_to_binary(number: int, bits: int = 8) -> str:
    """Converts a decimal integer to its two's complement binary representation.

    Args:
        number: The decimal integer to convert.
        bits: The number of bits for the binary representation.
    """
    if number >= 0:
        # For positive numbers, use standard binary conversion
        return bin(number)[2:].zfill(bits)
    else:
        # For negative numbers, calculate two's complement
        return bin((1 << bits) + number)[2:]

def calculate_twos_complement(binary_string: str) -> str:
    """Calculates the two's complement of a binary string.

    Args:
        binary_string: The binary string (e.g., '00000101').
    """
    bits = len(binary_string)
    # Invert the bits
    inverted = ''.join(['1' if b == '0' else '0' for b in binary_string])
    # Add 1
    inverted_int = int(inverted, 2)
    twos_comp_int = inverted_int + 1
    # Convert back to binary and handle overflow
    return bin(twos_comp_int)[2:].zfill(bits)[-bits:]

def add_twos_complement_binaries(bin1: str, bin2: str) -> str:
    """Adds two two's complement binary strings.

    Args:
        bin1: The first binary string.
        bin2: The second binary string.
    """
    bits = len(bin1)
    sum_val = int(bin1, 2) + int(bin2, 2)
    # Handle overflow by taking the last 'bits' number of bits
    result = sum_val & ((1 << bits) - 1)
    return bin(result)[2:].zfill(bits)

def convert_from_twos_complement(binary_string: str) -> int:
    """Converts a two's complement binary string back to a decimal integer.

    Args:
        binary_string: The two's complement binary string.
    """
    bits = len(binary_string)
    val = int(binary_string, 2)
    # If the most significant bit is 1, it's a negative number
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val


tools = [
    add, 
    multiply, 
    divide, 
    convert_to_binary, 
    calculate_twos_complement, 
    add_twos_complement_binaries,
    convert_from_twos_complement
]

# Define LLM with bound tools
llm = ChatOpenAI(model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with writing performing arithmetic on a set of inputs.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")

# Compile graph
graph = builder.compile(interrupt_before=["tools"])
