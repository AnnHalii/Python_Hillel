nums = [61, 228, 9]


biggest_num = lambda x: ''.join(sorted(map(str, x), reverse=True))
print(biggest_num(nums))

assert biggest_num(nums) == '961228'
