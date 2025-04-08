from langchain_ollama import OllamaLLM

def get_ollama_llm_response(query, context, model="mistral"):
    llm = OllamaLLM(model=model)
    prompt = (
        "Answer the question using ONLY the context below. "
        "If the answer is not there, respond with 'I don't know.'\n\n"
        f"Context:\n{context}\n\nQuestion: {query}"
    )
    return llm.invoke(prompt)