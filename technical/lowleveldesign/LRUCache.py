from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.cache[key] = value
        self.cache.move_to_end(key)
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
        return


#Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(2)
lRUCache.put(1, 1)
# cache is {1 = 1}
lRUCache.put(2, 2)
# cache is {1 = 1, 2 = 2}
print(lRUCache.get(1) == 1)
# return 1
lRUCache.put(3, 3)
# LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
print(lRUCache.get(2) == -1)
# returns - 1 (not found)
lRUCache.put(4, 4)
# LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
print(lRUCache.get(1) == -1)
# return -1 (not found)
print(lRUCache.get(3) == 3)
# return 3
print(lRUCache.get(4) == 4)

