# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=collections.deque()
        if not root:
            return []
        res=[]
        q.append(root)
        while(q): 
            l=len(q) 
            lev=[] 
            for i in range(l): 
                el=q.popleft() 
                lev.append(el.val) 
                if(el.left):
                    q.append(el.left) 

                if(el.right):
                    q.append(el.right)
            res.append(lev)
        return res
        
            

            
        