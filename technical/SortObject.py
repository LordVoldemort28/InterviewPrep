class Garbage():

    def __init__(self, value):
        self.value = value


collection_ = [Garbage(2), Garbage(1), Garbage(3)]
list_ = [[0,2], [1,1], [2,3]]

def garbageSortFunction(garbage):
    return garbage.value


collection_.sort(key=garbageSortFunction)

#or 

collection_.sort(key=lambda garbage: garbage.value)


#sort 2d list
list_.sort(key=lambda item: item[1])
print(list_)

for col in collection_:
    print(col.value)
