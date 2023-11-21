# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.sol = []

    def tree_path_helper(self, node, path):
        if node:
            path += str(node.val)
            if not node.left and not node.right:
                self.sol.append(path)
            else:
                path += "->"
                self.tree_path_helper(node.left, path)
                self.tree_path_helper(node.right, path)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.tree_path_helper(root, "")
        return self.sol
