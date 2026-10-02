"""Short learning tips. Keys match the topic names used in chatbot.TOPICS."""

TIPS = {
    "variables": "💡 Think of a variable as a labeled box containing a value.",
    "functions": "💡 Break large programs into small reusable functions.",
    "list": "💡 Python list indexing starts from zero.",
    "loops": "💡 Before writing a loop, identify what changes in every iteration.",
    "oop": "💡 Learn classes and objects first, then inheritance and polymorphism.",
    "exceptions": "💡 Handle specific exceptions instead of catching every error.",
    "dictionary": "💡 Dictionaries are useful when data has meaningful keys.",
}
DEFAULT_TIP = "💡 Practice one Python concept at a time and write small programs."


def get_mentor_tip(topic):
    return TIPS.get(topic, DEFAULT_TIP)