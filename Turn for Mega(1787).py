import sys


def calculate_number_of_cars(k, n, l):
    """

    :param k: Number of cars which that are able to take a turn in one minute
    :param n: Minutes of observation
    :param l: List where each element represents number of cars standing at the turn at i-th minute
    :type k: int
    :type n: int
    :type l: list
    :return: Number of cars currently standing in the traffic jam
    :rtype: int
    """

    # Calculate how many cars will be in the last minute
    for i in range(0, n - 1, 1):
        cars_left_at_i_minute = l[i] - k
        if cars_left_at_i_minute < 0:
            cars_left_at_i_minute = 0
        l[i + 1] += cars_left_at_i_minute

    # Calculate how many cars will be after the last minute
    cars_left_after_last_minute = l[-1] - k

    if cars_left_after_last_minute < 0:
        cars_left_after_last_minute = 0

    return cars_left_after_last_minute


# Read lines
first_line = sys.stdin.readline()
second_line = sys.stdin.readline()

# Split lines
split_first_line = first_line.split(" ")
split_second_line = second_line.split(" ")

# Getting numbers
num1 = int(split_first_line[0])
num2 = int(split_first_line[1])

num_list = list()

for i in range(0, num2, 1):
    num_list.append(int(split_second_line[i]))

# Print solution
print(calculate_number_of_cars(num1, num2, num_list))
