# Written by Ovi
# Date: 2025-03-12
# Summary: This script processes JSON roster data into an SQLite database and retrieves assignment-required results.

import json
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Setup: Drop existing tables and create fresh ones
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Load the JSON data
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

with open(fname) as f:
    json_data = json.load(f)

# Insert data into tables
for entry in json_data:
    name, title, role = entry

    # Insert or ignore into User table
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES (?)''', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore into Course table
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES (?)''', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert into Member table
    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES (?, ?, ?)''',
        (user_id, course_id, role))

# Commit changes
conn.commit()

# Execute the first query
cur.execute('''
SELECT User.name, Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;
''')

print("\nQuery Output (First Query):")
for row in cur.fetchall():
    print(row)

# Execute the second query
cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;
''')

print("\nSecret Code:")
print(cur.fetchone()[0])

# Close the connection
cur.close()