# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right_side_values = {}
        not_visited = [(root,0)]
        while not_visited:
            current,level = not_visited.pop()
            if not right_side_values.get(level, None):
                right_side_values[level] = current.val
            if current.left:
                not_visited.append((current.left, level + 1))
            if current.right:
                not_visited.append((current.right,level + 1))

        return list(right_side_values.values())
        