# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = [head]
        while head.next:
            prev.append(head.next)
            head = head.next
        print(prev)
        head = prev.pop()
        new_head = head
        while len(prev) > 0:
            last_node = prev.pop()
            last_node.next = None
            head.next = last_node
            print(head)
            head = head.next
            print(head)
        
        return new_head

