import random
from modules.team_loader import get_available_teams

def generate_opponent(player_team, same_league=False):
    """
    Generate a random opponent team.
    Args:
        player_team: ;Dictionary with team info
        same_league (bool): Whether to select an opponent from the same league.
    """

    star_rating = player_team['stars']
    league = player_team['league'] if same_league else None

    available = get_available_teams(
        stars=star_rating,
        exclude_teams=[player_team],
        league=league
    )
    if not available:
        return ValueError("No available teams found for the given criteria.")
    
    ## Randomly select an opponent from the available teams and using given criteria
    return random.choice(available)

def generate_matchup(num_player, star_rating, same_league=False):
    """
    Generate matchup for multiple players.
    Return: A list of team assignments.
    """
    from modules.team_loader import get_teams_by_stars
    all_teams = get_teams_by_stars(star_rating)

    # Check if enough teams are available
    if len(all_teams)<num_player:
        raise ValueError("Not enough teams available for {num_players} players with {star_rating} star teams.")
    
    selected = random.sample(all_teams, num_player) # Randomly select teams for players using .sample ensures no duplicates
    return selected