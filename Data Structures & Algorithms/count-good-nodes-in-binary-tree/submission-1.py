class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0

        def inorder(root, max_so_far):
            nonlocal c

            if not root:
                max_so_far = 0
                return

            if max_so_far <= root.val:
                max_so_far= root.val
                c += 1

            inorder(root.left, max_so_far)
            inorder(root.right, max_so_far)

        inorder(root, root.val)

        return c