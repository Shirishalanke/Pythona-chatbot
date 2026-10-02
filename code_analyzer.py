"""Syntax checking and common-error explanations."""
import ast

FENCE = "```"


def analyze_code(code):
    if not code.strip():
        return {"success": False, "message": "Please enter some Python code."}

    try:
        ast.parse(code)
    except SyntaxError as error:
        return {
            "success": False,
            "message": (
                "### 🕵️ Code Detective Found a Problem\n\n"
                f"**Error:** {error.msg}\n\n"
                f"**Line:** {error.lineno}\n\n"
                "Check the indicated line and look for:\n\n"
                "- Missing `:`\n"
                "- Missing brackets\n"
                "- Incorrect indentation\n"
                "- Missing quotes\n"
                "- Misspelled Python keywords\n\n"
                "💡 **Detective Tip:** Start with the line mentioned in the error."
            ),
        }

    return {
        "success": True,
        "message": (
            "### ✅ Syntax Check Passed\n\n"
            "Your code has valid syntax. This does not guarantee it behaves "
            "correctly, so test it by running it."
        ),
    }


def _block(code):
    return f"{FENCE}python\n{code}\n{FENCE}"


ERRORS = {
    "nameerror": (
        "### 🔎 NameError\n\nPython cannot find the variable or function you used.\n\n"
        + _block("print(username)")
        + "\n\n**Fix:** Define the variable before using it."
    ),
    "typeerror": (
        "### 🔎 TypeError\n\nYou are mixing incompatible types.\n\n"
        + _block("age = 21\nprint('Age: ' + age)")
        + "\n\n**Fix:**\n\n"
        + _block("print('Age: ' + str(age))")
    ),
    "indexerror": (
        "### 🔎 IndexError\n\nYou are accessing a list position that does not exist.\n\n"
        + _block("numbers = [10, 20, 30]\nprint(numbers[5])")
        + "\n\nThe list only has indexes 0, 1 and 2."
    ),
    "keyerror": (
        "### 🔎 KeyError\n\nYou are accessing a dictionary key that doesn't exist.\n\n"
        + _block("player = {'name': 'Virat'}\nprint(player['age'])")
        + "\n\n**Fix:** use `.get()`:\n\n"
        + _block("print(player.get('age'))")
    ),
}

DEFAULT_ERROR = (
    "### 🔎 Error Detective\n\n"
    "Paste the complete Python error message and I'll try to explain it."
)


def explain_common_error(error_text):
    error_text = error_text.lower()
    for name, explanation in ERRORS.items():
        if name in error_text:
            return explanation
    return DEFAULT_ERROR