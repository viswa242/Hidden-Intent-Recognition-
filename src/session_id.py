import sqlite3
import json
from pathlib import Path

DB_PATH = Path("Conversation_session.db")

class SessionStore:
    def __init__(self):
        self._initialize_db()
    
    def _initialize_db(self):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           CREATE TABLE  IF NOT EXISTS sessions (
                           session_id TEXT PRIMARY KEY,
                           history TEXT,
                           score_history TEXT,
                           total_score REAL)
                           """)
            conn.commit()

    def save_session(self, session_id, history, score_history, total_score):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO sessions
                (session_id, history, score_history, total_score)
                VALUES (?,?,?,?)
                """,(
                session_id,
                json.dumps(history),
                json.dumps(score_history),
                total_score
            ))
            conn.commit()
            
    def load_session(self, session_id):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT history, score_history, total_score
                FROM sessions
                WHERE session_id = ?
            """, (session_id,))
            row = cursor.fetchone()

            if row:
                return {
                    "history": json.loads(row[0]),
                    "score_history": json.loads(row[1]),
                    "total_score": row[2]
                }

        return None