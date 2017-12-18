import sys


def calculate_not_shot(a, b):
    """

    :param a: Cans count shot by Harry
    :param b: Cans count shot by Larry
    :type a: int
    :type b: int
    :return: Cans count not shot by Harry and not shot by Larry divided with space
    :rtype: str
    """
    # They will stop when they shot the same can so
    cans_shot_only_by_harry = a - 1
    cans_shot_only_by_larry = b - 1
    cans_not_shot_by_harry = cans_shot_only_by_larry
    cans_not_shot_by_larry = cans_shot_only_by_harry
    return str(cans_not_shot_by_harry) + " " + str(cans_not_shot_by_larry)


# Read line
line = sys.stdin.readline()

# Split line
split_line = line.split(" ")

# Get the numbers
num1 = int(split_line[0])
num2 = int(split_line[1])

# Print the solution
print(calculate_not_shot(num1, num2))
