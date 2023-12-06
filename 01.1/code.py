INPUT_FILE = "./input.txt"

def load_input(*, file_path: str) -> list:
    with open(file_path, "r") as f:
       return [line.strip() for line in f.readlines()]
    
def calculate_calibration_value(*, line_str: str) -> int:
    left_idx = 0
    right_idx = (len(line_str) - 1) * -1

    # Scan left-to-right
    seeking = True
    character = 0
    while seeking:
        if line_str[character].isdigit():
            left_idx = character
            seeking = False
        character += 1

    # Right-to-left scan
    seeking = True
    character = -1
    while seeking:
        if line_str[character].isdigit():
            right_idx = character
            seeking = False
        character -= 1
    
    calibration_value = int(f"{line_str[left_idx]}{line_str[right_idx]}")
    print(f"Calibration value: {calibration_value}")
    return calibration_value


def sum_calibration_values(*, input_data: list) -> int:
    return sum(input_data)


calibration_document_list = load_input(file_path=INPUT_FILE)
print(f"{len(calibration_document_list)} lines loaded...")

calibration_value_list = [calculate_calibration_value(line_str=calibration_document_line) for calibration_document_line in calibration_document_list]
print(f"{len(calibration_value_list)} calibration values calculated...")

calibration_value_sum = sum_calibration_values(input_data=calibration_value_list)
print(f"Calibration value sum: {calibration_value_sum}")