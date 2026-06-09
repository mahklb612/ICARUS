
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
