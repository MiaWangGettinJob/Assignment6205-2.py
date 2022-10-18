from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root,0)])
        maxwidth = 0

        while queue:
            _, headIndex = queue[0]
            for _ in range(len(queue)):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, index * 2 + 1))


            maxwidth = max(maxwidth, high - low + 1)

        return maxwidth
                