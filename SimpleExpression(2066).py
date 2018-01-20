def get_minimal_outcome(a, b, c):
    """

    :param a: First number
    :param b: Second number
    :param c: Third number
    :type a: int
    :type b: int
    :type c: int
    :return: Returns the minimal outcome of putting specified signs between them
    :rtype: int
    """
    """
    The general solution is a - b * c
    But there are cases when this solution is not the minimal outcome
    For example if a = b = 0 or a = b = 1 or a = 0 and b = 1 we should use a - b - c
    """
    if a == b == 0 or a == b == 1 or a == 0 and b == 1:
        return a - b - c
    else:
        return a - b * c


# Read input
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Print the solution
print(get_minimal_outcome(num1, num2, num3))
