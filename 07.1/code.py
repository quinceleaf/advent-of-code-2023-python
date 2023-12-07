import itertools

INPUT_FILE = "./input.txt"
# INPUT_FILE = "./sample_input.txt"


HAND_TYPES = [
    "HIGH_CARD",
    "ONE_PAIR",
    "TWO_PAIRS",
    "THREE_OF_KIND",
    "FULL_HOUSE",
    "FOUR_OF_KIND",
    "FIVE_OF_KIND",
]  # ascending order of value


HAND_TYPE_MAP = {
    11111: "HIGH_CARD",
    2111: "ONE_PAIR",
    221: "TWO_PAIRS",
    311: "THREE_OF_KIND",
    32: "FULL_HOUSE",
    41: "FOUR_OF_KIND",
    5: "FIVE_OF_KIND",
}

CARD_VALUES = [
    "A",
    "K",
    "Q",
    "J",
    "T",
    "9",
    "8",
    "7",
    "6",
    "5",
    "4",
    "3",
    "2",
]  # descending order of value

CARD_VALUES_MAP = {
    "A": "12",
    "K": "11",
    "Q": "10",
    "J": "09",
    "T": "08",
    "9": "07",
    "8": "06",
    "7": "05",
    "6": "04",
    "5": "03",
    "4": "02",
    "3": "01",
    "2": "00",
}


def load_input(*, file_path: str) -> list:
    hands_list = []
    with open(file_path, "r") as f:
        lines = f.readlines()

        for line in lines:
            hand = line.split()[0].strip()
            bid = int(line.split()[1].strip())

            hands_list.append(
                {
                    "hand": hand,
                    "bid": bid,
                    "hand_strength": 0,
                    "intermediate_rank": 0,
                    "rank": 0,
                }
            )

    return hands_list


def transform_to_lexographical_order(*, hand: str) -> str:
    return "".join([CARD_VALUES_MAP[card] for card in hand])


def determine_hand_type(*, hand: str) -> str:
    reordered_hand = "".join(sorted(hand, key=lambda x: CARD_VALUES.index(x)))
    grouped_hand = [len(list(g)) for k, g in itertools.groupby(reordered_hand)]
    grouped_hand.sort()
    grouped_hand.reverse()
    group_hand_str = "".join([str(i) for i in grouped_hand])

    return HAND_TYPE_MAP[int(group_hand_str)]


hands_dict = {}
hands_list = load_input(file_path=INPUT_FILE)
for hand in hands_list:
    hand_type = determine_hand_type(hand=hand["hand"])
    hand["hand_strength"] = HAND_TYPES.index(hand_type)
    hand["hand_type"] = hand_type
    hands_dict[hand["hand"]] = {
        "hand_strength": hand["hand_strength"],
        "bid": hand["bid"],
        "intermediate_rank": "",
        "rank": 0,
        "hand_type": hand["hand_type"],
    }

# Sort list-of-dictionaries by multiple keys
hands_list.sort(key=lambda x: (x["hand_strength"], x["rank"]), reverse=True)

for strength in range(0, len(HAND_TYPES)):
    hands_subset_by_strength = [
        hand["hand"] for hand in hands_list if hand["hand_strength"] == strength
    ]
    hands_subset_by_strength.sort()
    hands_subset_by_strength.reverse()

    for hand in hands_subset_by_strength:
        hand_dict = hands_dict[hand]
        intermediate_rank = transform_to_lexographical_order(hand=hand)
        hand_dict["intermediate_rank"] = intermediate_rank
        hands_dict[hand] = hand_dict

# Sort hands_dict by strength and intermediate_rank, then assign rank
ranked_hands_list = sorted(
    hands_dict.items(),
    key=lambda x: (x[1]["hand_strength"], x[1]["intermediate_rank"]),
    reverse=False,
)
for idx, hand in enumerate(ranked_hands_list, 1):
    hand_dict = hands_dict[hand[0]]
    hand_dict["rank"] = idx
    hands_dict[hand[0]] = hand_dict

# Calculate winnings by bid and rank and aggregate
total_winnings = 0
for key, value in hands_dict.items():
    winnings = hands_dict[key]["bid"] * hands_dict[key]["rank"]
    hands_dict[key]["winnings"] = winnings
    total_winnings += winnings

print(f"Total winnings: {total_winnings}")
