# INPUT_FILE = "./sample_input.txt"
INPUT_FILE = "./input.txt"


spelled_numbers_to_digits_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def load_input(*, file_path: str) -> list:
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def scan_for_calibration_value(*, line_str: str) -> int:
    leftmost = None
    rightmost = None

    print(f"\n\nLINE STRING: {line_str}")

    spelled_number_tuple = tuple(spelled_numbers_to_digits_dict.keys())

    # Scan left-to-right
    print("\nScanning left-to-right...")
    character = 0
    while leftmost is None:
        print(
            f"... evaluating (L-R), single-character {line_str[character]}, substring {line_str[:character+1]}"
        )

        if line_str[character].isdigit():
            leftmost = line_str[character]

        elif line_str[: character + 1].endswith(spelled_number_tuple):
            found_spelled_number = [
                spelled_number
                for spelled_number in spelled_number_tuple
                if (spelled_number in line_str[: character + 1])
            ][0]

            integer_number = spelled_numbers_to_digits_dict[found_spelled_number]
            leftmost = integer_number

        character += 1

    # Right-to-left scan
    print("\nScanning right-to-left...")
    character = -1
    while rightmost is None:
        print(
            f"... evaluating (R-L), single-character {line_str[character]}, substring {line_str[character:]}"
        )

        if line_str[character].isdigit():
            rightmost = line_str[character]

        elif line_str[character:].startswith(spelled_number_tuple):
            found_spelled_number = [
                spelled_number
                for spelled_number in spelled_number_tuple
                if (spelled_number in line_str[character:])
            ][0]

            integer_number = spelled_numbers_to_digits_dict[found_spelled_number]
            rightmost = integer_number

        character -= 1

    calibration_value = int(f"{leftmost}{rightmost}")
    print(f"\nLeftmost: {leftmost}, rightmost: {rightmost}, calibration value: {calibration_value}")
    return calibration_value


def sum_calibration_values(*, input_data: list) -> int:
    return sum(input_data)


calibration_document_list = load_input(file_path=INPUT_FILE)
print(f"{len(calibration_document_list)} lines loaded...")
# calibration_document_list = ["2tqbxgrrpmxqfglsqjkqthree6nhjvbxpflhr1eightwohr"]


calibration_value_list = [
    scan_for_calibration_value(line_str=calibration_document_line)
    for calibration_document_line in calibration_document_list
]
calibration_value_sum = sum_calibration_values(input_data=calibration_value_list)
print(f"\n\nCalibration value sum: {calibration_value_sum}")
