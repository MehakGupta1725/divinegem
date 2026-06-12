import sqlite3
import hashlib
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
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
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

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
""")

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

def hash_password(password):
    """Hash password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(username, password, role="user"):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (
            username,
            hash_password(password),
            role
        ))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


def authenticate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role
        FROM users
        WHERE username = ?
        AND password = ?
    """, (
        username,
        hash_password(password)
    ))

    user = cursor.fetchone()

    conn.close()

    return user


def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, role
        FROM users
    """)

    users = cursor.fetchall()

    conn.close()

    return users

def initialize_admin():
    create_user(
        "admin",
        "admin123",
        "admin"
    )