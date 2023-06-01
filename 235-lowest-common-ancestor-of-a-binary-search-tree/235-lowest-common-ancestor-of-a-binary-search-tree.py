# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dq = collections.deque()
        dq.append(root)
        
        while(dq):
            node = dq.popleft()
            
            if node.val > p.val and node.val > q.val:
                dq.append(node.left)
            elif node.val < p.val and node.val < q.val:
                dq.append(node.right)
            else:
                return node
        
        return root