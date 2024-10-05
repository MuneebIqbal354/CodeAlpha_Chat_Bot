from nltk.chat.util import Chat, reflections

# New set of question-answer pairs
chats = [
    [
        r"my name is (.*)",
        ["Hey there %1, nice to meet you! How can I assist you today?", ]
    ],
    [
        r"(what is your name|who are you) ?",
        ["I go by Skyler, your friendly virtual assistant. Let's chat!", ]
    ],
    [
        r"how are you ?",
        ["I'm great, thanks for asking! How are things on your end?", ]
    ],
    [
        r"do you have friends ?",
        ["I've got a lot of virtual pals, and you're my favorite new friend!", ]
    ],
    [
        r"(.*) sorry (.*)",
        ["No worries, it's all good!", "Don't sweat it, friend!", ]
    ],
    [
        r"i'm doing (.*)",
        ["That's fantastic to hear!", "Good to know you're feeling %1!", ]
    ],
    [
        r"hi|hey|hello",
        ["Hi there!", "Hey! How can I assist you today?", ]
    ],
    [
        r"(.*) (your age|old are you) ?",
        ["I'm a program without an age, but let's just say I'm timeless!", ]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to provide you with helpful information and answers!", ]
    ],
    [
        r"who created you ?",
        ["I was developed as a project to explore NLTK's chat functionalities.", ]
    ],
    [
        r"where are you located ?",
        ["I exist in the cloud, but my virtual roots are in cyberspace!", ]
    ],
    [
        r"how is the weather in (.*)?",
        ["I'm not there, but I've heard it's always interesting in %1.", ]
    ],
    [
        r"i work at (.*)",
        ["%1 sounds like an exciting place! How do you like it?", ]
    ],
    [
        r"(.*) raining in (.*)",
        ["Weather can be unpredictable, but stay prepared in %2!", ]
    ],
    [
        r"how is your health ?",
        ["As a program, I'm always running in top condition!", ]
    ],
    [
        r"what sports do you like ?",
        ["I'm a big fan of chess—strategies are my thing!", ]
    ],
    [
        r"goodbye|quit",
        ["Goodbye! It was great talking to you. Catch you later!", "Take care! See you next time!"]
    ],
    [
        r"do you know everything ?",
        ["I can assist with most queries, but I’m always learning!", "Try me out, and let's see if I can help."]
    ],
    [
        r"(.*) siri",
        ["Ah, Siri! We go way back—small world, isn't it?", ]
    ],
    [
        r"(.*) (lost|directions)",
        ["Here's something that might help you: https://maps.google.com", ]
    ],
    [
        r"what's the weather like ?",
        ["You can get the latest weather updates here: https://www.accuweather.com"]
    ],
    [
        r"what (.*) like ?",
        ["I love chatting and helping people—it's my main job!", ]
    ],
]

def chatbot_intro():
    print("Hello! I'm Tom, ready for a friendly chat. Type 'quit' to end the conversation.")

# Initialize the chatbot
chat = Chat(chats, reflections)
if __name__ == "__main__":
    chatbot_intro()
chat.converse()
