import json

with open('data/teams.json', 'r') as file:
    teams = json.load(file)

print(f"Loaded {len(teams)} teams from data.json")

#Print first team
print("First team:", teams[0])

#Filter five star teams
five_star_teams = [team for team in teams if team.get('stars') == 5.0]
print(f"Found {len(five_star_teams)} five star teams")
for team in five_star_teams:
    print(team)