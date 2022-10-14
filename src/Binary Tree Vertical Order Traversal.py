from collections import defaultdict
from collections import deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        columnTable = defaultdict(list)
        queue = deque([(root,0)])
        mincol, maxcol = 0, 0

        while queue:
            node, col = queue.popleft()

            if node:
                columnTable[col].append(node.val)
                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))

                mincol = min(mincol, col)
                maxcol = max(maxcol, col)


        return [columnTable[x] for x in range(mincol, maxcol+1)]
