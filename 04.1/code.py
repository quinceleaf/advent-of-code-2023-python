INPUT_FILE = "./input.txt"
# INPUT_FILE = "./sample_input.txt"


def load_input(*, file_path: str) -> list:
    with open(file_path, "r") as f:
       return [line.strip() for line in f.readlines()]
    
def evaluate_card(*, held_number_set: set, winning_number_set: set) -> int:
    winning_numbers_held_set = held_number_set.intersection(winning_number_set)
    number_of_winning_numbers = len(winning_numbers_held_set)

    if number_of_winning_numbers == 0:
        return 0
    else:
        point_value_of_card = 2**(number_of_winning_numbers - 1)
        return point_value_of_card
    
card_list = load_input(file_path=INPUT_FILE)
print(f"{len(card_list)} cards loaded...\n\n")

total_points = 0

for card in card_list:
    winning_number_set = {int(value) for value in card.split("|")[0].split(":")[1].split()}
    held_number_set = {int(value) for value in card.split("|")[1].split()}

    print(f"Winning numbers: {winning_number_set}")
    print(f"Held numbers: {held_number_set}")

    point_value_of_card = evaluate_card(held_number_set=held_number_set, winning_number_set=winning_number_set)
    total_points += point_value_of_card

    print(f"Point value of card: {point_value_of_card}\n\n")

print(f"\nTotal points: {total_points}")