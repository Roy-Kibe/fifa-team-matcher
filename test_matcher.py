from modules.matcher import generate_matchup, generate_opponent
from modules.team_loader import load_teams, get_teams_by_stars

teams = load_teams()
print(f"Loaded {len(teams)} teams\n")

five_star = get_teams_by_stars(5.0)
print(f"Found {len(five_star)} five-star teams")
for team in five_star[:5]: # print first 5 five-star teams
    print(f" - {team['name']}")
print()

player1_team = five_star[0]
print(f"Player 1 chose {player1_team['name']} from {player1_team['league']}")

#test for different league opponent
opponent = generate_opponent(player1_team, same_league=False)
print(f"Generated opponent for Player 2 (from any other league) is {opponent['name']} from {opponent['league']}\n")

#test for same league opponent
opponent_same_league = generate_opponent(player1_team, same_league=True)
print(f"Player 1 chose {player1_team['name']} from {player1_team['league']}")
print(f"Generated opponent for Player 2 (from same league) is {opponent_same_league['name']} from {opponent_same_league['league']}\n")


matchup = generate_matchup(num_player=4, star_rating=5.0)
print("Generated matchup for 4 players with 5-star teams:")
#printing the choosen teams
for i, team in enumerate(matchup, start=1):
    print(f" Player {i}: {team['name']}")
