# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.lonely_nodes = []
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        def getlonelynodeshelper (root):
            if not root:
                return
            elif root and root.right and not root.left:
                self.lonely_nodes.append(root.right.val)
            elif root and root.left and not root.right:
                self.lonely_nodes.append(root.left.val)
            getlonelynodeshelper(root.left)
            getlonelynodeshelper(root.right)
        getlonelynodeshelper(root)
        return self.lonely_nodes
