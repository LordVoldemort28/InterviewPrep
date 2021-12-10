from collections import OrderedDict

dict_ = OrderedDict()

dict_['one'] = 1
dict_['two'] = 2
dict_['three'] = 3

# print(dir(dict_))
"""
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dict__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', 
'__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', 
'__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'move_to_end', 'pop', 'popitem', 
'setdefault', 'update', 'values']
"""

print(dict_) #OrderedDict([('one', 1), ('two', 2), ('three', 3)])

# OrderedDict([('two', 2), ('three', 3), ('one', 1)])
print(dict_.move_to_end('one'))
print(dict_)

print(dict_.popitem())  # ('one', 1)
print(dict_.popitem(last=False)) # ('two', 2)

