# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        temp = None
        prev = None
        current = head
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

            # print("prev:{0}".format(prev.val))
            # print("temp:{0}".format(temp.val))
            # print("current:{0}".format(current.val))
        return prev
            # if current.val == 3:
                # print("current.next:{0}".format(current.next.val))
                # break



