from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.rag import ask_question

class GraphState(TypedDict):
    question: str
    answer: dict

def rag_node(state: GraphState):
    result = ask_question(state["question"])
    return {"answer": result}

workflow = StateGraph(GraphState)
workflow.add_node("rag", rag_node)
workflow.set_entry_point("rag")
workflow.add_edge("rag", END)

rag_graph = workflow.compile()
