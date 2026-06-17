# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        node_map = {}
        while head.next:
            print(node_map)
            if node_map.get(head, None):
                print(node_map.get(head, None))
                return True
            else:
                node_map[head] = True
            head = head.next
        
        return False