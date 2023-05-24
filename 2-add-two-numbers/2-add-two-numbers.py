# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res
        carry = 0
        
        while(l1 or l2):
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            
            s = l1val + l2val + carry
            carry = s//10
            s = s%10
            
            tail.next = ListNode(val=s)
            tail = tail.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                  
        if carry > 0:
            tail.next = ListNode(val = carry)
        
        return res.next