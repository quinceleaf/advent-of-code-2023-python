import functools

INPUT_FILE = "./input.txt"
# INPUT_FILE = "./sample_input.txt"

def load_input(*, file_path: str) -> list:
    with open(file_path, "r") as f:
        lines = f.readlines()
        times_list = [int(time.strip()) for time in lines[0].split(":")[1].split()]
        distance_list = [int(time.strip()) for time in lines[1].split(":")[1].split()]
        return dict(zip(times_list, distance_list))


def evaluate_race_options(*, hold_time: int, time_allowed: int, distance_required: int) -> bool:
    speed = hold_time
    distance_travelled = (speed * (time_allowed - hold_time))

    return True if distance_travelled > distance_required else False

time_allowed_vs_record_distanc_dict = load_input(file_path=INPUT_FILE)

number_of_options_all_races = []

for time_allowed, distance_required in time_allowed_vs_record_distanc_dict.items():
    possible_options = []

    for hold_time in range(0, time_allowed):
        if evaluate_race_options(hold_time=hold_time, time_allowed=time_allowed, distance_required=distance_required):
            possible_options.append({"time_allowed": time_allowed, "distance_required": distance_required, "hold_time": hold_time})

    number_of_options_all_races.append(len(possible_options))

product_of_valid_options = functools.reduce(lambda x, y: x * y, number_of_options_all_races)
print(f"Product of valid options: {product_of_valid_options}")
