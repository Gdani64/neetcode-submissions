# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # parent_val = float('-inf')
        good_nodes_counter = [0]
        def parse_good_nodes(root: TreeNode, parent_val) -> None:
            # print(parent_val)
            if root.val >= parent_val:
                good_nodes_counter[0] += 1
            if root.left:
                parse_good_nodes(root.left, max(root.val, parent_val))
            if root.right:
                parse_good_nodes(root.right, max(root.val, parent_val))
        
        parse_good_nodes(root, float('-inf'))
        
        return good_nodes_counter[0]
            

