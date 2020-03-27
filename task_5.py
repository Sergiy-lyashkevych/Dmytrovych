from collections import Counter

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
my_result = dict(Counter(my_dict).most_common(3))
print(my_result)


