from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        adj_list = [set() for i in range(n)]

        for pair in edges:
            adj_list[pair[0]].add(pair[1])
            adj_list[pair[1]].add(pair[0])
        
        leaves = deque()

        #add leaves
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n

        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            size = len(leaves)
            for s in range(size):
                leaf = leaves.popleft()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    leaves.append(neighbor)
        return list(leaves)

