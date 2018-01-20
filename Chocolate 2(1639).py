import sys


def who_will_go_first(m, n):
    """

    :param m: Count of rows of the chocolate
    :param n: Count of lines of the chocolate
    :type m: int
    :type n: int
    :return:  Returns "[:=[first]" if Karlsson should go first and "[second]=:] otherwise
    :rtype: str
    """
    if m * n % 2 == 0:
        return "[:=[first]"
    else:
        return "[second]=:]"


# Read input
line = sys.stdin.readline()
line_split = line.split(" ")
num1 = int(line_split[0])
num2 = int(line_split[1])

# Print solution
print(who_will_go_first(num1, num2))
