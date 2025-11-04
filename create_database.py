import sqlite3
import json

# Connecting to the database (or creating it if it doesn't exist)
conn = sqlite3.connect('data/fifa_teams.db')
cursor = conn.cursor() # cursor object to execute SQL commands

#Create a table called teams with the following columns:
cursor.execute('''
CREATE TABLE IF NOT EXISTS teams (
               id INTEGER PRIMARY KEY, AUTO_INCREMENT,
               name TEXT NOT NULL UNIQUE,
               league TEXT NOT NULL,
               stars REAL NOT NULL,
               overall_rating INTEGER,
               country TEXT,
               play_style TEXT
               )
               ''')

# Load team data from a JSON file
with open('data/teams.json', 'r') as file:
    teams =json.load(file)

# Insert team data into the database
for team in teams:
    try:
        cursor.execute('''
        INSERT INTO teams (name, league, stars, overall_rating, country, play_style)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            team['name'],
            team['league'],
            team['stars'],
            team.get('overall_rating', 80), # default to 80
            team['country'],
            team.get('play_style', 'balanced') # default to balanced
        ))
    except sqlite3.IntegrityError:
        print(f"Skipping duplicate: {team['name']}")


# Save changes to the database and close the connection
conn.commit()
print(f" Database created with {len(teams)} teams.")

# Verify insertion works by counting the number of teams in the database
cursor.execute('SELECT COUNT (*) FROM teams')
count = cursor.fetchone()[0]
print(f" Total teams in database: {count}")

conn.close()