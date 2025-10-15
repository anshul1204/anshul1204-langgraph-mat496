# Langgraph Anshul Virmani 2210110172 MAT496

**Module 1**

Video 1: Motivation

I learned that LangGraph helps overcome the usual limitations of language models, especially their lack of access to tools and external context like documentation. The video also talked about how basic LLMs fall short in certain tasks and introduced the idea of control flow. I also got a clearer understanding of chain architecture and agent architecture.


Video 2: Simple Graph

What I Learned: I learned how to create a basic graph structure using LangGraph, starting with defining a custom state using TypedDict, writing simple Python functions as nodes, and connecting these nodes with both normal and conditional edges. I also saw how a conditional edge can route execution differently based on logic, making the graph dynamic and interactive.


Changes in Code: I expanded the base graph by adding extra nodes and changing the conditional logic to randomly select between more options (e.g. choosing between multiple drink nodes). The graph’s state was customized to carry a user-specific string, and the output was observed at each node during execution to verify the logic. Being comfortable with state schemas and node function signatures also helped in tweaking the sequence and logic of the graph flow.​


Video 3: Langsmith Studio 

What I Learned: I learned how to download LangSmith Studio and use it to visualize and test graphs, and also how it helps track each step in the workflow. I also got to see how graphs can be viewed as proper flowcharts inside LangSmith Studio, instead of the basic visualization we used to see earlier in Jupyter Notebook.


Changes in Code: I updated the simple.py file by adding a new node and adjusted the probabilities by changing it from 50% to 33% because of the extra node. The new node represented a ‘bored’ state. I also tested the agent graph by asking it to multiply 10 and 2, and it successfully performed the multiplication.


