def getIterator(array):
    return iter(array)

if __name__ == '__main__':
    
    items = ['a', 'b', 'c']
    
    itemsIterator = getIterator(items)
    
    for x in itemsIterator:
        print(x)