# Sophia v2: Your Personal AI Chatbot Assistant

Sophia v2 is a versatile command-line chatbot designed to help you with various tasks, from grammar checking and text summarization to engaging in anonymous conversations and even playing a simple game!

---

## ✨ Features

* **Grammar & Spelling Check:** Get instant suggestions for improving your text.
* **Text Summarization:** Condense long pieces of text into short, digestible summaries.
* **Anonymous Chat:** Engage in a private, temporary chat session with a unique ID.
* **Guess the Number Game:** Play a fun guessing game with the bot.
* **Help Menu:** Easily discover all available commands and how to use them.

---

## 🚀 Getting Started

Follow these steps to get Sophia v2 up and running on your system, especially if you're using Replit.

### Prerequisites

* **Python 3.x**
* **Java Development Kit (JDK):** `language-tool-python` relies on Java. Most Replit environments come with Java pre-installed.

### Installation

1.  **Clone or Download the Project:**
    If you're using Replit, simply open your project. If you're setting this up locally, download the code files to your computer.

2.  **Create `requirements.txt`:**
    In the root directory of your project, create a file named `requirements.txt` (if it doesn't already exist). Add the following lines to it:
    ```
    nltk
    language-tool-python
    ```

3.  **Install Dependencies:**
    Replit usually installs packages automatically from `requirements.txt`. If not, or if you're running locally, open your terminal/shell and run:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Chatbot

1.  **Execute the Main Script:**
    Open your terminal or Replit's shell and run the main Python file:
    ```bash
    python main.py
    ```
    (Replace `main.py` with the actual name of your Python file if it's different.)

2.  **First Run (Important!):**
    The very first time you run Sophia v2, the `language-tool-python` library will download necessary language models. This can take anywhere from **30 seconds to a few minutes** depending on your internet connection and system performance. Please be patient during this initial setup.

---

## 🤖 How to Use

Once the bot is running, you can type commands in the input prompt. Here are some examples:

* `hello`
* `help`
* `summarize: Artificial intelligence is a wide-ranging branch of computer science concerned with building smart machines capable of performing tasks that typically require human intelligence.`
* `check grammar: He dont like it.`
* `start anonymous chat`
* `play guess the number`
* `exit`

---

## 🔮 Future Ideas

We're always thinking about how to make Sophia v2 even better! Here are some features we might add in the future:

* **Personal Notes & Tasks:** Manage your to-do lists and quick notes.
* **Reminders:** Set timely notifications for events.
* **Unit Conversion:** Convert between various units of measurement.
* **External Information:** Fetch definitions, synonyms, random facts, and more from online sources.
* **Improved Conversational Flow:** Make interactions feel even more natural and intuitive.

---

## 🛠️ Technologies Used

* **Python:** The core programming language.
* **NLTK (Natural Language Toolkit):** For text processing like sentence tokenization.
* **`language-tool-python`:** For robust grammar and spelling checking.
* **`uuid`:** For generating unique identifiers (used in anonymous chat).
* **`random`:** For game logic.
