# SRinputs - Static Repetitive inputs

A small Python package that improves the usage of the built-in input() function with functionalities such as static and multiple inputs.

## Instalation

You can install it using pip.

```bash
pip install SRinputs
```

## Features

* **Type validation:** Requests and validates inputs such as `int`, `float` or `str`.
* **Error handling:** Catch `KeyboardInterrupt` and `EOFError` in a user friendly way, allowing the program to continue.
* Mandatory entries:** Ensures that the user enters a valid value before continuing, avoiding empty entries by default.
* Multiple entries:** Requests a specific number of entries and returns them in a list.