from collections import defaultdict
# The functionality of both dictionaries and defualtdict are almost 
# same except for the fact that defualtdict never raises a KeyError. 
# It provides a default value for the key that does not exists.

a = defaultdict(int)

# defaultdict(<class 'int'>, {})
print(a)

word = "mississippi"

for letter in word:
    a[letter] += 1

# defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
print(a)
