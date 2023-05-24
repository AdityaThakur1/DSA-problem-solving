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
        while(l1 and l2):
            s = l1.val + l2.val + carry
            carry = s//10
            s = s%10
            
            tail.next = ListNode(val=s)
            tail = tail.next
            
            l1, l2 = l1.next, l2.next
        
        while(l1):
            s = l1.val + carry
            carry = s//10
            s = s%10
            tail.next = ListNode(val = s)
            tail = tail.next
            l1 = l1.next
        
        while(l2):
            s = l2.val + carry
            carry = s//10
            s = s%10
            tail.next = ListNode(val = s)
            tail = tail.next
            l2 = l2.next
            
        if carry > 0:
            tail.next = ListNode(val = carry)
        
        return res.next