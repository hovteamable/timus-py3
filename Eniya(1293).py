import sys


def calculate_thorium_sulphide_count(n, a, b):
    """

    :param n: Rectangular panel's count on one sie
    :param a: Dimension of rect
    :param b: Dimension of rect
    :type n : int
    :type a : int
    :type b : int
    :return: The thorium sulphide count to reconstruct the ship (nanogramm/m^2)
    :rtype: int
    """
    for_one_panel = a * b
    for_one_side = n * for_one_panel
    total = 2 * for_one_side
    return total


# Read line
line = sys.stdin.readline()

# Split line
split_line = line.split(" ")

# Get the numbers
num1 = int(split_line[0])
num2 = int(split_line[1])
num3 = int(split_line[2])

# Print solution
print(calculate_thorium_sulphide_count(num1, num2, num3))
