import re

if __name__ == "__main__":
    with open("input.txt") as f:
        win_total_sum = 0
        scratchcards_total_sum = 0
        scratchcards = []
        
        # Get through every line
        for line in f:
            win_count = 0
            
            # Get all items after the : and before the | and put them in a list
            win = re.compile(r'(?<=:)(.*?)(?=\|)').findall(line)
            win = [int(n) for n in win[0].split()]

            # Get all items after the | and put them in a list
            my_nums = re.compile(r'(?<=\|).*').findall(line)
            my_nums =  [int(n) for n in my_nums[0].split()]
            
            # Count every win if a number in the win list is in my nums
            for n in my_nums:
                if n in win:
                    win_count += 1
            
            # For every win in each scratchcard, double the prize and sum everything
            if (win_count != 0):
                win_total_sum += pow(2, win_count - 1)
            
            # Append how many winning numbers each one have and init 0 for part 2
            scratchcards.append([win_count, 0])

        # For part 2, go through each card and add the next cards according to
        # how much they won. Do this for every subsequent card and sum the quantity
        for i, item in enumerate(scratchcards):
            for x in range(item[0]):
                for y in range(item[1] + 1):
                    scratchcards[i + x + 1][1] += 1
            scratchcards_total_sum += item[1] + 1

    print("Part 1:", win_total_sum)
    print("Part 2:", scratchcards_total_sum)

            