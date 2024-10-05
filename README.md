<h1 align="center">Task No. 2: Chatbot</h1>

This project implements a rule-based chatbot built using Python's Natural Language Toolkit (NLTK). This chatbot can engage in simple conversations, answer frequently asked questions, and provide links to useful resources. It demonstrates the basic implementation of a 
chatbot using the `nltk.chat.util` module.

### Features:

- Engages in small talk and casual conversations.
- Answers questions about weather, work, and other general topics.
- Provides useful links to services like Google Maps and weather updates.
- User-friendly interactions with customizable responses.

### Prerequisites:

- Python 3.x installed on your system.
- The NLTK library installed.

## Code Explanation

The chatbot uses a predefined set of patterns and responses. When you type a message, Skyler searches for a matching pattern and returns a corresponding response. The patterns are regular expressions that recognize specific user inputs, allowing the chatbot to respond accordingly.

```
from nltk.chat.util import Chat, reflections
```

This line imports the necessary modules from NLTK. The `Chat` class provides the framework for the rule-based chatbot, while `reflections` allows the chatbot to reflect the user's statements (like turning "I" into "you").

### 1. Defining Patterns and Responses

The chatbot's responses are defined in the QA list as a set of patterns (regular expressions) paired with responses. For example:

```
chats = [
    [
        r"my name is (.*)",
        ["Hey there %1, nice to meet you! How can I assist you today?", ]
    ],
    [
        r"(what is your name|who are you) ?",
        ["I go by Skyler, your friendly virtual assistant. Let's chat!", ]
    ],
    # Additional patterns and responses...
]
```

Each entry in the chats list contains:

- A regular expression to match the user's input (e.g., "my name is (.*)").
- A response list with placeholders for dynamic text (e.g., `%1` will be replaced with the user's name).

### 2. Reflections

The `reflections` dictionary is a default set of rules to convert user statements to the chatbot’s perspective. For example, "I am" becomes "you are" to make the conversation feel more natural.

### 3. Initializing the Chatbot

The `Chat` class takes the `chats` list and `reflections` as input to initialize the chatbot:

```
chat = Chat(chats, reflections)
```

### 4. Starting the Conversation

The function chatbot_intro() prints an introduction message when the chatbot starts:

```
def chatbot_intro():
    print("Hello! I'm Skyler, ready for a friendly chat. Type 'quit' to end the conversation.")
```

Finally, the chatbot is started with:

```
if __name__ == "__main__":
    chatbot_intro()
    chat.converse()
```

When you run the script, the chatbot will prompt you to enter messages. It will continue the conversation until you type "quit."

### Example:

```
You: hello
Tom: Hi there!

You: what is your name?
Tom: I go by Skyler, your friendly virtual assistant. Let's chat!

You: how is the weather in London?
Skyler: I'm not there, but I've heard it's always interesting in London.

You: quit
Tom: Goodbye! It was great talking to you. Catch you later!
```
