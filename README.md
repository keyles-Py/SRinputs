# SRinputs - Smart & Reliable Inputs Suite
![License](https://img.shields.io/github/license/keyles-Py/SRinputs)

A comprehensive Python suite designed to supercharge the built-in `input()` function. Whether you need to validate real user data or simulate fake information for testing, **SRinputs** has you covered.

## Installation

```bash
pip install SRinputs
```
## Modules
The package is now divided into two specialized modules:
1. **SRinputs** (Static & Repetitive)Focuses on safe data collection from real users. It handles validation, language detection, and prevents common crashes.
* Type Validation: Supports int, float, and str.

* Safety: Catch KeyboardInterrupt and EOFError gracefully.

* Persistence: Mandatory entries by default (no more empty inputs by mistake).

* Bulk Collection: multiInput to gather lists of data easily.

2. **FRinputs** (Fake & Random) Designed for developers and students. It "mocks" inputs using the Faker library, allowing you to test your classes and functions without typing a single word in the terminal.

* Zero-Typing Testing: Simulates input automatically.

* Realistic Data: Names (by gender), Emails, URLs, IDs, and Social Media Handles.

* Customizable: Supports custom prompts and formats.

## Usage Examples

Safe User Input (SR)
```
from SRinputs.SRinputs import IntInput, multiInput

# Validates an integer

age = IntInput("Please enter your age: ")

# Collects exactly 5 names in a list

names = multiInput(5, "Enter a student name: ")
```
## Automated Testing / Mocking (FR)
Ideal for testing your classes without manual input:

```
from SRinputs.FRinputs import FRNameInput, FRHandleInput, FREmailInput

class User:
    def __init__(self, name, handle, email):
        self.name = name
        self.handle = handle
        self.email = email

# No terminal typing required! Data is generated and "injected" automatically.
user1 = User(
    name = FRNameInput(),
    handle = FRHandleInput(),
    email = FREmailInput()
)

print(f"Created: {user1.name} ({user1.handle})")
```
## Supported Types (FR Module)


| Function | Description |
|---|---|
| FRNameInput | Generates names (supports 'male', 'female', 'nonbinary'). |
| FRDateInput | enerates dates with multiple format options (0-3). |
| FRHandleInput | Generates social media handles like @name_123. |
| FRIdInput | Generates IDs (8-10 digits). |
| FREmailInput | Generates random email addresses. |
| FRUrlInput | Generates fake website links. |