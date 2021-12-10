from collections import namedtuple
import collections

#namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
Person = namedtuple('Person', ['name', 'age', 'gender'])

P1 = Person('Rahul', 24, 'male')
P2 = Person('Shivani', 25, 'female')

print(P1)  # Person(name='Rahul', age=24, gender='male')
print(P2)  # Person(name='Shivani', age=25, gender='female')

print(P1[1]) # 24
print(P2[1]) # 25

print(P1.name) # Rahul 
print(P2.name) # Shivani

print(getattr(P1, 'age')) # 24

print(dir(namedtuple))


# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))

print(Student._fields)


"""
The namedtuple instance using iterable is:
Student(name='Manjeet', age='19', DOB='411997')
The OrderedDict instance using namedtuple is:
OrderedDict([('name', 'Nandini'), ('age', '19'), ('DOB', '2541997')])
The namedtuple instance from dict is:
Student(name='Nikhil', age=19, DOB='1391997')
All the fields of students are : 
('name', 'age', 'DOB')
"""
