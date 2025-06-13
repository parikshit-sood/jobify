import sqlite3
import os


def create_database(db_path="../db/jobs.db"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    if os.path.exists(db_path):
        print(f"Database already exists at {db_path}. No action taken.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open("../db/schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("SUCCESS: Database is ready.")


if __name__ == "__main__":
    create_database()
