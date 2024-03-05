# Assert LLM

A tool for lazy people that doesn't want to spend time on writing tests.

(Just a project that I wrote for fun)

## How to run

Install the required packages with `pip install .`

Load any model on [LM Studio](https://lmstudio.ai) and start the "Local Inference Server".
Assuming it's configured to expose the port `1234` on localhost, you can use this tool
on your unit tests like this:

```
>>> from src.main import llm_assert
>>> from src.engines.lmstudio import LMStudioEngine
>>> engine = LMStudioEngine("http://localhost:1234/v1")
>>> llm_assert(engine, "5", "this is a number")
>>> llm_assert(engine, "5", "this is not a number")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jdiazsua/Documents/Projects/PoCs/assert-llm/src/main.py", line 49, in llm_assert
    assert answer == "True", f"'{sut}' doesn't match the prompt '{prompt}'"
           ^^^^^^^^^^^^^^^^
AssertionError: '5' doesn't match the prompt 'this is not a number'
```

This looks like an overkill, but it can be useful for lazy checks like:

```
>>> input_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
123 Elm Street, Springfield, IL 62704.
Vivamus aliquet, augue id semper varius, ex tellus luctus justo, nec viverra metus lectus nec magna.
"""
>>> llm_assert(engine, input_text, "it contains an address")
>>> llm_assert(engine, input_text, "it contains a telephone number")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/jdiazsua/Documents/Projects/PoCs/assert-llm/src/main.py", line 49, in llm_assert
    assert answer == "True", f"'{sut}' doesn't match the prompt '{prompt}'"
           ^^^^^^^^^^^^^^^^
AssertionError: '
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
123 Elm Street, Springfield, IL 62704.
Vivamus aliquet, augue id semper varius, ex tellus luctus justo, nec viverra metus lectus nec magna.
' doesn't match the prompt 'it contains a telephone number'
```

## Contributing

Feel free to add new engines to the [engines](src/engines/) package. The only requirement is that
they must implement the `Engine` interface, as it will be used by the `llm_assert` function.

You can also contribute by adding new functions with different `system_message` and `prompt`
or calling different APIs.
