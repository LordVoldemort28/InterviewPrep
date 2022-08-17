class DisjointSet():
    """
    Disjoint sets forest are data structure where each set is represent
    by tree data in which each node holds a reference to its parents.
    And the representative of each set in the root of that set's tree.
    
    Normal Find Function
    --------------------
    MakeSet: O(N)
    Union: O(H)
    Find: O(H)
    Connected: O(H)
    
    H is hight of the tree
    
    Path Compression Optimization
    -----------------------------
    MakeSet: O(N)
    Find: O(logN)
    Union: O(logN)
    Connected: O(logN)
    
    Modified by: Rahul Prajapati
    Source: https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/
    """
    def __init__(self):
        self.parent = {}

    def makeSet(self, universe):

        for i in range(0, universe):
            self.parent[i] = i

    def find2(self, x):
        #Time complexity: O(N)
        if self.parent[x] == x:
            return x
        return self.find2(self.parent[x])

    #Optimized path compression find
    def find(self, x):
        #Time complexity: O(logN)
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):

        if x not in self.parent.keys():
            self.parent[x] = x
            
        if y not in self.parent.keys():
            self.parent[y] = y
            
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot != yRoot:
            self.parent[xRoot] = yRoot

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def numParent(self):

        topParent = set()
        
        for parent in self.parent:
            topParent.add(self.find(parent))
            
        return len(topParent)


class Solutions(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        size = len(isConnected)

        djs = DisjointSet()

        # djs.makeSet(size)

        for i in range(0, size):
            for j in range(0, size):
                if isConnected[i][j] == 1:
                    djs.union(i, j)
                    
        print(djs.parent)
        return djs.numParent()

if __name__ == '__main__':
    
    tool = Solutions()

    input = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print(tool.findCircleNum(input))
