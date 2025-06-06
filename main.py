import nltk
from nltk.tokenize import sent_tokenize
import random
import uuid
import language_tool_python
import os

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

chat_history = []
notes = []
tasks = []

game_active = False
secret_number = 0
attempts = 0
max_attempts = 7

grammar_tool = None
try:
    grammar_tool = language_tool_python.LanguageTool('en-US')
except Exception as e:
    print(f"\n--- ERROR: LanguageTool Initialization Failed ---")
    print(f"Details: {e}")
    print("Grammar checking functionality will be disabled.")
    print("--------------------------------------------------\n")


def generate_user_id():
    return str(uuid.uuid4())[:8]

def display_anonymous_chat():
    if chat_history:
        return "\n--- Anonymous Chat ---\n" + "\n".join(chat_history) +"\n----------------------"
    return "No messages yet."

def start_anonymous_chat():
    print("🔒 Entered Anonymous Chat")
    user_id = generate_user_id()
    print(f"🔹 Your ID: {user_id}")
    print("Type 'exit' to leave chat, 'show' to view chat.\n")

    while True:
        message = input(f"{user_id}: ")
        if message.lower() == "exit":
            return "👋 You left anonymous chat."
        elif message.lower() == "show":
            print(display_anonymous_chat())
        else:
            chat_history.append(f"{user_id}: {message}")
            print(f"Message added to chat history.")

def summarize_text(text, max_sentences=3):
    sentences = sent_tokenize(text)
    summary = " ".join(sentences[:min(len(sentences), max_sentences)])
    return summary

def check_grammar(text):
    if grammar_tool is None:
        return "❌ Grammar checker is not available due to initialization error."

    try:
        matches = grammar_tool.check(text)
        if matches:
            suggestions = []
            for match in matches:
                message = match.message
                replacements = match.replacements
                context = text[match.offset:match.offset + match.errorLength]
                rule_id = match.ruleId

                replacement_str = ", ".join(replacements) if replacements else "N/A"

                suggestion_str = (
                    f"  - Problem: '{context}'\n"
                    f"    Suggestion: '{replacement_str}'\n"
                    f"    Info: {message}"
                )
                suggestions.append(suggestion_str)

            return "⚠️ Grammar Suggestions:\n" + "\n".join(suggestions)
        else:
            return "✅ No grammar suggestions found or text is correct."
    except Exception as e:
        return f"❌ An error occurred during grammar checking: {e}"

def display_help_menu():
    return (
        "--- Chatbot Help Menu ---\n"
        "Welcome! I'm your friendly AI assistant Sophia v2. Here's a list of commands you can use:\n\n"
        "### General Commands\n"
        "* **`hello`**: Get a friendly greeting from me!\n"
        "    * *Example:* `hello`\n"
        "* **`help`**: Display this help menu.\n"
        "    * *Example:* `help`\n"
        "* **`exit`**: Quit the chatbot application.\n"
        "    * *Example:* `exit`\n\n"
        "### Text Processing Tools\n"
        "* **`summarize: [your text here]`**: Get a concise summary of the text you provide.\n"
        "    * *Example:* `summarize: The quick brown fox jumps over the lazy dog. This is a very interesting story.`\n"
        "* **`check grammar: [your sentence here]`**: I'll check your sentence for grammar and spelling errors and suggest corrections.\n"
        "    * *Example:* `check grammar: I is going to the store.`\n\n"
        "### Anonymous Chat\n"
        "* **`start anonymous chat`**: Enter a private chat room where you can communicate with a temporary, unique ID.\n"
        "    * *Example:* `start anonymous chat`\n"
        "    * *Once inside the anonymous chat:*\n"
        "        * Type **`exit`** to leave the anonymous chat.\n"
        "        * Type **`show`** to view the entire chat history.\n\n"
        "### Games\n"
        "* **`play guess the number`**: Start a game where you try to guess my secret number.\n"
        "    * *Example:* `play guess the number`\n"
        "    * *During the game:*\n"
        "        * Type a number to guess.\n"
        "        * Type **`quit game`** to end the game early.\n\n"
        "### What's Next? (Coming Soon!)\n"
        "We're constantly working to improve! Here are some features planned for future updates:\n"
        "* **Notes & Tasks:** Add, view, and manage your personal notes and to-do lists directly within the chat.\n"
        "* **Reminders:** Set timely reminders for important events or tasks.\n"
        "* **Unit Converter:** Easily convert between different units of measurement (e.g., miles to kilometers).\n"
        "* **Information Retrieval:** Ask for definitions, synonyms, random facts, and more!\n\n"
        "-------------------------"
    )

def handle_game_input(user_input):
    global game_active, attempts, secret_number, max_attempts

    if user_input.lower() == "quit game":
        game_active = False
        return "Okay, you quit the game. The secret number was {}. Goodbye!".format(secret_number)

    try:
        guess = int(user_input)
        attempts += 1

        if guess < secret_number:
            response = f"Higher! You have {max_attempts - attempts} attempts left."
        elif guess > secret_number:
            response = f"Lower! You have {max_attempts - attempts} attempts left."
        else:
            game_active = False
            return f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!"

        if attempts >= max_attempts and game_active:
            game_active = False
            return f"Out of attempts! The secret number was {secret_number}. Better luck next time!"

        return response
    except ValueError:
        return "That's not a valid number. Please enter a whole number or 'quit game'."

def generate_response(user_input):
    global game_active, secret_number, attempts

    if game_active:
        return handle_game_input(user_input)

    user_input_lower = user_input.lower()

    if user_input_lower.startswith("summarize:"):
        text_to_summarize = user_input[len("summarize:"):].strip()
        if text_to_summarize:
            summary = summarize_text(text_to_summarize)
            return f"Here’s the summary:\n{summary}"
        else:
            return "Please provide the text to summarize after 'summarize:'."
    elif user_input_lower.startswith("check grammar:"):
        text_to_check = user_input[len("check grammar:"):].strip()
        if text_to_check:
            return check_grammar(text_to_check)
        else:
            return "Please provide the sentence to check after 'check grammar:'."
    elif user_input_lower == "start anonymous chat":
        return start_anonymous_chat()
    elif user_input_lower.startswith("hello"):
      
        return "Hello there! How can I assist you today?"
    elif user_input_lower == "help":
        return display_help_menu()
      
    elif user_input_lower == "play guess the number":
        game_active = True
        secret_number = random.randint(1, 100)
        attempts = 0
        return "I'm thinking of a number between 1 and 100. You have {} attempts. What's your first guess?".format(max_attempts)
    elif user_input_lower == "exit":
      
        return "Exiting the chatbot."
    else:
      
        return "I'm not sure how to respond to that. Type 'help' for a list of commands."

if __name__ == "__main__":
    print("Welcome to the Sophia v2 Chat Bot!")
    print("Type 'help' for a list of commands, or 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print(f"Bot: {response}")
