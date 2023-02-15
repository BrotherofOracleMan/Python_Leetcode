# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def rightSideViewHelper(root, num ,arr):
            if root is None:
                return
            if len(arr) == num:
                arr.append(root.val)
            rightSideViewHelper(root.right, num+1, arr)
            rightSideViewHelper(root.left, num+1, arr)
        arr =[]
        rightSideViewHelper(root, 0, arr)
        return arr
