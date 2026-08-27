class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        maxd = 0

        def rec(root, level):
            nonlocal maxd

            if root is None:
                return

            maxd = max(maxd, level)

            rec(root.left, level + 1)
            rec(root.right, level + 1)

        rec(root, 1)

        return maxd