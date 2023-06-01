# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bal(self, root, ht):
        if not root:
            return (True, 0)
                
        lb, lt = self.bal(root.left,0)
        rb, rt = self.bal(root.right,0)
        
        res = lb and rb
        if res == True and abs(lt-rt) > 1:
            res = False
        
        return (res, max(lt,rt)+1)
        
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res , _ = self.bal(root,0)
        
        return res