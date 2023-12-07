INPUT_FILE = "./input.txt"
# INPUT_FILE = "./sample_input.txt"


def load_input(*, file_path: str) -> list:
    with open(file_path, "r") as f:
       return [line.strip() for line in f.readlines()]
    

def evaluate_card(*, held_number_set: set, winning_number_set: set) -> int:
    winning_numbers_held_set = held_number_set.intersection(winning_number_set)
    number_of_winning_numbers = len(winning_numbers_held_set)
    return number_of_winning_numbers


def update_card_copies_dict(*, card_copies_dict: dict, current_card_number: int, quantity_of_current_card: int, winning_numbers_held: int) -> dict:
    for card_number in range(current_card_number + 1, current_card_number + winning_numbers_held + 1):
        card_copies_dict[card_number] = card_copies_dict.get(card_number, 0) + (1 * quantity_of_current_card)
    return card_copies_dict
    

card_list = load_input(file_path=INPUT_FILE)
print(f"{len(card_list)} cards loaded...")

card_copies_dict = {}

for card in card_list:
    # Determine card number
    card_number = int(card.split(":")[0].split()[1])
    print(f"\n\nCard number: {card_number}")

    # Update number of copies of current card
    card_copies_dict[card_number] = card_copies_dict.get(card_number, 0) + 1
    quantity_of_current_card = card_copies_dict[card_number]
    print(f"Quantity of current card: {quantity_of_current_card}")

    # Determine winning and held numbers
    winning_number_set = {int(value) for value in card.split("|")[0].split(":")[1].split()}
    held_number_set = {int(value) for value in card.split("|")[1].split()}

    number_of_winning_numbers = evaluate_card(held_number_set=held_number_set, winning_number_set=winning_number_set)
    print(f"Number of winning numbers: {number_of_winning_numbers}")
    
    if number_of_winning_numbers > 0:
        card_copies_dict = update_card_copies_dict(card_copies_dict=card_copies_dict, current_card_number=card_number, quantity_of_current_card=quantity_of_current_card, winning_numbers_held=number_of_winning_numbers)

    for card, copies in card_copies_dict.items():
        print(f"Card {card}: {copies} copies")

card_quantities = list(card_copies_dict.values())
total_cards = sum(card_quantities)
print(f"\nTotal cards: {total_cards}")