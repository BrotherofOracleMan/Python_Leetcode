# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def kthSmallestHelper(root, list_of_nodes):
            if root is None:
                return None
            left = kthSmallestHelper(root.left, list_of_nodes)
            list_of_nodes.append(root)
            if len(list_of_nodes) == k:
                return root
            right = kthSmallestHelper(root.right, list_of_nodes)
            return left or right
        return kthSmallestHelper(root,[]).val
