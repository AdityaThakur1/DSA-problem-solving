# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #iterative solution
        """daimeter = 0
        if not root:
            return 0
        
        depth_list = [0]*2
        node_list = []
        
        if root.left:
            node_list.append(root.left)
        if root.right:
            node_list.append(root.right)
            
        for i,node in enumerate(node_list):
            dq = collections.deque()
            dq.append([node_list[i],1])
            
            while(dq):
                node, depth = dq.popleft()
                depth_list[i] = max(depth_list[i], depth)

                if node.left:
                    dq.append([node.left, depth_list[i]+1])
                if node.right:
                    dq.append([node.right, depth_list[i]+1])
        
        print(depth_list)            
        return sum(depth_list)"""

        diameter = 0

        def dfs(root):
            nonlocal diameter

            if not root:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)
        return diameter
                
        