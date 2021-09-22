class Solution:
    def allPathsSourceTarget(self, graph):

        all_path = []

        def dfs(current, path):

            if current == len(graph)-1:
                all_path.append(path)
                return

            for neighbor in graph[current]:
                dfs(neighbor, path+[neighbor])

        dfs(0, [0])

        return all_path

tool = Solution()
input = [[1, 2], [3], [3], []]
print(tool.allPathsSourceTarget(input))
