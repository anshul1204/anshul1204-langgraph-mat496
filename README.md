# Langgraph Anshul Virmani 2210110172 MAT496

**Module 1**

Video 1: Motivation

I learned that LangGraph helps overcome the usual limitations of language models, especially their lack of access to tools and external context like documentation. The video also talked about how basic LLMs fall short in certain tasks and introduced the idea of control flow. I also got a clearer understanding of chain architecture and agent architecture.


Video 2: Simple Graph

What I Learned: I learned how to create a basic graph structure using LangGraph, starting with defining a custom state using TypedDict, writing simple Python functions as nodes, and connecting these nodes with both normal and conditional edges. I also saw how a conditional edge can route execution differently based on logic, making the graph dynamic and interactive.


Changes in Code: I expanded the base graph by adding extra nodes and changing the conditional logic to randomly select between more options (e.g. choosing between multiple drink nodes). The graph’s state was customized to carry a user-specific string, and the output was observed at each node during execution to verify the logic. Being comfortable with state schemas and node function signatures also helped in tweaking the sequence and logic of the graph flow.​



