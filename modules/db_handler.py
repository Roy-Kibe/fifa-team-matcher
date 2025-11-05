import sqlite3

DB_PATH = 'data/fifa_teams.db'

def get_connection():
    """Create a DB connection"""
    return sqlite3.connection(DB_PATH)

def get_all_teams():
    #Get all teams from the database
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM teams')
    rows = cursor.fetchall()

    teams = []
    for row in rows:
        teams.append({
            'id': row[0],
            'name': row[1],
            'league': row[2],
            'stars': row[3],
            'overall_rating': row[4],
            'country': row[5],
            'play_style': row[6]
        })

    conn.close()
    return teams

def get_teams_by_stars(star_rating):
    #Get teams filtered by star rating
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM teams WHERE stars=?', (star_rating,))
    rows = cursor.fetchall()

    teams = []
    for row in rows:
        teams.append({
            'id': row[0],
            'name': row[1],
            'league': row[2],
            'stars': row[3],
            'overall_rating': row[4],
            'country': row[5],
            'play_style': row[6]
        })

    conn.close()
    return teams

def get_teams_by_league(league_name):
    """Get teams filtered by league"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM teams WHERE league = ?', (league_name,))
    rows = cursor.fetchall()
    
    teams = []
    for row in rows:
        teams.append({
            'id': row[0],
            'name': row[1],
            'league': row[2],
            'stars': row[3],
            'overall_rating': row[4],
            'country': row[5],
            'play_style': row[6]
        })
    
    conn.close()
    return teams

def get_teams_by_id():
    #Get a specific team by its ID
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM teams WHERE id=?', (id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return {
            'id': row[0],
            'name': row[1],
            'league': row[2],
            'stars': row[3],
            'overall_rating': row[4],
            'country': row[5],
            'play_style': row[6]
        }
    else:
        return None 
