from collections import Counter

counts = Counter("mississippi")

# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(counts)

# Counter({'i': 6, 's': 6, 'm': 2, 'p': 2, 'o': 1, 'u': 1, 'r': 1})
counts.update("missouri")
print(counts)

# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1, 'o': 0, 'u': 0, 'r': 0})
counts.subtract("missouri")
print(counts)

# [('i', 4), ('s', 4), ('p', 2), ('m', 1), ('o', 0), ('u', 0), ('r', 0)]
print(counts.most_common())

# [('i', 4)]
print(counts.most_common(1))
print(dir(counts))

