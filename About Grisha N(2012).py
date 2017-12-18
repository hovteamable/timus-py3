def is_possible(f):
    """

    :param f: The problems count that will be solved in first hour
    :type f: int
    :return: Is it possible for Grisha N to solve 12 tasks in 5 hours ("YES/"NO")
    :rtype: str
    """
    problems_left = 12 - f
    minutes_left = (5 - 1) * 60
    minute_on_each_problem = 45
    problems_to_be_solved_count = minutes_left // minute_on_each_problem
    return "YES" if problems_to_be_solved_count >= problems_left else "NO"


# Read input
n = int(input())

# Print solution
print(is_possible(n))
