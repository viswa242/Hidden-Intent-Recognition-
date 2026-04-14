import sqlite3
import uuid
import json
from datetime import datetime

DB_PATH = "Conversation_sessions.db"

class SessionManager:
    def __init__(self, session_id=None):
        # self.conn = sqlite3.connect(DB_PATH)
        # self.cursor = self.conn.cursor()
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        
        self._create_table()
        self.session_id = session_id or self._create_session()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT UNIQUE,
            conversation TEXT,
            created_at TIMESTAMP
            )
        """)
        self.conn.commit()

    
    
    def _create_session(self):
        session_id = str(uuid.uuid4())
        self.cursor.execute(
            "INSERT INTO sessions (session_id, conversation, created_at) VALUES (?, ?, ?)",
            (session_id, json.dumps([]), datetime.now())
        )
        self.conn.commit()
        return session_id

    def load_conversation(self):
        self.cursor.execute(
            "SELECT conversation FROM sessions WHERE session_id = ?",
            (self.session_id,)
        )
        row = self.cursor.fetchone()
        return json.loads(row[0]) if row else []

    def save_conversation(self, conversation):
        self.cursor.execute(
            "UPDATE sessions SET conversation = ? WHERE session_id = ?",
            (json.dumps(conversation), self.session_id)
        )
        self.conn.commit()
