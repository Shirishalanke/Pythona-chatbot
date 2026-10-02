"""Levels and ranks."""


def calculate_level(xp):
    return (xp // 100) + 1


def calculate_level_progress(xp):
    return (xp % 100) / 100


def get_rank(level):
    if level >= 10:
        return "🐍 Python Master"
    if level >= 7:
        return "🔥 Python Expert"
    if level >= 5:
        return "⚡ Python Developer"
    if level >= 3:
        return "🚀 Python Learner"
    return "🌱 Python Beginner"