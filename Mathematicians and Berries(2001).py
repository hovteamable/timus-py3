import sys


def calculate_mass_of_berries(first_with_berries, second_with_berries,
                              first_without_berries, second_without_berries):
    """

    :param first_with_berries: Weight of the first mathematician's basket with berries
    :param second_with_berries: Weight of the second mathematician's basket with berries
    :param first_without_berries: Weight of the first mathematician's basket without berries
    :param second_without_berries: Weight of the second mathematician's basket without berries
    :type first_with_berries: int
    :type second_with_berries: int
    :type first_without_berries: int
    :type second_without_berries: int
    :return: Mass of berries picked by first mathematician and the second separated with space
    :rtype str
    """
    first_berry_mass = first_with_berries - first_without_berries
    second_berry_mass = second_with_berries - second_without_berries
    return str(first_berry_mass) + " " + str(second_berry_mass)


# Read all lines
first_line = sys.stdin.readline()
second_line = sys.stdin.readline()
third_line = sys.stdin.readline()

# Split all lines
split_first_line = first_line.split()
split_second_line = second_line.split()
split_third_line = third_line.split()

# Get numbers
num1 = int(split_first_line[0])
num2 = int(split_first_line[1])
num3 = int(split_third_line[0])
num4 = int(split_second_line[1])

# Print the solution
print(calculate_mass_of_berries(num1, num2, num3, num4))
