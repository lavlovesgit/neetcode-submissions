# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        root1=root
        def rec(root,val,prev):
            if not root:
                if prev.val>val:
                    prev.left=TreeNode(val)
                else:
                    prev.right=TreeNode(val)
                return

            if(val>root.val):
                rec(root.right,val,root)
            else:
                rec(root.left,val,root)
        if not root :
            root1=TreeNode(val)
        else:
            rec(root,val,root)
        return root1
        
            


        

        