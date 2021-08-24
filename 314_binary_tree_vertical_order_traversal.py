# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque 


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        list_of_values = []
        hash_table = defaultdict(list)
        bfs_queue = deque()
        bfs_queue.append([root,0])
        final_list = []
        
        while(len(bfs_queue) > 0):
            size = len(bfs_queue)            
            for i in range(size):
                value = bfs_queue.popleft()
                list_of_values.append([value[0],value[1]])
                if value[0] and value[0].left:
                    bfs_queue.append([value[0].left,value[1] - 1])
                if value[0] and value[0].right:
                    bfs_queue.append([value[0].right,value[1] + 1])
        
        for pair in list_of_values:
            if pair[0]:
                hash_table[pair[1]].append(pair[0].val)
        
        for key,value in sorted(hash_table.items()):
            final_list.append(value)
            
        return final_list