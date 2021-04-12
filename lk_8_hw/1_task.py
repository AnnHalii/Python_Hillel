nums = [61, 228, 9]


def biggest_num(list_of_nums):
    return ''.join(sorted(map(str, list_of_nums), reverse=True))


print(biggest_num(nums))
