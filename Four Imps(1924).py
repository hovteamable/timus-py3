def black_or_grimy(n):
    """

    :param n: The number until which we will put "+" or "-"
    :type n : int
    :return: Return black if black imps win and grimy otherwise
    :rtype: str
    """
    if is_sum_even(n):
        return "black"
    else:
        return "grimy"


def is_sum_even(n):
    """

    :param n: The number until which we will put "+" or "-"
    :type n : int
    :return: Return whether the sum of specified expression is even or odd
    :rtype: bool
    """
    if n % 2 == 0:
        if n % 4 == 0:
            return True
        else:
            return False
    else:
        return not is_sum_even(n - 1)


# Read input
num = int(input())

# Print solution
print(black_or_grimy(num))
