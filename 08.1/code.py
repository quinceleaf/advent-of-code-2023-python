INPUT_FILE = "./input.txt"
# INPUT_FILE = "./sample_input_1.txt"
# INPUT_FILE = "./sample_input_2.txt"


def load_input(*, file_path: str) -> dict:
    node_dict = {}

    with open(INPUT_FILE) as f:
        lines = f.readlines()

        for idx, line in enumerate(lines):
            if idx == 0:
                instruction_str = line.strip()
            elif idx == 1:
                continue
            else:
                line = line.strip()
                node = line.split("=")[0].strip()
                left = line.split("(")[1].split(",")[0].strip()
                right = line.split(",")[1].split(")")[0].strip()

                node_dict[node] = (left, right)

    return instruction_str, node_dict


instruction_str, node_dict = load_input(file_path=INPUT_FILE)
print(f"Instruction: {instruction_str}")
print(f"Node Dict: {node_dict}")

current_node = "AAA"
print(f"\nStarting at node: {current_node}\n")

instruction_idx = 0
step_counter = 0

seeking = True
while seeking:
    step_counter += 1
    entry_node = current_node
    node_choice_tuple = node_dict[current_node]
    instruction = instruction_str[instruction_idx]

    if instruction == "L":
        current_node = node_choice_tuple[0]
    elif instruction == "R":
        current_node = node_choice_tuple[1]

    print(
        f"(Step {step_counter}): Move {instruction} from {entry_node} to {current_node}"
    )

    if current_node == "ZZZ":
        print(f"\nFound ZZZ in {step_counter} steps")
        seeking = False
    else:
        instruction_idx += 1
        if instruction_idx >= len(instruction_str):
            instruction_idx = 0