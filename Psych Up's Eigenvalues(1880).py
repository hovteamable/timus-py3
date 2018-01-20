import sys


def get_teams_eigenvalue(e1, e2, e3):
    """
    Returns eigenvalues of the team
    :param e1: The eigenvalues of first person
    :param e2: The eigenvalues of second person
    :param e3: The eigenvalues of third person
    :type e1: list
    :type e2: list
    :type e3: list
    :return: Returns the count of eigenvalues of the team
    :rtype: int
    """
    '''
     The idea is to fix one teammate's eigenvalue and see does the other 
     teammates' eigenvalue list contain that
    '''
    eigenvalues_count = 0
    for e in e1:
        if contains_binary(e2, e) and contains_binary(e3, e):
            eigenvalues_count += 1
    return eigenvalues_count


def contains_binary(l, elem):
    """

    :param l: The list where we will try to find the element
    :param elem: The element we are looking for
    :return: Whether the list contains the element or not
    :rtype: bool
    """

    first = 0
    last = len(l) - 1

    while first <= last:
        index = (first + last) // 2

        if l[index] == elem:
            return True
        elif l[index] > elem:
            last = index - 1
        elif l[index] < elem:
            first = index + 1
        else:
            return False


# Read first number
num1 = int(input())

# Read first line
first_line = sys.stdin.readline()

# Read second number
num2 = int(input())

# Read second line
second_line = sys.stdin.readline()

# Read third number
num3 = int(input())

# Read third line
third_line = sys.stdin.readline()

# Split the lines and put it in num list
first_line_split = first_line.split(" ")
second_line_split = second_line.split(" ")
third_line_split = third_line.split(" ")
num_list1 = list()
num_list2 = list()
num_list3 = list()
for i in range(0, num1, 1):
    num_list1.append(int(first_line_split[i]))
for i in range(0, num2, 1):
    num_list2.append(int(second_line_split[i]))
for i in range(0, num3, 1):
    num_list3.append(int(third_line_split[i]))

# Print solution
print(get_teams_eigenvalue(num_list1, num_list2, num_list3))
