import re

match_blue = re.compile(r"\d{1,3} blue")
match_green = re.compile(r"\d{1,3} green")
match_red = re.compile(r"\d{1,3} red")


# INPUT_FILE = "./input.txt"
INPUT_FILE = "./sample_input.txt"


constraint = {"red": 12, "green": 13, "blue": 14}


def load_input(*, file_path: str) -> list:
    with open(file_path, "r") as f:
       return [line.strip() for line in f.readlines()]
    
def check_if_possible(*, game_record: str, constraint: dict) -> bool:
    # Get key
    game_key = int(game_record.split(":")[0].split(" ")[1])

    # Check blue
    blue_values = [int(match.group(0).split(" ")[0]) for match in match_blue.finditer(game_record)]
    if max(blue_values) > constraint["blue"]:
        print(f"Game key {game_key} failed blue check")
        return False

    # Check green
    green_values = [int(match.group(0).split(" ")[0]) for match in match_green.finditer(game_record)]
    if max(green_values) > constraint["green"]:
        print(f"Game key {game_key} failed green check")
        return False

    # Check red
    red_values = [int(match.group(0).split(" ")[0]) for match in match_red.finditer(game_record)]
    if max(red_values) > constraint["red"]:
        print(f"Game key {game_key} failed red check")
        return False
    
    return True
    
game_record_list = load_input(file_path=INPUT_FILE)
print(f"{len(game_record_list)} lines loaded...")

possible_games_iterator = filter(lambda game_round: check_if_possible(game_record=game_round, constraint=constraint), game_record_list)
possible_games_list = list(possible_games_iterator)
print(f"{len(possible_games_list)} possible games found...")

keys_total = 0
for game_str in possible_games_list:
    game_key = int(game_str.split(":")[0].split(" ")[1])
    keys_total += game_key

print(f"Sum of possible game keys: {keys_total}")