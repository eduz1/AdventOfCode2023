import re

# Find the box surrounding the item
def box_finder(sign, row):
    start = sign[1]
    end = sign[2]
    above = []
    same = []
    below = []

    for x in range(start - 1, end + 1):
        # Skip any left coordinates if any space is -1
        if x >= 0:
            # Get coordinates in the row above
            # Skip if current row is 0 
            if row > 0:
                above.append([x, row - 1])
            
            # Get coordinates in the row below
            below.append([x, row + 1])
            
            # Get adjacent coordinates in the same row
            if (x == start - 1) or (x == end):
                same.append([x, row])

    return above, same, below

if __name__ == "__main__":
    total_sum = 0
    pow_total_sum = 0
    numbers = []
    symbol_coords = []
    number_boxes = []
    star_coords = []
    stars = []

    # Go through the file
    with open("input.txt") as f:
        for i, line in enumerate(f, 0):
            # Remove all the "\n"
            line = line[:-1]
            # Get all the characters that are not "." or numbersi
            re_symbols = re.compile(r'[^\d.]+')
            # Get the symbols and their coordinates
            symbol_matches = [(match.group(), match.start(), match.end()) for match in re_symbols.finditer(line)]

            # Append the every symbol coordinates
            for item in symbol_matches:
                symbol_coords.append([item[1], i])

            # Now get all the numbers and their coordinates
            re_numbers = re.compile(r"(\d+)")
            number_matches = [(match.group(), match.start(), match.end()) for match in re_numbers.finditer(line)]
            
            # For each number, get all the coordinates that surround that number
            for item in number_matches:
                numbers.append(item[0])
                number_boxes.append(box_finder(item, i))

            # Get all star coordinates in the text
            re_star = re.compile(r'\*')
            star_matches = [(match.group(), match.start(), match.end()) for match in re_star.finditer(line)]

            # For each number, get all the coordinates that surround that number. Do this for part 2
            for item in star_matches:
                stars.append([item[1], i])

    # Calculate part 1 of the challenge
    for i, num in enumerate(number_boxes, 0):
        # See if any number coordinate is the same as any symbol, if
        # it is, sum that number
        for item in num:
            # print(item)
            for x in symbol_coords:
                if x in item:
                    # print("FOUND SUM:", numbers[i])
                    total_sum += int(numbers[i])

    # Calculate part 2 of the challenge
    for item in stars:
        num_count = 0
        gear_pow = 1
        # Get all number coordinates and go through them
        for i, num in enumerate(number_boxes, 0):
            for num_item in num:
                # If we can find a star next to a number, +1 to count and add multiplication
                if item in num_item:
                    num_count += 1
                    gear_pow *= int(numbers[i])
        
        # If the count is more than 2, add the multiplication to the total
        if num_count > 1:
            pow_total_sum += gear_pow

    print("Part 1:", total_sum)
    print("Part 2:", pow_total_sum)