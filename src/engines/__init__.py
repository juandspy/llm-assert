from abc import ABC, abstractmethod

class Engine(ABC):
    """Engine is an interface that must be implemented by any LLM engine."""
    @abstractmethod
    def ask_chat(self, system_message: str, user_message: str, temperature=0.7) -> str:
        """Use an LLM to get a response."""
