import sys


def calculate_amount_of_seconds(n, m):
    """

    :param m: Integers from 0 to m
    :param n: Array in which we will check the occurence of the m
    :type m: int
    :type n: int
    :return: Amount of seconds
    :rtype: int
    """
    # For each element of array the programmer will do m + 1 operations
    return (m + 1) * n


# Read line
line = sys.stdin.readline()

# Split line
split_line = line.split(" ")

# Get numbers
num1 = int(split_line[0])
num2 = int(split_line[1])

# Print solution
print(calculate_amount_of_seconds(num1, num2))
