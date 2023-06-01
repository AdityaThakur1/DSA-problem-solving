# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        """
        deq = collections.deque()
        deq.append((root,0))
        
        result = []
        
        while(deq):
            node, lv = deq.popleft()
            
            if len(result) >= lv+1:
                result[lv].append(node.val)
            else:
                result.append([node.val])
            
            if node.left:
                deq.append((node.left, lv+1))
            if node.right:
                deq.append((node.right, lv+1))
            
        return result"""

        deq = collections.deque([root])
        result = []
        
        while(deq):
            val = []
            
            for i in range(len(deq)):
                node = deq.popleft()
                val.append(node.val)
                
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                
            result.append(val)
            
        return result