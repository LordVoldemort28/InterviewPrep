a = set([0, 2])


# (x) != (y)
#Remember brackets around value

print(0 in a, end=" xor ")
print(2 in a, end=" = ")
print((0 in a) != (2 in a))
print(0 in a, end=" xor ")
print(1 in a, end=" = ")
print((0 in a) != (1 in a))
print(2 in a, end=" xor ")
print(1 in a, end=" = ")
print((2 in a) != (1 in a))
print(3 in a, end=" xor ")
print(1 in a, end=" = ")
print((3 in a) != (1 in a))
