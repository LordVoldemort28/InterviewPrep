# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value):
        # Write your code here.
        if self.value > value and self.left:
            return self.left.contains(value)
        elif self.value < value and self.right:
            return self.right.contains(value)
        else:
            return self.value == value

    def find(self, value):

        # Write your code here.
        if self.value > value and self.left:
            return self.left.find(value)
        elif self.value < value and self.right:
            return self.right.find(value)
        else:
            return self if self.value == value else None

    def remove(self, value, parentNode=None):
        
        if value < self.value and self.left:
            parentNode = self
            self.left.remove(value, parentNode)
        elif value > self.value and self.right:
            parentNode = self
            self.right.remove(value, parentNode)
        else:
            #Both child are there
            if self.right and self.left:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif not parentNode:
                if self.left:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right:
                    self.value = self.right.value
                    self.right = self.right.right
                    self.left = self.right.left
            elif parentNode.left == self:
                parentNode.left = self.left if self.left else self.right
            elif parentNode.right == self:
                parentNode.right = self.left if self.left else self.right
        return self

    def getMinValue(self):
        if self.left:
            return self.left.getMinValue()
        else:
            return self.value

if __name__ == '__main__':
        
    root = BST(10)

    for i in range(0, 20):
        root.insert(i)


