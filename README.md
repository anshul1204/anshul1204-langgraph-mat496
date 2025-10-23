# Langgraph Anshul Virmani 2210110172 MAT496

<u>**Module 1**</u>


Video 1: Motivation

I learned that LangGraph helps overcome the usual limitations of language models, especially their lack of access to tools and external context like documentation. The video also talked about how basic LLMs fall short in certain tasks and introduced the idea of control flow. I also got a clearer understanding of chain architecture and agent architecture.


Video 2: Simple Graph

What I Learned: I learned how to create a basic graph structure using LangGraph, starting with defining a custom state using TypedDict, writing simple Python functions as nodes, and connecting these nodes with both normal and conditional edges. I also saw how a conditional edge can route execution differently based on logic, making the graph dynamic and interactive.


Changes in Code: I expanded the base graph by adding extra nodes and changing the conditional logic to randomly select between more options (e.g. choosing between multiple drink nodes). The graph’s state was customized to carry a user-specific string, and the output was observed at each node during execution to verify the logic. Being comfortable with state schemas and node function signatures also helped in tweaking the sequence and logic of the graph flow.​

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-1/simple-graph.ipynb)


Video 3: Langsmith Studio 

What I Learned: I learned how to download LangSmith Studio and use it to visualize and test graphs, and also how it helps track each step in the workflow. I also got to see how graphs can be viewed as proper flowcharts inside LangSmith Studio, instead of the basic visualization we used to see earlier in Jupyter Notebook.


Changes in Code: I updated the simple.py file by adding a new node and adjusted the probabilities by changing it from 50% to 33% because of the extra node. The new node represented a ‘bored’ state. I also tested the agent graph by asking it to multiply 10 and 2, and it successfully performed the multiplication.

![alt text](Images/image.png)

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-1/studio/simple.py)


Video 4: Chain

What I Learned: In this part, i learned how to extend graphs into more complex chains. I focused on using chat messages as state through LangGraph’s pre-built MessagesState, incorporating sequence of messages for context between nodes. I learned how to append messages across steps using reducer functions and how to use LLM chat models and tool bindings for real conversations, not just static data.


Changes in Code: I customized the chain to support real conversational flows by adding sample message lists, switching between human and AI message types, and binding custom translation and arithmetic tools to the model. The tweaks included testing tool invocation inside the chain for example, triggering translations or math based on specific user messages and verifying the reducer logic so that all chat history persisted as the chain progressed.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-1/chain.ipynb)


Video 5: Router

What I Learned: I explored the concept of routers within LangGraph, where the model routes between returning a direct response or calling a tool, based on the user’s input. This section reinforced how conditional edges and tool-calling logic drive simple “agent” behavior within a graph.


Changes in Code: I updated the router graph to demonstrate tool vs natural language path selection explicitly. Functions like language translation or arithmetic could be routed based on detected intent in the message, with clear logging at decision points. I cleaned up the tool call schema, ensured logging of routes, and tested different user prompts to confirm the control flow was handling all edges correctly.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-1/router.ipynb)

Video 6: Agent 

What I Learned: Here I built a general agent architecture based on the ReAct design, where the LLM model can loop between reasoning, acting (via tool calls), and observing results until deciding to give a final answer. This modular approach supports complex sequences and multiple tool decisions before producing a direct output.


Changes in Code: I wrote arithmetic tools (add, multiply, divide etc.) and extended the agent to handle binary and two’s complement operations. I updated the tool list and LLM bindings, and tested flows where the agent had to chain tool calls (e.g. do math, convert to binary, handle two’s complement logic, and then convert back to decimal). The graph flow was enhanced with debugging statements and more robust node-to-node connections to support advanced tool chaining.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-1/agent.ipynb)

Video 7: Agent with Memory

What I Learned: I learned how to extend agent architectures in LangGraph by introducing memory. Now, agents can remember previous steps in a conversation and use checkpoints to persist state, which lets the assistant recall past user messages and calculations even after interruptions.​


Changes in Code: I set up in-memory checkpointing using the built-in MemorySaver, so the graph can store and retrieve state with a thread id. I expanded my toolset to include binary conversion and two's complement logic, and tested the agent with multi-step arithmetic and conversions, verifying memory by resuming conversations and operations after state updates and interruptions.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-1/agent-memory.ipynb)





<u>**Module 2**</u>


Video 1: State Schema

What I Learned: I reviewed various ways to define a LangGraph state schema, including TypedDict, Literal, and Dataclasses. I understood how to declare keys, constrain values and how nodes expect and communicate state using these schemas. Learned the difference between static type hints and actual runtime validation.


Changes in Code: Introduced specific typed state schemas using TypedDict with literals for constrained values. Tried dataclasses for more concise data structures, adjusting how node functions access data accordingly (attribute access for dataclasses vs dictionary keys). Created sample graphs testing each state type.


Video 2: State Reducers

What I Learned: This part helped me in understanding state reducers which define how updates to state keys/channels happen. It covered different approaches to define the state schema with Python TypedDict, Pydantic, or Dataclasses and how reducers specify overwriting or custom update logic for each key.


Changes in Code: I experimented with different reducer types and writing reducer functions that handle adding or merging state values. Tweaked schemas to use literals and custom state classes. Experimented with preserving parts of the state while updating others and coordinating reducer flows with the graph execution.


Video 3: Multiple Schemas

What I Learned: The video covered customizing LangGraph to use multiple state schemas simultaneously. This is useful to pass “private state” used internally between nodes without exposing it on the graph's inputs or outputs. Also learned how to define distinct input/output schemas for a graph, improving control and security.


Changes in Code: Implemented examples showing the separation of OverallState vs PrivateState. Modified nodes to accept one schema and produce outputs conforming to another. Added input/output schema declarations to graph builders and compiled graphs testing private state passing and partial output folding.
