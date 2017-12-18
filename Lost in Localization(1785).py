def translate_to_anindilyakwa(n):
    """

    :param n: The number to be translated
    :type n: int
    :return: Return the translation
    :rtype: str
    """
    if 1 <= n <= 4:
        return "few"
    elif 5 <= n <= 9:
        return "several"
    elif 10 <= n <= 19:
        return "pack"
    elif 20 <= n <= 49:
        return "lots"
    elif 50 <= n <= 99:
        return "horde"
    elif 100 <= n <= 249:
        return "throng"
    elif 250 <= n <= 499:
        return "swarm"
    elif 500 <= n <= 999:
        return "zounds"
    else:
        return "legion"


# Read input
n = int(input())

# Print solution
print(translate_to_anindilyakwa(n))
