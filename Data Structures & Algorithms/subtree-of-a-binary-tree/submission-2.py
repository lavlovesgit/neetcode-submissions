# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSameTree(p,q):
    if p is None and q is None:
        return True
    if ( p is not None and q is None  ) or (q is not None and p is None  ):
        return False
    if p.val!=q.val:
        return False
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        if root.val==subRoot.val:
            if isSameTree(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        


        