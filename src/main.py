"""Main functions of the package."""
from typing import Any
from src.engines import Engine


class UnexpectedEngineResponseError(Exception):
    """Raised when the LLM Engine provides an unexpected response."""

# Characters we want to include on the answer
whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def llm_assert(engine: Engine, sut: Any, prompt: str):
    """
    Assert, using an LLM Engine, whether an input matches a prompt.
    
    This function queries an LLM engine using the prompt parameter,
    informing it that it can only respond with 'True' or 'False'.
    It filters the engine's response, removing any characters that are not letters.
    If the filtered response is not 'True' or 'False', it raises a ValueError.
    Otherwise, it returns a boolean value based on the response.

    Example:
        >>> engine = LMStudioEngine("http://localhost:1234/v1")
        >>> assert llm_assert(engine, "5", "this is a number")
        >>> assert llm_assert(engine, "apple", "this is a number")
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        AssertionError

    Args:
        engine (Engine): The LLM Engine to ask the question.
        sut (Any): The item under test.
        prompt (str): The question to ask the engine.
        
    Raises:
        UnexpectedEngineResponseError: If the engine's response is not 'True' or 'False'.
        AssertionError: If the engine's response is 'False'
    """
    answer = engine.ask_chat(
        system_message="""
        You can only answer 'True' or 'False', no matter what the input is.
        Don't provide any explanation.
        """,
        user_message=f"{sut}: {prompt}")
    answer = ''.join(filter(whitelist.__contains__, answer))
    if answer not in ["True", "False"]:
        raise UnexpectedEngineResponseError(
            f"Got unexpected answer from the LLM Engine: '{answer}'.")
    assert answer == "True", f"'{sut}' doesn't match the prompt '{prompt}'"
