import random

class RandomizedSet:

    def __init__(self):
        self.randomSet = dict()
        self.data = list()
        

    def insert(self, val: int) -> bool:

        if val in self.randomSet:
            return False
        
        self.randomSet[val] = len(self.data)
        self.data.append(val)

        return True

    def remove(self, val: int) -> bool:

        if not val in self.randomSet:
            return False
        
        removeItemIndex = self.randomSet[val]
        lastItemInList = self.data[-1]
        
        self.randomSet[lastItemInList] = removeItemIndex
        self.data[removeItemIndex] = lastItemInList
        
        self.data.pop()
        self.randomSet.pop(val)
        
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.data)
