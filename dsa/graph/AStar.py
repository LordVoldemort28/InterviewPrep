import heapq

"""
Optimal path searching algorithm in graph. It can be seen as extension of Djikstra algorithm
which make greedy choice based on max heuristic attribute. 

Time complexity: O(|E|) = O(b^d)
Space complexity: O(|V|) = O(b^d)

Modified by: Rahul Prajapati
Source: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
"""

"""
Pseudocode

# A* (star) Pathfinding

    # Initialize both open and closed list
    let the openList equal empty list of nodes 
    let the closedList equal empty list of nodes

    # Add the start node
    put the startNode on the openList (leave it's f at zero)

    # Loop until you find the end
    while the openList is not empty

        # Get the current node
        let the currentNode equal the node with the least f value
        remove the currentNode from the openList
        add the currentNode to the closedList

        # Found the goal
        if currentNode is the goal
            Congo! You've found the end! Backtrack to get path

        # Generate children
        let the children of the currentNode equal the adjacent nodes

        for each child in the children

            # Child is on the closedList
            if child is in the closedList
                continue to beginning of for loop

            # Create the f, g, and h values
            child.g = currentNode.g + distance between child and current
            child.h = distance from child to end
            child.f = child.g + child.h

            # Child is already in openList
            if child.position is in the openList's nodes positions
                if the child.g is higher than the openList node's g
                    continue to beginning of for loop

            # Add the child to the openList
            add the child to the openList
"""

class MinHeap:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        if not len(self):
            return None

        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)


class StepNode:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        # G - Distance between the current node and the state node
        # H - Estimated from the current node to the end node
        # F - (F=G+H) Total cost of the node to reach the goal
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, stepNode):
        return self.position == stepNode.position

    def __lt__(self, stepNode):
        return self.f < stepNode.f

    def __str__(self):
        return "Parent = {}\nPosition = {}\nG = {}\nH = {}\nF = {}".format(
            self.parent,
            self.position,
            self.g,
            self.h,
            self.f
        )

def aStar(maze, start, end):
    """
    Return a list of tuples as a path from the given start to the given end 
    in the given maze
    """

    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        print("Path is not possible")
        return

    start_node = StepNode(None, start)
    end_node = StepNode(None, end)

    open = MinHeap()
    closed = []

    maze_length = len(maze)-1
    maze_width = len(maze[0])-1

    open.push(start_node)

    while open:

        # Get the current node
        current_node = open.pop()

        # Pop current off the open list, add to closed list
        closed.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # Generate children
        children = []

        # Get all coordinates for each direction
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # Get node position
            jump_position_x = current_node.position[0] + new_position[0]
            jump_position_y = current_node.position[1] + new_position[1]

            # Set position
            jump_position = (jump_position_x, jump_position_y)

            # Make sure within range
            if jump_position_x > maze_length or jump_position_x < 0 or \
                    jump_position_y > maze_width or jump_position_y < 0:
                continue

            # Make sure walkable terrain:
            if maze[jump_position_x][jump_position_y] != 0:
                continue

            # Create new node
            new_node = StepNode(current_node, jump_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed:
                if child == closed_child:
                    continue

            # Create the f, g and h value
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open.heap:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open.push(child)


def print_path(path):

    for idx in range(0, len(path)-1):
        print("{} ----> {}".format(path[idx], path[idx+1]))


# 0 is representing walkable step and 1 is wall
maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (9, 5)

path = aStar(maze, start, end)
print_path(path)
