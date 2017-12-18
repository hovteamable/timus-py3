import sys


def calculate_sum(a, b):
    """

    :param a : The First Number
    :param b : The Second Number
    :type a: int
    :type b: int
    :return: Return the sum of the first and second number
    :rtype: int
    """
    return a + b


# Read line
line = sys.stdin.readline()

# Split line
split_line = line.split(' ')

# Get the numbers
num1 = int(split_line[0])
num2 = int(split_line[1])

# Print solution
print(calculate_sum(num1, num2))
