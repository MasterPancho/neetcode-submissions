# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left_bound, right_bound):
            if not node:
                return True

            #Check that the boundaries are met. If not return false
            if not (node.val < right_bound and node.val > left_bound):
                return False
            
            #Left subtree must have a lesser value of its parent
            #Right subtree must have a greater value of its parent
            return(valid(node.left, left_bound, node.val) and valid(node.right, node.val, right_bound))


        return valid(root, float("-inf"), float("inf"))