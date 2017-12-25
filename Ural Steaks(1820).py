import sys


def minimal_minutes_to_cook(n, k):
    """

    :param n: Count of steaks to cook
    :type n: int
    :param k: Count of steaks that can be fried on pan at most
    :type k: int
    :return: Minimal number of minutes to cook the steaks
    :rtype int
    """
    # If n <= k then the answer is always 2 so
    if n <= k:
        return 2

    # Each steak must be cook for both sides, so we can consider we have 2*n steaks to cook on one side, so
    if n * 2 % k == 0:
        return n * 2 // k
    # Otherwise we will need one more pan to cook the remaining steaks
    else:
        return n * 2 // k + 1


# Read line
line = sys.stdin.readline()

# Split line
line_split = line.split(' ')

# Get the numbers
num1 = int(line_split[0])
num2 = int(line_split[1])

# Print solution
print(minimal_minutes_to_cook(num1, num2))
