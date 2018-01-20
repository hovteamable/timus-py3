import sys


def get_maximum_total_force_and_middle(n, l):
    """

    :param n: The len of list
    :param l: The list of magic forces acting on each section(1<=l[i]<=10^6)
    :type n: int
    :type l: list
    :return: Returns the max total force of the field acting on three cons. section on the wall
    and the index of the middle element of the section seperated with space
    :rtype: str
    """
    max_total_force = 3  # As the minimal value that l[i] can have is 1
    index_of_middle_element = 1

    for i in range(0, n - 2, 1):
        total_force = l[i] + l[i + 1] + l[i + 2]
        if total_force >= max_total_force:
            max_total_force = total_force
            index_of_middle_element = (i + 1) + 1

    return str(max_total_force) + " " + str(index_of_middle_element)


# Read input
num1 = int(input())
first_line = sys.stdin.readline()
first_line_split = first_line.split(" ")
numbers = list()
for split in first_line_split:
    numbers.append(int(split))

# Print solution
print(get_maximum_total_force_and_middle(num1, numbers))
