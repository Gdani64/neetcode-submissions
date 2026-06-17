from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([(root, float('-inf'), float('inf'))])
        
        while q:
            current, low, high = q.pop()
            if not (low < current.val < high):
                return False
            if current.right:
                q.append((current.right, current.val, high))
            if current.left:
                q.append((current.left, low, current.val))
        
        return True