my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
print()
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)
