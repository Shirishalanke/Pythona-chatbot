"""
PYTHONA knowledge base.

Each entry needs: question, topic, answer.
`topic` must match a topic name in chatbot.TOPICS
(e.g. "list", "loops", "oop") so topic detection can find it.

To add a new entry, copy any line at the bottom of this file:
    _entry(topic, question, explanation, code, output)
"""
from textwrap import dedent


def _entry(topic, question, explanation, code, output, lang="python"):
    code = dedent(code).strip()
    output = dedent(output).strip()
    answer = (
        f"## 🐍 {question}\n\n"
        f"{explanation}\n\n"
        f"**Example:**\n\n```{lang}\n{code}\n```\n\n"
        f"**Output:**\n\n```\n{output}\n```"
    )
    return {"question": question, "topic": topic, "answer": answer}


PYTHON_KNOWLEDGE = [
    _entry(
        "python", "What is Python?",
        "Python is a high-level, interpreted, general-purpose programming "
        "language known for its clean, readable syntax. It is used for web "
        "development, data science, automation, AI and more.",
        'print("Hello, Python!")',
        "Hello, Python!",
    ),
    _entry(
        "variables", "What is a variable?",
        "A variable is a name that stores a value. You create one by "
        "assigning a value with `=`. Python figures out the type itself.",
        """
        name = "Asha"
        x = 10
        print(name, x)
        """,
        "Asha 10",
    ),
    _entry(
        "data types", "What are data types?",
        "Data types describe what kind of value something is. The common "
        "ones are `int`, `float`, `str`, `bool`, `list`, `tuple`, `set` "
        "and `dict`. Use `type()` to check one.",
        'print(type(10), type(3.14), type("hi"), type(True))',
        "<class 'int'> <class 'float'> <class 'str'> <class 'bool'>",
    ),
    _entry(
        "string", "What is a string?",
        "A string is text inside quotes. Strings are indexed from 0 and "
        "come with many helpful methods such as `upper()` and `replace()`.",
        """
        s = "Python"
        print(s.upper())
        print(s[0])
        print(len(s))
        """,
        """
        PYTHON
        P
        6
        """,
    ),
    _entry(
        "list", "What is a list?",
        "A list is an ordered, changeable collection written in square "
        "brackets. Indexing starts at 0.",
        """
        fruits = ["apple", "banana"]
        fruits.append("mango")
        print(fruits)
        print(fruits[0])
        """,
        """
        ['apple', 'banana', 'mango']
        apple
        """,
    ),
    _entry(
        "tuple", "What is a tuple?",
        "A tuple is an ordered collection written in round brackets. "
        "Unlike a list, it cannot be changed after it is created.",
        """
        point = (3, 4)
        print(point[0], point[1])
        """,
        "3 4",
    ),
    _entry(
        "set", "What is a set?",
        "A set is an unordered collection of unique items. Duplicates are "
        "removed automatically.",
        """
        numbers = {1, 2, 2, 3}
        print(numbers)
        """,
        "{1, 2, 3}",
    ),
    _entry(
        "dictionary", "What is a dictionary?",
        "A dictionary stores data as key-value pairs. Use the key to "
        "look up its value.",
        """
        player = {"name": "Virat", "sport": "cricket"}
        print(player["name"])
        player["country"] = "India"
        print(player)
        """,
        """
        Virat
        {'name': 'Virat', 'sport': 'cricket', 'country': 'India'}
        """,
    ),
    _entry(
        "conditions", "What are conditional statements?",
        "Conditions let your program make decisions using `if`, `elif` "
        "and `else`. Indentation shows which code belongs to each branch.",
        """
        age = 20
        if age >= 18:
            print("Adult")
        else:
            print("Minor")
        """,
        "Adult",
    ),
    _entry(
        "loops", "What are loops?",
        "A loop repeats code. Use a `for` loop to go through a sequence "
        "and a `while` loop to repeat until a condition becomes false.",
        """
        for i in range(3):
            print(i)

        count = 0
        while count < 2:
            print("tick")
            count += 1
        """,
        """
        0
        1
        2
        tick
        tick
        """,
    ),
    _entry(
        "functions", "What is a function?",
        "A function is a reusable block of code defined with `def`. It can "
        "take inputs (parameters) and send back a result with `return`.",
        """
        def greet(name):
            return f"Hello, {name}!"

        print(greet("Asha"))
        """,
        "Hello, Asha!",
    ),
    _entry(
        "lambda", "What is a lambda function?",
        "A lambda is a small anonymous function written in one line. It is "
        "handy for short, simple operations.",
        """
        square = lambda x: x * x
        print(square(5))
        """,
        "25",
    ),
    _entry(
        "list comprehension", "What is list comprehension?",
        "List comprehension is a short way to build a list from a loop in "
        "a single line.",
        """
        squares = [n * n for n in range(1, 6)]
        print(squares)
        """,
        "[1, 4, 9, 16, 25]",
    ),
    _entry(
        "exceptions", "What is exception handling?",
        "Exception handling stops your program from crashing when an error "
        "occurs. Put risky code in `try` and handle the problem in `except`.",
        """
        try:
            print(10 / 0)
        except ZeroDivisionError:
            print("Cannot divide by zero")
        """,
        "Cannot divide by zero",
    ),
    _entry(
        "oop", "What is a class and an object?",
        "A class is a blueprint, and an object is a thing made from that "
        "blueprint. Classes group data (attributes) and behaviour (methods).",
        """
        class Dog:
            def __init__(self, name):
                self.name = name

            def bark(self):
                print(f"{self.name} says Woof!")

        Dog("Tommy").bark()
        """,
        "Tommy says Woof!",
    ),
    _entry(
        "inheritance", "What is inheritance?",
        "Inheritance lets a child class reuse the attributes and methods "
        "of a parent class.",
        """
        class Animal:
            def speak(self):
                print("Some sound")

        class Dog(Animal):
            pass

        Dog().speak()
        """,
        "Some sound",
    ),
    _entry(
        "polymorphism", "What is polymorphism?",
        "Polymorphism means different classes can share the same method "
        "name, and each one behaves in its own way.",
        """
        class Cat:
            def speak(self):
                print("Meow")

        class Dog:
            def speak(self):
                print("Woof")

        for animal in (Cat(), Dog()):
            animal.speak()
        """,
        """
        Meow
        Woof
        """,
    ),
    _entry(
        "recursion", "What is recursion?",
        "Recursion is when a function calls itself. It needs a base case "
        "to stop, otherwise it never ends.",
        """
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)

        print(factorial(5))
        """,
        "120",
    ),
    _entry(
        "modules", "What is a module?",
        "A module is a Python file containing code you can reuse. Bring it "
        "into your program with `import`.",
        """
        import math
        print(math.sqrt(16))
        """,
        "4.0",
    ),
    _entry(
        "pip", "What is pip?",
        "pip is Python's package installer. It downloads libraries from "
        "PyPI so you can use them in your projects. Run it in the terminal.",
        "pip install requests",
        "Successfully installed requests",
        lang="bash",
    ),
    _entry(
        "environment", "What is a virtual environment?",
        "A virtual environment is an isolated space for a project's "
        "packages, so different projects don't clash. Create it with `venv`.",
        """
        python -m venv venv
        venv\\Scripts\\activate      # Windows
        source venv/bin/activate    # Mac/Linux
        """,
        "(venv) appears at the start of your terminal prompt",
        lang="bash",
    ),
    _entry(
        "file handling", "What is file handling?",
        "File handling lets you read and write files. The `with` statement "
        "closes the file for you automatically.",
        """
        with open("notes.txt", "w") as f:
            f.write("Hello file")

        with open("notes.txt") as f:
            print(f.read())
        """,
        "Hello file",
    ),
    _entry(
        "generators", "What is a generator?",
        "A generator produces values one at a time using `yield` instead of "
        "building the whole list in memory.",
        """
        def count_up(n):
            for i in range(1, n + 1):
                yield i

        for x in count_up(3):
            print(x)
        """,
        """
        1
        2
        3
        """,
    ),
    _entry(
        "decorators", "What is a decorator?",
        "A decorator wraps a function to add extra behaviour without "
        "changing its code. You apply it with the `@` symbol.",
        """
        def shout(func):
            def wrapper():
                print(func().upper())
            return wrapper

        @shout
        def hello():
            return "hello"

        hello()
        """,
        "HELLO",
    ),
    _entry(
        "input", "How do I take user input?",
        "Use `input()` to read what the user types. It always returns a "
        "string.",
        """
        name = input("Enter your name: ")
        print("Hello,", name)
        """,
        """
        Enter your name: Asha
        Hello, Asha
        """,
    ),
    _entry(
        "output", "How do I print output?",
        "`print()` shows output on the screen. Use `sep` to change the "
        "separator and f-strings to insert values.",
        """
        print("Hello", "World", sep="-")
        print(f"2 + 3 = {2 + 3}")
        """,
        """
        Hello-World
        2 + 3 = 5
        """,
    ),
    _entry(
        "type conversion", "What is type conversion?",
        "Type conversion (casting) changes a value from one type to "
        "another using `int()`, `float()`, `str()` and similar functions.",
        """
        age = "21"
        print(int(age) + 1)
        print(str(5) + "5")
        """,
        """
        22
        55
        """,
    ),
    _entry(
        "errors", "What are Python errors?",
        "Errors tell you something went wrong. Syntax errors stop the "
        "program from starting, while exceptions such as `NameError`, "
        "`TypeError`, `IndexError` and `KeyError` happen while it runs. "
        "Read the last line of the message first.",
        """
        try:
            print(undefined_name)
        except NameError as e:
            print("Caught:", e)
        """,
        "Caught: name 'undefined_name' is not defined",
    ),
    _entry(
        "errors", "What is NameError?",
        "A `NameError` means Python can't find a variable or function name. "
        "Usually it is misspelled or was never defined.",
        """
        print(username)
        """,
        "NameError: name 'username' is not defined",
    ),
    _entry(
        "syntax", "What is Python syntax?",
        "Syntax is the set of rules for writing valid Python. Python uses "
        "indentation (4 spaces) instead of braces, and block statements "
        "end with a colon. Breaking these rules gives a `SyntaxError` or "
        "`IndentationError`.",
        """
        if True:
            print("Indented correctly")
        """,
        "Indented correctly",
    ),
    _entry(
        "operators", "What are operators?",
        "Operators perform actions on values: arithmetic (`+ - * / // % **`), "
        "comparison (`== != < >`) and logical (`and or not`).",
        "print(7 + 3, 7 - 3, 7 * 3, 7 / 2, 7 // 2, 7 % 2, 2 ** 3)",
        "10 4 21 3.5 3 1 8",
    ),
    _entry(
        "scope", "What is variable scope?",
        "Scope decides where a variable can be used. A variable created "
        "inside a function is local to it, while one created outside is "
        "global.",
        """
        x = "global"

        def show():
            x = "local"
            print(x)

        show()
        print(x)
        """,
        """
        local
        global
        """,
    ),
]