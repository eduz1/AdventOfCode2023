# Get how many ways you can win the race surpassing the distance record
def get_ways(time, dist):
    races_won = 0

    # Skip 0 and time because they will result in 0 distance
    for i in range(1, time):
        # Get distance by multiplying the time pressed by the remaining time
        race_dist = (time - i) * i
        # Count if we surpassed the distance
        if race_dist > dist:
            races_won += 1

    return races_won

if __name__ == "__main__":
    time_arr = []
    dist_arr = []
    single_time = ""
    single_dist = ""
    total_ways = 1

    # Get all digits into their respective lists
    with open("input") as f:
        time_arr = [int(num) for num in f.readline().split() if num.isdigit()]
        dist_arr = [int(num) for num in f.readline().split() if num.isdigit()]

    for time, dist in zip(time_arr, dist_arr):
        # Calculate time and multiply each race for 1st part
        total_ways *= get_ways(time, dist)

        # Concatenate each digit for the 2nd part
        single_time += str(time)
        single_dist += str(dist)

    # Convert concatenated value into an int
    single_time = int(single_time)
    single_dist = int(single_dist)

    # Print part 1 and calculate and print for part 2
    print("Part 1:", total_ways)
    print("Part 2:", get_ways(single_time, single_dist))

        