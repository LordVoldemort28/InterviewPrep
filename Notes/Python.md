Quick Notes
------------------

1. Short notation for iterating in a array or dict
```python3
# Link - https://www.programiz.com/python-programming/methods/built-in/all
# all values true
l = [1, 3, 4, 5]
print(all(l))


#OR 

for item in result["hits"]["hits"]
if all(key in item["_source"] for key in keys)
```


2. The key method for numeric type are 
```python3
abs(-34.5) #34.5

math.ceil(2.17)

math.floor(3.14)

pow(2.71, 3.14) or 2.71 ** 3.14 #22.88355

min(x, -4) 

math.sqrt(225)
```

3. Interconvert integer and strings
```python3
str(42)

int('42')

float('3.14')
```

4. Unlike integers, floats are not infinite precision, and it's convenient to refer to infinity as `float('inf')` an `float('-inf')`.
These value are comparable to integers, and can be used to create psuedo max-int aand pseudo min-int

5. The key methods in random are
```python3
random.randrange(28) #14

random.randint(8, 16) #9

random.random() #0.1783188929273345

random.shuffle(list)

random.choice(list)
```

