from math import ceil
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # find where is the half of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val)
        second_half_start = slow.next # val=8
        slow.next = None

        # reverse second list
        c = second_half_start
        rev = None
        while c:
            n = c.next
            c.next = rev
            rev = c
            c = n
        # print(rev.val,rev.next.val)

        # merge lists
        list1 = head
        list2 = rev
        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1, list2 = tmp1, tmp2



        
            




