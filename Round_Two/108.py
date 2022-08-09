# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sortedArrayToBSTHelper(left,right):
            if left > right:
                return None
            pivot = left + (right-left)//2
            root = TreeNode(nums[pivot])
            root.left = sortedArrayToBSTHelper(left, pivot-1)
            root.right = sortedArrayToBSTHelper(pivot+1,right)
            return root
        return sortedArrayToBSTHelper(0, len(nums) - 1)
        
