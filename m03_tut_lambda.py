my_list = [5, 4, 3]


# Square lambda
my_list = list(map(lambda a: a * a, my_list))
print(my_list)


# List sorting lambda
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a = list(sorted(a, key=lambda a: a[1]))
print(a)
