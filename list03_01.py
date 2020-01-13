#del은 범위지정도 가능

list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]
print(list_b)

list_c = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
print(list_c)

list_d = [0, 1, 2, 3, 4, 5, 6]
del list_d[3:]
print(list_d)