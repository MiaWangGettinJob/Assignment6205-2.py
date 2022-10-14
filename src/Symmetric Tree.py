class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def ifSame(nodeA, nodeB):
            if nodeA == None and nodeB == None:
                return True
            elif nodeA == None or nodeB == None:
                return False
            if nodeA.val != nodeB.val:
                return False
            return ifSame(nodeA.left, nodeB.right) and ifSame(nodeA.right, nodeB.left)

        return ifSame(root.left, root.right)


