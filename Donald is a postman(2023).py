def count_steps(n, l):
    """

    :param n: Letters count
    :param l: Letters list
    :type n : int
    :type l : list
    :return: Returns the count of steps he has to do to deliver all letters
    :rtype: int
    """
    current_position = 0
    steps_count = 0
    first_case = ["Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin"]
    second_case = ["Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"]
    third_case = ["Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"]
    for letter in l:
        if letter in first_case:
            steps_count += current_position
            current_position = 0
        if letter in second_case:
            if not current_position == 1:
                steps_count += 1
            current_position = 1
        if letter in third_case:
            steps_count += 2 - current_position
            current_position = 2

    return steps_count


# Read input
num = int(input())

string_list = list()

for i in range(0, num, 1):
    string_list.append(input())

# Print solution
print(count_steps(num, string_list))
