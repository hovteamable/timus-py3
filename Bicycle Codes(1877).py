def parse_lock_combination(lock):
    """

    :param lock: The lock combination
    :type lock: str
    :return: The number of lock(first zeros ignored)
    :rtype: int
    """
    return int(lock)


def will_open(lock1, lock2):
    """

    :param lock1: The first lock combination
    :param lock2: The second lock combination
    :type lock1: str
    :type lock2: str
    :return: "yes" if thief will open the lock and "no" otherwise
    :rtype: str
    """
    # Parsing combination to numbers
    parsed_combination1 = parse_lock_combination(lock1)
    parsed_combination2 = parse_lock_combination(lock2)

    # Won't open if parsed_combination1 is odd and parsed_combination2 is even
    return "no" if parsed_combination1 % 2 != 0 and parsed_combination2 % 2 == 0 else "yes"


# Read lines
first_line = input()
second_line = input()

# Print solution
print(will_open(first_line, second_line))
