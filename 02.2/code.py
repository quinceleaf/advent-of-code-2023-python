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
    
    
def calculate_power_of_minimum_set(*, game_record: str) -> int:
    # Check blue
    blue_values = [int(match.group(0).split(" ")[0]) for match in match_blue.finditer(game_record)]
    minimum_required_blue_cubes = max(blue_values)

    # Check green
    green_values = [int(match.group(0).split(" ")[0]) for match in match_green.finditer(game_record)]
    minimum_required_green_cubes = max(green_values)

    # Check red
    red_values = [int(match.group(0).split(" ")[0]) for match in match_red.finditer(game_record)]
    minimum_required_red_cubes = max(red_values)

    power_of_set = minimum_required_blue_cubes * minimum_required_green_cubes * minimum_required_red_cubes
    return power_of_set

    
game_record_list = load_input(file_path=INPUT_FILE)
print(f"{len(game_record_list)} lines loaded...")

game_powers_list = list(map(lambda game_record: calculate_power_of_minimum_set(game_record=game_record), game_record_list))
print(f"Game powers list: {game_powers_list}")

sum_of_all_powers = sum(game_powers_list)
print(f"Sum of game powers: {sum_of_all_powers}")