from config import settings


def choose_model() -> str:
    provider = settings.model_provider.lower()
    if provider == "gemini":
        return "gemini-1.5-flash"
    if provider == "openrouter":
        return "openrouter/auto"
    return "gpt-4o-mini"


if __name__ == "__main__":
    print("LangChain boilerplate ready")
    print("Provider:", settings.model_provider)
    print("Model:", choose_model())
