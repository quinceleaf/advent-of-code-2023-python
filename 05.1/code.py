INPUT_FILE = "./input.txt"
# INPUT_FILE = "./sample_input.txt"


def import_map(*, file_path: str, key_str: int) -> list:
    map_line_dict = []

    with open(file_path, "r") as f:
        map_lines = f.read().split("\n\n")

    map_to_extract = [line for line in map_lines if key_str in line][0]

    for idx, line in enumerate(map_to_extract.split("\n")):
        if idx > 0:
            map_line_dict.append(
                {
                    "destination_range_start": int(line.split()[0]),
                    "source_range_start": int(line.split()[1]),
                    "range_length": int(line.split()[2]),
                }
            )

    return map_line_dict


def expand_map_for_individual_source(*, map_list: list, source: int) -> int:
    for map in map_list:
        source_range = range(
            map["source_range_start"], map["source_range_start"] + map["range_length"]
        )
        if source in source_range:
            return map["destination_range_start"] + (source - map["source_range_start"])

    return source


def trace_path_from_seed_to_location(
    *,
    seed: int,
    seed_to_soil_map_list: list,
    soil_to_fertilizer_map_list: list,
    fertilizer_to_water_map_list: list,
    water_to_light_map_list: list,
    light_to_temperature_map_list: list,
    temperature_to_humidity_map_list: list,
    humidity_to_location_map_list: list,
) -> int:
    soil = expand_map_for_individual_source(map_list=seed_to_soil_map_list, source=seed)
    fertilizer = expand_map_for_individual_source(
        map_list=soil_to_fertilizer_map_list, source=soil
    )
    water = expand_map_for_individual_source(
        map_list=fertilizer_to_water_map_list, source=fertilizer
    )
    light = expand_map_for_individual_source(
        map_list=water_to_light_map_list, source=water
    )
    temperature = expand_map_for_individual_source(
        map_list=light_to_temperature_map_list, source=light
    )
    humidity = expand_map_for_individual_source(
        map_list=temperature_to_humidity_map_list, source=temperature
    )
    location = expand_map_for_individual_source(
        map_list=humidity_to_location_map_list, source=humidity
    )

    return location


# Import seed list
with open(INPUT_FILE, "r") as f:
    lines = f.readlines()
    for idx, line in enumerate(lines, 1):
        if idx == 2:
            seed_list = line.strip().split()

# Import maps
seed_to_soil_map_list = import_map(file_path=INPUT_FILE, key_str="seed-to-soil")
soil_to_fertilizer_map_list = import_map(
    file_path=INPUT_FILE, key_str="soil-to-fertilizer"
)
fertilizer_to_water_map_list = import_map(
    file_path=INPUT_FILE, key_str="fertilizer-to-water"
)
water_to_light_map_list = import_map(file_path=INPUT_FILE, key_str="water-to-light")
light_to_temperature_map_list = import_map(
    file_path=INPUT_FILE, key_str="light-to-temperature"
)
temperature_to_humidity_map_list = import_map(
    file_path=INPUT_FILE, key_str="temperature-to-humidity"
)
humidity_to_location_map_list = import_map(
    file_path=INPUT_FILE, key_str="humidity-to-location"
)


# Trace path
seed_locations = []

for seed in seed_list:
    location = trace_path_from_seed_to_location(
        seed=int(seed),
        seed_to_soil_map_list=seed_to_soil_map_list,
        soil_to_fertilizer_map_list=soil_to_fertilizer_map_list,
        fertilizer_to_water_map_list=fertilizer_to_water_map_list,
        water_to_light_map_list=water_to_light_map_list,
        light_to_temperature_map_list=light_to_temperature_map_list,
        temperature_to_humidity_map_list=temperature_to_humidity_map_list,
        humidity_to_location_map_list=humidity_to_location_map_list,
    )
    seed_locations.append(location)

lowest_location = min(seed_locations)
print(f"\n\nLowest location: {lowest_location}")