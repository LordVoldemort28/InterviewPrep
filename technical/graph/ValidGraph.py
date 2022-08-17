class DisjointSet():

    def __init__(self):
        self.parent = {}

    def makeSet(self, universe):

        for i in range(0, universe):
            self.parent[i] = i

    def find(self, x):

        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def optimized_path_compression(self, x):
        #Time complexity: O(logN)
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):

        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot != yRoot:
            self.parent[xRoot] = yRoot

    def connected(self, x, y):
        return self.find(x) = self.find(y)

    def numParent(self):

        numRoot = []
        tempParent = set(self.parent.values())

        for each in tempParent:
            root = self.find(each)
            if root not in numRoot:
                numRoot.append(root)
        return len(numRoot)
    
class ValidTree(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n-1 != len(edges):
            return False

        djs = DisjointSet()
        djs.makeSet(n)

        for (x, y) in edges:
            djs.union(x, y)

        print(djs.numParent())
        return djs.numParent() == 1


tool = ValidTree()

n, edges = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]
print(tool.validTree(n, edges) == True)

n, edges = 5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(tool.validTree(n, edges) == False)

n, edges = 5, [[0, 1], [0, 4], [1, 4], [2, 3]]
print(tool.validTree(n, edges) == False)
