from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = collections.defaultdict(list)
        visited_set = set()
        number_of_connected_components = 0
        bfs_q = deque()

        for value in edges:
            adj_list[value[0]].append(value[1])
            adj_list[value[1]].append(value[0])
        #print(adj_list)

        for edge in range(n):
            if edge in visited_set:
                continue
            bfs_q.append(edge)
            while len(bfs_q) > 0:
                node = bfs_q.popleft()
                for value in adj_list[node]:
                    if value not in visited_set:
                        bfs_q.append(value)
                        visited_set.add(value)
            number_of_connected_components += 1
            if len(visited_set) == n:
                return number_of_connected_components

        return number_of_connected_components
