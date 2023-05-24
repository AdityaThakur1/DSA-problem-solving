# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return head.next
        
        h1, h2 = head, head
        
        while(n):
            h1 = h1.next
            n = n-1
            
        if(h1 is None):
            return head.next
        
        while(h1.next):
            h1, h2 = h1.next, h2.next
        
        if h2.next.next:
            h2.next = h2.next.next
        else:
            h2.next = None
        
        return head