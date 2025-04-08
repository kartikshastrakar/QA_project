from src.llm.ollama_integration import get_ollama_llm_response

def test_get_ollama_llm_response(mocker):
    mock_llm = mocker.patch("src.llm.ollama_integration.Ollama")
    mock_llm.return_value.invoke.return_value = "This is a mock response."

    query = "What is the test?"
    context = "This is a test context."
    response = get_ollama_llm_response(query, context)

    assert response == "This is a mock response."