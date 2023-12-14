import re

# Summation of 100
GAMES_SUM = 5050

# Part 1 color threshold
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Returns the id of the games that are impossible, otherwise 0
def get_game_id_if_impossible(line):
    # Get the current game id
    current_id = int(re.findall(r'Game (\d+):', line)[0])
    line_sum = 0
    
    # Split into subgames
    subgames = line.split(";")

    # Go through each subline and get all the numbers for impossible games
    for subline in subgames:
        # Get all numbers from different colors
        red_cubes = re.findall(r'(?:^|,|\s)(\d+)(?=\s*red)', subline)
        green_cubes = re.findall(r'(?:^|,|\s)(\d+)(?=\s*green)', subline)
        blue_cubes = re.findall(r'(?:^|,|\s)(\d+)(?=\s*blue)', subline)

        # Check if any color passed the threshold, if true get the current id
        # and break
        if red_cubes:
            if int(red_cubes[0]) > MAX_RED:
                line_sum = current_id
                break

        if green_cubes:
            if int(green_cubes[0]) > MAX_GREEN:
                line_sum = current_id
                break

        if blue_cubes:
            if int(blue_cubes[0]) > MAX_BLUE:
                line_sum = current_id
                break

    return line_sum

# Get each minimum number of color and return the multiplication between each
# one of them
def get_min_sube_pow_sum(line):
    # Get all the values from all colors and convert them into int
    min_red = [int(x) for x in re.findall(r'(?:^|,|\s)(\d+)(?=\s*red)', line)]
    min_green = [int(x) for x in re.findall(r'(?:^|,|\s)(\d+)(?=\s*green)', line)]
    min_blue = [int(x) for x in re.findall(r'(?:^|,|\s)(\d+)(?=\s*blue)', line)]

    # Return the multiplication of all color's max amount
    return max(min_red) * max(min_green) * max(min_blue)

if __name__ == "__main__":
    total_id_sum = 0
    total_pow_sum = 0

    # Analyze each line and do each part separately
    for line in open("input.txt", "r"):
        total_id_sum += get_game_id_if_impossible(line)
        total_pow_sum += get_min_sube_pow_sum(line)

    print("Part 1:", GAMES_SUM - total_id_sum)
    print("Part 2:", total_pow_sum)