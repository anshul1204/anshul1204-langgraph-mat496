# Langgraph Anshul Virmani 2210110172 MAT496

**Module 1**


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





**Module 2**


Video 1: State Schema

What I Learned: I reviewed various ways to define a LangGraph state schema, including TypedDict, Literal, and Dataclasses. I understood how to declare keys, constrain values and how nodes expect and communicate state using these schemas. Learned the difference between static type hints and actual runtime validation.


Changes in Code: Introduced specific typed state schemas using TypedDict with literals for constrained values. Tried dataclasses for more concise data structures, adjusting how node functions access data accordingly (attribute access for dataclasses vs dictionary keys). Created sample graphs testing each state type.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-2/state-schema.ipynb)


Video 2: State Reducers

What I Learned: This part helped me in understanding state reducers which define how updates to state keys/channels happen. It covered different approaches to define the state schema with Python TypedDict, Pydantic, or Dataclasses and how reducers specify overwriting or custom update logic for each key.


Changes in Code: I experimented with different reducer types and writing reducer functions that handle adding or merging state values. Tweaked schemas to use literals and custom state classes. Experimented with preserving parts of the state while updating others and coordinating reducer flows with the graph execution.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-2/state-reducers.ipynb)

Video 3: Multiple Schemas

What I Learned: The video covered customizing LangGraph to use multiple state schemas simultaneously. This is useful to pass “private state” used internally between nodes without exposing it on the graph's inputs or outputs. Also learned how to define distinct input/output schemas for a graph, improving control and security.


Changes in Code: Implemented examples showing the separation of OverallState vs PrivateState. Modified nodes to accept one schema and produce outputs conforming to another. Added input/output schema declarations to graph builders and compiled graphs testing private state passing and partial output folding.


[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-2/multiple-schemas.ipynb)

Video 4: Trim and Filter Messages

What I Learned: This video focused on advanced techniques for trimming and filtering messages in the graph state to balance memory and token usage. Various trimming strategies like keeping last N messages or filtering by criteria were tested. This is foundational for building chatbots that sustain longer sessions without hitting token limits.


Changes in Code: I wrote custom trimming functions that selectively trim conversation while preserving necessary context. Tested trimming with allow_partial mode and different max token limits. Integrated trimming logic in chatbot graphs and observed model outputs with varying trimming policies.

![alt text](image-1.png)

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-2/trim-filter-messages.ipynb)

Video 5: Chatbot Summarizing Messages and Memory

What I Learned: I learned how to build a chatbot that uses LLMs to produce a running summary of the conversation, instead of just trimming or filtering messages. This lets the chatbot retain a compressed, context-rich summary, which supports long conversations without increasing token usage or latency. I worked with a custom state extended from MessagesState that included a summary field and developed logic to generate and update the summary dynamically within the conversation flow.


Changes in Code: I modified the summarization node to include summary text in the system message fed to the model. I implemented a summarization function that extends or creates the summary based on new messages and removes older messages to limit state size. I added a conditional edge to trigger summarization only after the conversation exceeds a threshold number of messages (modified to summarizing after 5 messages instead of default). Added tracing setup for LangSmith and tested the thread-based memory persistence.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-2/chatbot-summarization.ipynb)

Video 6: Chatbot Summarizing Messages and External Memory

What I Learned: This section introduced external persistent memory by incorporating external database-backed checkpointers (like SQLite). This enables chatbots to save and resume conversations across restarts and long durations, overcoming the transient state limitation.

Changes in Code: Set up SQLite checkpointer and connected it to the chatbot graph for state persistence. Rebuilt the chatbot to use this persistent memory with thread IDs. Demonstrated re-loading state after kernel restart, validating memory persistence on disk. Prepared configuration for other DBs like Postgres for production use.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-2/chatbot-external-memory.ipynb)



**Module 3**


Video 1: Streaming

What I Learned: In this video, I learned how streaming works inside the graph so the model can send partial outputs live. I also learned how streaming can be interrupted so I can change the state mid-stream and then continue the run. It showed how this helps in creating summaries or reacting while the model is still generating.


Changes in Code: I updated my graph so LLM nodes can stream tokens. I enabled streaming modes for state updates and token updates. I added logic to interrupt streaming when needed, based on events or human input. I also integrated checkpoints into the streaming flow and used RunnableConfig to control how the streaming behaves.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-3/streaming-interruption.ipynb)


Video 2: Breakpoints

What I Learned: I learned the basics of breakpoints where the graph pauses at fixed points so someone can manually approve the next step. It showed how the flow stops, waits for input, and then continues. I also got to see how breakpoints fit into LangChain and LangGraph when we want more human control.


Changes in Code: I added simple breakpoint nodes to my graph and connected them using control-flow edges. I inserted a human approval node to handle pausing and resuming. I used the memory saver and state graph to manage breakpoint states and added streaming so I could see when the graph pauses and starts again. I also imported the tools needed for these advanced nodes.

![alt text](image-2.png)

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-3/breakpoints.ipynb)

Video 3: Editing State and Human Feedback

What I Learned: I understood how a human feedback step can be added inside the graph so we can jump in and update things while it’s running. I learned how the graph uses nodes like the assistant, tools, and this human feedback point, and how conditional edges help switch the flow depending on tool calls. It also taught me about saving checkpoints and handling interruptions so the state can be changed mid-execution.


Changes in Code: I added a human feedback node to my graph and changed the edges so the flow goes from START to human feedback and then to the assistant. I used addConditionalEdges to manage the flow after the assistant’s output. I also updated the state thread using human feedback messages, added the required imports, and enabled the graph to show its structure. My code now supports streaming updates and can react to user input during execution.

![alt text](image-3.png)

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-3/edit-state-human-feedback.ipynb)


Video 4: Dynamic Breakpoints

What I Learned: In this video, I learned how dynamic breakpoints work in a graph. They can interrupt execution automatically whenever the input matches certain conditions like message length or specific patterns. I also understood how the graph can pause, let me update the state, and then continue running. It was helpful to see how this is different from normal pausing because it reacts based on rules.


Changes in Code: I created several breakpoint nodes in my code with custom logic using regex checks and length rules. I used interrupt exceptions to stop the execution and added code to resume it after the state is updated. I also added memory checkpoints and made the streaming updates aware of breakpoints. The graph edges and nodes were adjusted so multiple breakpoint conditions work correctly.

![alt text](image-4.png)

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-3/dynamic-breakpoints.ipynb)

Video 5: Time Travel

What I learned: I learned about the “time travel” features in the state graph. It showed me how I can replay old runs, look at older states, and even fork new execution paths from past checkpoints. I also learned how to replace earlier messages by updating state using their message IDs instead of always adding new ones.


Changes in Code: I expanded my graph code to include replaying and forking features. I used functions like getState, getStateHistory, and the replay methods. I also added logic to fork a new thread from a past checkpoint and overwrite states using message IDs. I improved the streaming so it shows state changes for every rewind or fork, and set up proper checkpoint management for branching.

[View Notebook](https://github.com/anshul1204/anshul1204-langgraph-mat496/blob/main/module-3/time-travel.ipynb)


**Module 4**


Video 1: Parallelization

What I Learned: I learned how to run parts of a graph in parallel so different nodes do work at the same time and the results get combined later. I got famalier with fan-out (send many tasks) and fan-in (reduce results) patterns that makes big tasks faster. I saw how state updates from multiple nodes can be collected and then reduced in a controlled order. It also explained how to use a custom reducer to merge or sort the parallel outputs.


Changes in Code: I added a fan-out section using Send so the same task could be sent to multiple nodes in parallel, and then added a reducer that collects all their outputs and combines them using a sorting_reducer. I also created the actual parallel nodes and connected them properly to the fan-out point so everything runs together. To make sure the updates come back in the right order, I added logic for how the reducer receives and processes the list of results. I even enabled the streaming view so I could watch each node finish and see the reducer put everything together in real time.


Video 2: Sub-Graphs

What I Learned: I learned how sub-graphs let us put smaller workflows inside a bigger workflow, kind of like “mini-graphs” inside the main one. It helped me understand how complex tasks can be broken into modules that are easier to manage. I also learned how input passes into the sub-graph and how the output comes back to the parent graph. I also got to know how sub-graphs make the code cleaner when the workflow has repeated or grouped logic.

Changes in Code: I created a separate sub-graph using its own builder and state logic, and added a final output node to complete it. Then I compiled that sub-graph and plugged it into the main graph as a regular node so the parent could call it. I connected the edges so the main graph flows into this sub-graph node and then continues with whatever state the sub-graph returns. I also added a small helper function to prepare or filter the input before sending it into the sub-graph, just to make sure it only receives the fields it actually needs.


Video 3: Map Reduce

What I Learned: I understood how map-reduce lets us break a big task into smaller chunks and then combine the results at the end. I learned how each part of the work can run in parallel, which makes everything faster. I also understood how LangGraph uses the Send function to automatically fan out tasks without manually writing loops. It taught me how state is passed between nodes and how the reduce step collects everything together.


Changes in Code: I added a new State class to keep track of the subjects and jokes, along with a BestJoke model for the final output. Then I wrote the continue_to_jokes function, which uses Send to fan out each subject to the "generate_joke" node automatically. I also added two main nodes: "generate_subjects" to create joke topics using the LLM, and "generate_joke" to actually make the jokes. After that, I connected the whole flow so it moves from start → subject generation → parallel joke generation → reduction. Finally, I added a reducer step that collects all the jokes and uses the find_best_joke logic to pick the best one.