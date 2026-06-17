# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (n > 0 and not head.next):
            return None
        
        def reverse(list_head: ListNode) -> None:
            c = list_head
            t = rev = None
            while c:
                t = c.next
                c.next = rev
                rev = c
                c = t
            return rev
        
        head = reverse(head)
        if n == 1:
            head = head.next
            return reverse(head)
        
        prev = c = head
        i = 1
        while True:
            if i == n:
                prev.next = c.next
                break
            prev = c
            c = c.next
            i += 1
        
        return reverse(head)








