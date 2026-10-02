"""SQLite storage. The DB lives next to this file, so the project is portable."""
import sqlite3
from contextlib import closing
from datetime import datetime
from pathlib import Path

DB_FOLDER = Path(__file__).resolve().parent / "data"
DB_PATH = DB_FOLDER / "pythona.db"


def get_connection():
    DB_FOLDER.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def _now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _run(sql, params=()):
    with closing(get_connection()) as conn, conn:
        conn.execute(sql, params)


def _fetch(sql, params=()):
    with closing(get_connection()) as conn:
        return conn.execute(sql, params).fetchall()


def init_database():
    with closing(get_connection()) as conn, conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT NOT NULL,
                bot_response TEXT NOT NULL,
                topic TEXT,
                created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS learning_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT UNIQUE NOT NULL,
                questions_asked INTEGER DEFAULT 0,
                correct_answers INTEGER DEFAULT 0,
                xp INTEGER DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS knowledge_base (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                topic TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
        """)


def save_chat(user_message, bot_response, topic):
    _run(
        "INSERT INTO chat_history (user_message, bot_response, topic, created_at) "
        "VALUES (?, ?, ?, ?)",
        (user_message, bot_response, topic, _now()),
    )


def get_chat_history():
    return _fetch(
        "SELECT user_message, bot_response, topic, created_at "
        "FROM chat_history ORDER BY id DESC"
    )


def update_learning_progress(topic, correct=False):
    xp = 20 if correct else 5
    _run(
        """
        INSERT INTO learning_progress (topic, questions_asked, correct_answers, xp)
        VALUES (?, 1, ?, ?)
        ON CONFLICT(topic) DO UPDATE SET
            questions_asked = questions_asked + 1,
            correct_answers = correct_answers + excluded.correct_answers,
            xp = xp + excluded.xp
        """,
        (topic, int(correct), xp),
    )


def get_learning_progress():
    return _fetch(
        "SELECT topic, questions_asked, correct_answers, xp "
        "FROM learning_progress ORDER BY xp DESC"
    )


def add_knowledge(question, answer, topic):
    _run(
        "INSERT INTO knowledge_base (question, answer, topic, created_at) "
        "VALUES (?, ?, ?, ?)",
        (question, answer, topic, _now()),
    )


def get_knowledge():
    return _fetch(
        "SELECT id, question, answer, topic, created_at "
        "FROM knowledge_base ORDER BY id DESC"
    )