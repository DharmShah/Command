from state import GraphState


def run_graph(question: str) -> GraphState:
    return {
        "question": question,
        "answer": "Demo response from LangGraph boilerplate"
    }


if __name__ == "__main__":
    result = run_graph("What is LangGraph?")
    print(result)
