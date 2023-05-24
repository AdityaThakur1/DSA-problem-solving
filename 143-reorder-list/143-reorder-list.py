# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        h1, h2 = head, head
        
        while(h2 and h2.next):
            h1 = h1.next
            h2 = h2.next.next
        
        #h1 = h1.next
        #points to 2nd half of linkedlist
        #reverse the 2nd half od linked list
        prev = None
        while(h1):
            temp = h1.next
            h1.next = prev
            prev = h1
            if(temp is not None):
                h1 = temp
            else:
                break

        h2 = head
        while(h1.next and h2.next):
                t1, t2 = h1.next, h2.next
                h2.next = h1
                h1.next = t2
                h1, h2 = t1, t2
        
        return head
            
            