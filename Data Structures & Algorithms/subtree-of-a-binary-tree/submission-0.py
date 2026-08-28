# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False

            if p.val!=q.val:
                return False
            
            return rec(p.left,q.left) and rec(p.right,q.right)
        return rec(p,q)  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def rec1(root):
            if root is None:
                return False

            if root.val == subRoot.val:
                if self.isSameTree(root, subRoot):
                    return True

            return rec1(root.left) or rec1(root.right)

        return rec1(root)
        