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
    """

    def __init__(self):
        self.parent = {}

    def makeSet(self, universe):

        for i in range(0, universe):
            self.parent[i] = i

    def find(self, x):
        #Time complexity: O(N)
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def optimized_path_compression(self, x):
        #Time complexity: O(logN)
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, count):

        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot != yRoot:
            self.parent[xRoot] = yRoot
            count = count - 1

        return count

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def numParent(self):

        parents = set()

        for parent in self.parent.keys():
            parents.add(self.find(parent))

        return len(parents)


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        row = len(grid)
        col = len(grid[0])

        djs = DisjointSet()
        count = sum([grid[i][j] == "1" for i in range(row)
                    for j in range(col)])

        djs.makeSet(row*col)

        for i in range(0, row):
            for j in range(0, col):

                if grid[i][j] == "0":
                    continue

                index = i*col+j

                if j < col-1 and grid[i][j+1] == '1':
                    count = djs.union(index, index+1, count)
                if i < row-1 and grid[i+1][j] == '1':
                    count = djs.union(index, index+col, count)
        
        return count


tool = Solution()

input = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
print(tool.numIslands(input))
