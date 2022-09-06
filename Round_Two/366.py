# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_table = defaultdict(list)
        max_height = 0
        def findleaveshelper(root):
            if root == None:
                return 0
            left = findleaveshelper(root.left)
            right = findleaveshelper(root.right)
            height = max(left,right)
            hash_table[height].append(root.val)
            return height + 1
        findleaveshelper(root)
        
        return hash_table.values()
