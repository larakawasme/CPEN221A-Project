import sqlite3
from flask import g

DB_NAME = "pedalprep.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_NAME)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def initialize_tables():
    con = sqlite3.connect(DB_NAME)
    cursor = con.cursor()
    # Create bike table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS bike_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bike_type TEXT NOT NULL,
            brand TEXT NOT NULL,
            model TEXT,
            year TEXT
        )
        """
    )

    # Create maintenance table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS maintenance_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT UNIQUE NOT NULL,
            last_completed TEXT,
            notes TEXT,
            interval_days INTEGER DEFAULT 30 -- default reminder interval
        )
        """
    )

    # Checklist table: the subset of maintenance tasks selected for the pre-ride checklist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS checklist_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        maintenance_id INTEGER NOT NULL UNIQUE,
        FOREIGN KEY(maintenance_id) REFERENCES maintenance_tasks(id)
            )
        """
    )

    # Current checklist: gets cleared for each checklist session and overwritten
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS checklist_session (
        checklist_task_id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT 0,
        FOREIGN KEY(checklist_task_id) REFERENCES checklist_tasks(id)
            )
        """
    )
    con.commit()
    con.close()
