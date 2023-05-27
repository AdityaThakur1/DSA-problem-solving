# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root"""
        
        #iterative solution
        dq = collections.deque()
        if root:
            dq.append(root)
        else:
            return root
        
        while(len(dq)>0):
            node = dq.popleft()
            node.right, node.left = node.left, node.right
            if(node.left):
                dq.append(node.left)
            if(node.right):
                dq.append(node.right)
        
        return root
        