"""Question matching for PYTHONA."""
import re

from knowledge_base import PYTHON_KNOWLEDGE

STOPWORDS = {
    "what", "is", "a", "an", "the", "are", "how", "do", "does", "in",
    "of", "to", "explain", "tell", "me", "about", "can", "you", "i",
}

TOPICS = {
    "python": ["python"],
    "variables": ["variable", "variables"],
    "data types": ["data type", "datatype"],
    "string": ["string", "strings"],
    "list": ["list", "lists"],
    "tuple": ["tuple", "tuples"],
    "set": ["set", "sets"],
    "dictionary": ["dictionary", "dictionaries", "dict"],
    "conditions": ["if else", "if statement", "conditional", "condition", "elif"],
    "loops": ["loop", "loops", "for loop", "while loop"],
    "functions": ["function", "functions"],
    "lambda": ["lambda"],
    "list comprehension": ["list comprehension"],
    "exceptions": ["exception", "exceptions", "exception handling", "try except"],
    "oop": ["class", "classes", "object", "objects", "oop", "oops"],
    "inheritance": ["inheritance", "inherit"],
    "polymorphism": ["polymorphism"],
    "recursion": ["recursion", "recursive"],
    "modules": ["module", "modules", "import"],
    "pip": ["pip"],
    "environment": ["virtual environment", "venv"],
    "file handling": ["file handling", "read file", "write file"],
    "generators": ["generator", "generators", "yield"],
    "decorators": ["decorator", "decorators"],
    "input": ["input", "user input"],
    "output": ["print", "printing", "output"],
    "type conversion": ["type conversion", "casting", "type casting"],
    "errors": ["error", "errors", "indexerror", "nameerror", "typeerror", "keyerror"],
    "syntax": ["syntax", "indentation"],
    "operators": ["operator", "operators"],
    "scope": ["scope", "global variable", "local variable"],
}

NOT_FOUND = """
## 🐍 PYTHONA

I couldn't find that topic in my current Python knowledge base.

Try asking:

- What is Python?
- What is a variable?
- What is a list?
- What is a dictionary?
- What is a function?
- What is inheritance?
- What is exception handling?
- What is recursion?
- What is a generator?
- What is a decorator?
- What is NameError?
"""


def normalize_text(text):
    text = re.sub(r"[^\w\s]", " ", text.lower())
    return " ".join(text.split())


def _keywords(text):
    return set(text.split()) - STOPWORDS


def find_best_answer(question):
    question = normalize_text(question)
    if not question:
        return None

    q_words = _keywords(question)
    best, best_score = None, 0

    for item in PYTHON_KNOWLEDGE:
        stored_q = normalize_text(item["question"])
        stored_topic = normalize_text(item["topic"])

        score = 0
        if question == stored_q:
            score += 100
        score += len(q_words & _keywords(stored_q)) * 20
        score += len(q_words & set(stored_topic.split())) * 15
        if stored_q in question:
            score += 50
        if question in stored_q:
            score += 40

        if score > best_score:
            best, best_score = item, score

    return best if best_score >= 20 else None


def detect_topic(question):
    """Whole-word match; the longest matching keyword wins."""
    question = normalize_text(question)
    best_topic, best_len = None, 0
    for topic, words in TOPICS.items():
        for word in words:
            if len(word) > best_len and re.search(rf"\b{re.escape(word)}\b", question):
                best_topic, best_len = topic, len(word)
    return best_topic


def find_topic_answer(topic):
    if not topic:
        return None
    topic = normalize_text(topic)
    for item in PYTHON_KNOWLEDGE:
        if normalize_text(item["topic"]) == topic:
            return item
    return None


def chatbot_response(question):
    question = question.strip()
    if not question:
        return {"topic": "general", "response": "Please enter a Python question."}

    result = find_best_answer(question) or find_topic_answer(detect_topic(question))
    if result:
        return {"topic": result["topic"], "response": result["answer"]}
    return {"topic": "general", "response": NOT_FOUND}