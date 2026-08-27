# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        levl=0

        def rec(root,levl):
            if root is None :
                return 
            if levl==len(res):
                res.append([])
            res[levl].append(root.val)

            rec(root.left,levl+1)
            rec(root.right,levl+1)
        rec(root,0)
        return res
                
        