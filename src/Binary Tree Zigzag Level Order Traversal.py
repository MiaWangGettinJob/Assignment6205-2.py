from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []
        if not root:
            return result
        queue.append(root)
        left_right = False
        while queue:
            length = len(queue)
            currentLevel = deque()
            left_right = not left_right
            for i in range(length):
                node = queue.popleft()
                if left_right:
                    currentLevel.append(node.val)
                else:
                    currentLevel.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(currentLevel)

        return result

