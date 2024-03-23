def forecast (*args):
    some_dict = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for location, weather in args:
        if weather in some_dict:
            some_dict[weather].append(location)

    result = ""

    for weather, locations in some_dict.items():
        if locations:
            sorted_loco = sorted(locations)
            for loco in sorted_loco:
                result += f"{loco} - {weather}\n"
    return result

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
