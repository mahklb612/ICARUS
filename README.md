This guide explains how to set up ICARUS, including creating the `icarus.py` file, adding the API key, installing requirements, and running the chatbot in VS Code.

It covers:

- How to get a Gemini API key from Google AI Studio
- How to create the `icarus.py` file
- How to create the `.env` file
- How to create the `requirements.txt` file
- How to install the required Python packages
- How to run ICARUS from VS Code

---

## 1. Project Folder

Your project folder should contain the following files:

```text
icarus_chatbot/
│
├── icarus.py
├── .env
├── requirements.txt
└── README.md
```

If `icarus.py`, `.env`, or `requirements.txt` do not exist yet, create them using the steps below.

---

## 2. Get a Gemini API Key from Google AI Studio

1. Open Google AI Studio in your web browser:

```text
https://aistudio.google.com/
```

2. Sign in using your Google account.

3. Select **Get API key**.

4. Select **Create API key**.

5. Copy the generated API key.

6. Keep the API key private. Do not share it, email it, or upload it to GitHub.

---

## 3. Create the `icarus.py` File

In the same project folder, create a Python file named:

```text
icarus.py
```

This file contains the ICARUS chatbot program. Copy the following code into `icarus.py`:

```python
"""
11.1HD - Exploring AI Chatbots for beginners

ICARUS is a basic Gemini chatbot using Google AI Studio API key.

"""

import os
from dotenv import load_dotenv
from google import genai


BOT_NAME = "ICARUS"


def load_api_key():
    """
    Load the Gemini API key from the .env file.

    Returns:
        str: The Gemini API key.

    Raises:
        ValueError: If the API key is missing.
    """
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY was not found. "
            "Please add it to your .env file."
        )

    return api_key


def create_chatbot(api_key):
    """
    Create and return a Gemini chat session.

    Args:
        api_key (str): The Gemini API key.

    Returns:
        Chat: A Gemini chat session.
    """
    client = genai.Client(api_key=api_key)

    chat = client.chats.create(
        model="gemini-2.5-flash"
    )

    return chat


def run_chatbot():
    """
    Run the terminal-based ICARUS chatbot.
    """
    print("=" * 50)
    print(f"{BOT_NAME} - Gemini Basic Chatbot")
    print("Type 'exit', 'quit', or 'bye' to stop.")
    print("=" * 50)

    try:
        api_key = load_api_key()
        chat = create_chatbot(api_key)

        while True:
            user_message = input("\nYou: ").strip()

            if user_message.lower() in ["exit", "quit", "bye"]:
                print(f"\n{BOT_NAME}: Goodbye!")
                break

            if user_message == "":
                print(f"{BOT_NAME}: Please type a message.")
                continue

            response = chat.send_message(user_message)

            print(f"\n{BOT_NAME}: {response.text}")

    except ValueError as error:
        print(f"\nConfiguration Error: {error}")

    except Exception as error:
        print(f"\nUnexpected Error: {type(error).__name__}: {error}")


if __name__ == "__main__":
    run_chatbot()
```

Save the file before continuing.

---

## 4. Create the `.env` File

In the same folder as `icarus.py`, create a file named:

```text
.env
```

Add the following line to the `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with the API key copied from Google AI Studio.

Example format:

```text
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxxx
```

Important notes:

- Do not put spaces around the equals sign.
- Do not place the API key inside quotation marks.
- Make sure the file is named `.env`, not `.env.txt`.
- Keep this file in the same folder as `icarus.py`.

## 5. Create the `requirements.txt` File

In the same folder as `icarus.py`, create a file named:

```text
requirements.txt
```

Add the following package names:

```text
google-genai
python-dotenv
```

These packages are required because:

- `google-genai` allows Python to communicate with the Gemini API.
- `python-dotenv` allows Python to load the API key from the `.env` file.

---

## 6. Open the Project in VS Code

1. Open Visual Studio Code.
2. Select **File**.
3. Select **Open Folder**.
4. Choose your ICARUS project folder.
5. Open the VS Code terminal using:

```text
Terminal > New Terminal
```

---

## 7. Install the Requirements

Install the required packages using:

```text
pip install -r requirements.txt
```

Alternatively, you can install the packages directly:

```text
pip install google-genai python-dotenv
```

---

## 8. Run ICARUS

After the packages are installed and the `.env` file is ready, run the chatbot from the VS Code terminal:

```text
python icarus.py
```

If `python` does not work on macOS or Linux, try:

```text
python3 icarus.py
```

---

## 9. Expected Output

When ICARUS starts successfully, you should see output similar to this:

```text
==================================================
ICARUS - Gemini Basic Chatbot
Type 'exit', 'quit', or 'bye' to stop.
==================================================

You:
```

You can then type a message and press Enter.

Example:

```text
You: Hello

ICARUS: Hello! How can I help you today?
```

To stop the chatbot, type:

```text
exit
```

or:

```text
quit
```

or:

```text
bye
```

---

## 10. Troubleshooting Common Problems

### Problem: `GEMINI_API_KEY was not found`

Check that:

- The `.env` file is in the same folder as `icarus.py`.
- The file is named exactly `.env`.
- The variable name is exactly `GEMINI_API_KEY`.
- There are no spaces around the equals sign.

Correct format:

```text
GEMINI_API_KEY=your_api_key_here
```

---

### Problem: `ModuleNotFoundError: No module named 'dotenv'`

This means `python-dotenv` is not installed.

Fix:

```text
pip install python-dotenv
```

---

### Problem: `ModuleNotFoundError: No module named 'google'`

This means `google-genai` is not installed.

Fix:

```text
pip install google-genai
```

---

### Problem: Invalid API key

Check that:

- The full API key was copied from Google AI Studio.
- The API key was pasted correctly into the `.env` file.
- The API key has not been deleted.
- The `.env` file does not contain extra spaces or quotation marks.

---

## 11. Final Checklist

Before running ICARUS, confirm the following:

- `icarus.py` is in the project folder.
- `.env` is in the project folder.
- `.env` contains `GEMINI_API_KEY=your_api_key_here`.
- `requirements.txt` contains `google-genai` and `python-dotenv`.
- The virtual environment is activated.
- The required packages are installed.
- The chatbot is started using `python icarus.py`.
