import json

def load_teams():
    with open('data/teams.json', 'r') as file:
        return json.load(file)

def get_teams_by_stars(stars):
    #function to filter teams by stars using list comprehension
    teams = load_teams()
    return [t for t in teams if t['stars'] == stars] #list comprehension over for loop

# print(get_teams_by_stars(4.5))  # for testing purposes

def get_team_by_league(league_name):
    teams = load_teams()
    return [t for t in teams if t['league'] == league_name] 

# print (get_team_by_league('Premier League')) - for testing purposes

def get_available_teams(stars, exclude_teams=None, league=None):
    teams = get_teams_by_stars(stars)
    if league:
        teams = [t for t in teams if t['league'] == league]
    if exclude_teams:
        exclude_names = [t['name'] for t in exclude_teams]
        teams = [t for t in teams if t['name'] not in exclude_names]
    return teams

# print(get_available_teams(4.5, league='Bundesliga'))  # for testing purposes

