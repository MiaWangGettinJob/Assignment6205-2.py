from collections import defaultdict
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.maxdepth = 0
        if not root:
            return 0
        NodeDepth = defaultdict(list)
        def recueseTree(node):
            if node is None:
                return -1
            depth = max(recueseTree(node.left), recueseTree(node.right)) + 1
            NodeDepth[depth].append(node.val)
            self.maxdepth = max(depth, self.maxdepth)
            return depth

        recueseTree(root)

        return [NodeDepth[x] for x in range(self.maxdepth + 1)]

