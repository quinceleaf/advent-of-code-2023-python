import re

number_pattern = r"([\d]{1,4})"
number_block = re.compile(number_pattern)

symbol_pattern = r"[^\d.]"
symbol_block = re.compile(symbol_pattern)

INPUT_FILE = "./input.txt"
# INPUT_FILE = "./sample_input.txt"


def calculate_adjacent_points(*, points: list, matrix_dimensions: tuple) -> list:
    adjacent_points = []
    max_x_value = matrix_dimensions[0]
    max_y_value = matrix_dimensions[1]

    for point in points:
        x = point[0]
        y = point[1]

        # Horizontal
        adjacent_points.append((x - 1, y))
        adjacent_points.append((x + 1, y))

        # Vertical
        adjacent_points.append((x, y - 1))
        adjacent_points.append((x, y + 1))

        # Diagonal
        adjacent_points.append((x - 1, y - 1))
        adjacent_points.append((x - 1, y + 1))
        adjacent_points.append((x + 1, y - 1))
        adjacent_points.append((x + 1, y + 1))

    return [
        point
        for point in adjacent_points
        if all(
            [
                point[0] >= 1,
                point[0] <= max_x_value,
                point[1] >= 1,
                point[1] <= max_y_value,
                point not in points,
            ]
        )
    ]



def get_part_candidates(*, matrix: list) -> list:
    part_candidate_list = []

    for idx, line_str in enumerate(matrix, 1):
        matches = [
            (match.group(), match.span()) for match in number_block.finditer(line_str)
        ]
        if len(matches) == 0:
            continue

        for match in matches:
            part_number = match[0]
            span = match[1]

            points = []
            for column in range(span[0], span[1]):
                points.append((idx, column + 1))

            adjacent_points = calculate_adjacent_points(
                points=points, matrix_dimensions=(len(matrix), len(line_str))
            )

            part_candidate_list.append({
                "part_number": part_number,
                "points": set(points),
                "adjacent_points": set(adjacent_points),
            })

    return part_candidate_list


def get_symbol_candidates(*, matrix: list) -> dict:
    symbol_candidate_dict = {}

    for idx, line_str in enumerate(matrix, 1):
        matches = [
            (match.group(), match.span()) for match in symbol_block.finditer(line_str)
        ]
        if len(matches) == 0:
            continue

        for match in matches:
            symbol = match[0]
            span = match[1]

            points = []
            for column in range(span[0], span[1]):
                points.append((idx, column + 1))

            existing_symbol_locations = symbol_candidate_dict.get(symbol, [])
            symbol_candidate_dict[symbol] = points + existing_symbol_locations

    return symbol_candidate_dict


def load_matrix(*, file_path: str) -> list:
    with open(file_path, "r") as f:
        matrix = [line.strip() for line in f.readlines()]

    max_columns = max([len(line) for line in matrix])
    print(f"{max_columns} x {len(matrix)} matrix loaded...\n")
    return matrix


parts_schematic_matrix = load_matrix(file_path=INPUT_FILE)

valid_part_candidates = get_part_candidates(matrix=parts_schematic_matrix)

symbol_candidates = get_symbol_candidates(matrix=parts_schematic_matrix)

symbol_point_set = set([value for values in symbol_candidates.values() for value in values])

valid_part_numbers = []
for part in valid_part_candidates:
    part_number = part["part_number"]
    part_adjacent_points_set = part["adjacent_points"]

    if len(part_adjacent_points_set.intersection(symbol_point_set)) == 0:
        continue

    valid_part_numbers.append(part_number)

sum_of_all_part_numbers = sum([int(part_number) for part_number in valid_part_numbers])
print(f"Sum of part numbers: {sum_of_all_part_numbers}")
