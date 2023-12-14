import re

replacement = [
    ("one", "o1e"),
    ("two", "t2o"),
    ("three", "t3e"),
    ("four", "f4r"),
    ("five", "f5e"),
    ("six", "s6x"),
    ("seven", "s7n"),
    ("eight", "e8h"),
    ("nine", "n9e"),
    ("zero", "z0o")
]

# Get digits from line and call sum_side_nums()
def get_txt_sum(line):
     # Find all digits in the line and put them in a list.
    reg = re.findall("\\d", line)
    # Combine the first and last number or the only number twice (if applicable)
    # and sum it for the 1st challenge.
    return sum_side_nums(reg)

# Combines the first and last number or the only number twice (if applicable).
def sum_side_nums(line):
    sum = 0

    # Check for length to avoid making operations in empty lists.
    if len(line) > 0:
        # Get the first digit.
        sum = int(line[0])

        # If there are more than 2 digits, combine them together.
        # Ex: [7] -> 77
        if len(line) > 1:
            sum = (sum * 10) + int(line[-1])
        # If there's only one digit, repeat them twice.
        # Ex: [7] -> 77
        else:
            sum += (sum * 10)

    return sum

if __name__ == "__main__":
    lines = []
    total_sum_1 = 0
    total_sum_2 = 0

    f = open("input.txt", "r")
    
    # Go through each line of the .txt.
    for line in f:
        total_sum_1 += get_txt_sum(line)

        # Replace every text number to their digit equivalent.
        for (old_word, new_word) in replacement:
                line = line.replace(old_word, new_word)

        total_sum_2 += get_txt_sum(line)

    print("Part 1:", total_sum_1)
    print("Part 2:", total_sum_2)