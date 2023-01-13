from collections import defaultdict

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n = len(sentence1)
        adj_list = defaultdict(list)
        ans = []
        if len(sentence1) != len(sentence2):
            return False

        for prev_val, next_val in similarPairs:
            adj_list[prev_val].append(next_val)
            adj_list[next_val].append(prev_val)
            
        for i in range(0,n):
            if sentence1[i] == sentence2[i]:
                continue
            if sentence2[i] not in adj_list:
                return False
            else:
                found = False
                visited = []
                dfs_stack = [sentence1[i]]
                while(len(dfs_stack) > 0):
                    d = dfs_stack.pop()
                    if d == sentence2[i]:
                        found = True
                    for value in adj_list[d]:
                        if value not in visited:
                            visited.append(value)
                            dfs_stack.append(value)
                if not found:
                    return False
        return True
