# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        dq = collections.deque()
        if root:
            dq.append(root)
        else:
            return []
        
        while(dq):
            val = []
            
            for i in range(len(dq)):
                node = dq.popleft()
                val.append(node.val)
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                
            res.append(val[-1])           
                
        return res