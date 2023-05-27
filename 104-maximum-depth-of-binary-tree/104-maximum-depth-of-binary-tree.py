# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #recursive solution
        """if root is None:
            return 0
        height = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        return height"""
    
        #iterative solution
        dq = collections.deque()
        if root:
            dq.append([root,1])
        else:
            return 0
        max_height = 0
        
        while(dq):
            
            node, depth = dq.popleft()
            max_height = max(max_height, depth)
            
            if node.left:
                dq.append([node.left, max_height+1])
            if node.right:
                dq.append([node.right, max_height+1])
                
        return max_height
                