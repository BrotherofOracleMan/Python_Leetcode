# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.index = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTreehelper(left, right, inorder_map):
            if left >= right:
                return None
        #create a map here
            value = preorder[self.index]
            root = TreeNode(value)
            index = inorder_map[value]
            self.index += 1
            root.left = buildTreehelper(left, index, inorder_map)
            root.right = buildTreehelper(index+1, right, inorder_map)
            return root
        inorder_map = {inorder[i]:i for i in range(0, len(inorder))}
        return buildTreehelper(0, len(inorder), inorder_map)
