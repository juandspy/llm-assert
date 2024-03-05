"""Test the main functions of the package."""
import pytest

from src.main import llm_assert
from src.engines.lmstudio import LMStudioEngine


INPUTS= [
    ("5", "this is a number", True),
    ("twenty", "this is a number", True),
    ("apple", "this is a number", False),
    ("5", "this is not a number", False),
    ("twenty", "this is not a number", False),
    ("apple", "this is not a number", True)
]

class MockEngine:
    def __init__(self, mocked_answer: str):
        self.mocked_answer = mocked_answer
    def ask_chat(self, system_message: str, user_message: str, temperature=0.7) -> str:
        return self.mocked_answer

@pytest.mark.parametrize("sut,prompt,expected_exception", INPUTS)
def test_llm_assert__mock(sut, prompt, expected_exception):
    """Test the assert function"""
    engine = MockEngine(str(expected_exception))
    if not expected_exception:
        with pytest.raises(AssertionError):
            llm_assert(engine, sut, prompt)
    else:
        llm_assert(engine, sut, prompt)


@pytest.mark.parametrize("sut,prompt,expected_exception", INPUTS)
def test_llm_assert__lmstudio(sut, prompt, expected_exception):
    """Test the assert function"""
    engine = LMStudioEngine("http://localhost:1234/v1")
    if not expected_exception:
        with pytest.raises(AssertionError):
            llm_assert(engine, sut, prompt)
    else:
        llm_assert(engine, sut, prompt)
