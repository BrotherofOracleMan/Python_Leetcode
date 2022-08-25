# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrderHelper(root):
            if root is None:
                return
            yield from inOrderHelper(root.left)
            yield root.val
            yield from inOrderHelper(root.right)
        
        cur = head = TreeNode()
        
        for i,val in enumerate(inOrderHelper(root)):
            if i == 0:
                cur.val = val
            else:
                cur.right = TreeNode(val)
                cur = cur.right

        return head
