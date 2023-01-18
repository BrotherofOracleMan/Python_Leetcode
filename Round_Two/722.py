from collections import defaultdict, deque

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = collections.defaultdict(list)
        bfs_q = deque()
        ans = []
        visited_set = defaultdict(bool)
        unvisited_nodes=[]
        single_nodes =[]

        for account in accounts:
            name = account[0]
            if len(account) == 2:
                single_nodes.append(account)
            else:
                for i in range(1, len(account)-1):
                    account_name1, account_name2 = account[i], account[i+1]
                    adj_list[(account_name1,name)].append((account_name2,name))
                    adj_list[(account_name2,name)].append((account_name1,name))
                    visited_set[(account_name1,name)] = False
                    visited_set[(account_name2,name)] = False
                    unvisited_nodes.append((account_name2,name))
                    unvisited_nodes.append((account_name1,name))

        for singlenode in single_nodes:
            if (singlenode[1],singlenode[0]) not in adj_list:
                ans.append(singlenode)
       
        for unvisited_node in unvisited_nodes:
            if not visited_set[unvisited_node]:
                bfs_q.append(unvisited_node)
                part_ans = []
                part_ans.append(unvisited_node[1])
                while(len(bfs_q) > 0):
                    n =bfs_q.popleft()
                    for node in adj_list[n]:
                        if not visited_set[node]:
                            visited_set[node] = True
                            part_ans.append(node[0])
                            bfs_q.append(node)
                part_ans[1:len(part_ans)] = sorted(part_ans[1:len(part_ans)])
                ans.append(part_ans)
        return ans
