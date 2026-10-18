# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root :
                return root
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            
            if root.right is  None and root.left is None:
                return None
            elif root.right is not None and root.left is None:
                return root.right
            elif root.left is not None and root.right is None:
                return root.left
            elif root.left is not None and root.right is not None:
                succ=root.right
                while succ.left:
                    succ=succ.left
                root.val=succ.val
                root.right=self.deleteNode(root.right, root.val)

        return root    



