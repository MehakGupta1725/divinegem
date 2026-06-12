import sqlite3
from datetime import datetime

DB_NAME = "consultations.db"


def get_connection():
    """Create and return a database connection."""
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():
    """Create required tables if they don't exist."""
    conn = get_connection()
    cursor = conn.cursor()

    # Recommendations table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            zodiac TEXT NOT NULL,
            concern TEXT NOT NULL,
            gemstone TEXT NOT NULL,
            recommendation_date TEXT NOT NULL
        )
    """)

    # Consultations table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            preferred_date TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_recommendation(name, zodiac, concern, gemstone):
    """Save gemstone recommendation."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO recommendations (
            name,
            zodiac,
            concern,
            gemstone,
            recommendation_date
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        zodiac,
        concern,
        gemstone,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def save_consultation(name, phone, preferred_date):
    """Save consultation request."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO consultations (
            name,
            phone,
            preferred_date,
            created_at
        )
        VALUES (?, ?, ?, ?)
    """, (
        name,
        phone,
        preferred_date,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_recommendations():
    """Fetch all recommendations."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM recommendations
        ORDER BY recommendation_date DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_consultations():
    """Fetch all consultation requests."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM consultations
        ORDER BY created_at DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data