import sys


def get_diagonal_array_string(n, m):
    """

    :param n: The matrix's size
    :param m: The matrix
    :type n: int
    :type m : list
    :return: String that represents array created by diagonal order of matrix
    :rtype: str
    """
    diagonal_list = list()
    for i in range(0, n, 1):
        for j in range(0, i + 1, 1):
            diagonal_list.append(m[i - j][j])

    for j in range(1, n, 1):
        first_index = n - 1
        second_index = j
        while first_index >= 0 and second_index < n:
            diagonal_list.append(m[first_index][second_index])
            first_index -= 1
            second_index += 1
    diagonal_string = str()
    for element in diagonal_list:
        diagonal_string += str(element)
        diagonal_string += " "

    return diagonal_string


# Read input
num1 = int(input())

matrix = list()
for i in range(0, num1, 1):
    line = sys.stdin.readline()
    line_split = line.split(" ")
    row = list()
    for value in line_split:
        row.append(int(value))
    matrix.append(row)

# Print Solution
print(get_diagonal_array_string(num1, matrix))
