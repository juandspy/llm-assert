"""Logic to make use of LM Studio models."""
from openai import OpenAI


class BaseEngine:
    def __init__(self, base_url: str, api_key: str="not-needed"):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = "local-model"

    def ask_chat(self, system_message: str, user_message: str, temperature=0.7) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=temperature,
        )
        return completion.choices[0].message.content

class LMStudioEngine(BaseEngine):
    pass

class OpenAIEngine(BaseEngine):
    def __init__(self, base_url: str, api_key: str):
        if not api_key:
            raise ValueError("API key cannot be empty")
        super().__init__(base_url, api_key)


if __name__ == "__main__":
    engine = LMStudioEngine(base_url="http://localhost:1234/v1")
    answer = engine.ask_chat(
        system_message="Always answer in rhymes.",
        user_message="Introduce yourself.")
    print(answer)
