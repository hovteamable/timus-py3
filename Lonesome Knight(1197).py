import sys


def get_under_attack_square_count(line, row):
    """
    :param line: The line horse is in
    :param row: The row horse is in
    :type line: str
    :type row: int
    :return: Returns the squares count a horse in specified row and line can attack
    :rtype: int
    """
    # The squares' count horse can attack
    attack_square_count = 0

    # Going left 2 and 1 up
    attack_square_count += is_on_board(chr(ord(line) - 2), row - 1)

    # Going left 2 and 1 down
    attack_square_count += is_on_board(chr(ord(line) - 2), row + 1)

    # Going right 2 down 1
    attack_square_count += is_on_board(chr(ord(line) + 2), row + 1)

    # Going right 2 up 1
    attack_square_count += is_on_board(chr(ord(line) + 2), row - 1)

    # Going right 1 up 2
    attack_square_count += is_on_board(chr(ord(line) + 1), row - 2)

    # Going left 1 up 2
    attack_square_count += is_on_board(chr(ord(line) - 1), row - 2)

    # Going left 1 down 2
    attack_square_count += is_on_board(chr(ord(line) - 1), row + 2)

    # Going right 1 down 2
    attack_square_count += is_on_board(chr(ord(line) + 1), row + 2)

    return attack_square_count


def is_on_board(line, row):
    """
    :param line: The line horse is in
    :param row: The row horse is in
    :type line: str
    :type row: int
    :return Whether the horse is on board or not
    :rtype: bool
    """
    return 'a' <= line <= 'h' and 1 <= row <= 8


num = int(input())

# Read other lines for count of num and save it in list
lines = list()
for i in range(0, num, 1):
    line = sys.stdin.readline()
    lines.append(line)

# Print the solution for each line
for line in lines:
    print(get_under_attack_square_count(line[0], int(line[1])))
