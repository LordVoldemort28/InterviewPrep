from collections import OrderedDict, defaultdict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.minFrequency = 0
        self.capacity = capacity
        self.frequency = defaultdict(int)
        self.cache = defaultdict(OrderedDict)
        
    def updateFrequency(self, key, value=None):
        
        keyFrequency = self.frequency[key]
        currentValue = self.cache[keyFrequency].pop(key)
        
        if value is not None:
            currentValue = value
            
        self.frequency[key] += 1
        self.cache[keyFrequency+1][key] = currentValue
        
        if keyFrequency == self.minFrequency and not self.cache[keyFrequency]:
            self.keyFrequency += 1
            
        return currentValue

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.frequency:
            return -1
        
        return self.updateFrequency(key)
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        
        if key in self.frequency:
            self.updateFrequency(key, value)
        else:
            if self.capacity == len(self.frequency):
                self.frequency.pop(self.cache[self.minCount].popItem(last=False))
                
            self.minCount = 1
            self.cache[1][key] = value
            self.frequency[key] = 1


dict_ = OrderedDict()
dict_[key] = value
