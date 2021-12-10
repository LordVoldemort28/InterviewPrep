from collections import ChainMap
# dict-like class for creating a single view of multiple mappings

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)  # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

print(c.maps)  # [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]

print(list(c.keys()))  # ['e', 'f', 'c', 'd', 'a', 'b']

print(list(c.values()))  # [5, 6, 3, 4, 1, 2]

d4 = {'g': 7}
c = c.new_child(d4)

# ChainMap({'g': 7}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
print(c)

print(c['d']) # 4
