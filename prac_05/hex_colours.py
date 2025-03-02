COLOR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

print("Available colors and their codes:")
for name, code in COLOR_CODES.items():
    print(f"{name:20} {code}")

color_name = input("Enter a color name (or blank to quit): ").strip().lower()
while color_name != "":
    try:
        print(f"The hex code for {color_name} is {COLOR_CODES[color_name]}")
    except KeyError:
        print(f"Invalid color name: {color_name}")
    color_name = input("Enter a color name (or blank to quit): ").strip().lower()
