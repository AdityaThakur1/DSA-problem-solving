# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h1, h2 = head, head
        
        while (h2 and h2.next):
            h1 = h1.next
            h2 = h2.next.next
            
            if h1 == h2:
                return True
            
        return False