class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def insertBST(root,val):
            if root is None or root.val == val:
                root = TreeNode(val)
            elif root.val < val:
                root.right = insertBST(root.right,val)
            else:
                root.left = insertBST(root.left,val)
            return root
            
            
        root = TreeNode(preorder[0])
        root.left = None
        root.right = None
        lesser = [i for i in preorder if i < root.val]
        greater = [i for i in preorder if i > root.val]
        
        for num in greater:
            insertBST(root,num)
        for num in lesser:
            insertBST(root,num)

            
        return root
