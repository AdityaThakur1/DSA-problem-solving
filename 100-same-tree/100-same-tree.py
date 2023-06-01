# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = collections.deque()
        dp = collections.deque()
        
        dq.append(p)
        dp.append(q)
        
        while(dq):
            rq = dq.popleft()
            rp = dp.popleft()
            
            if rq and rp:
                if rq.val != rp.val:
                    return False
                
                dq.append(rq.left)
                dq.append(rq.right)
                
                dp.append(rp.left)
                dp.append(rp.right)
                
            elif rp or rq:
                return False
        
        return True
                