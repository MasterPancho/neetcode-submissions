# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #Recursive DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))

    #BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        level = 0
        queue = deque([root])

        while(queue):

            for i in range(len(queue)):
                node = queue.popleft()
                
                if node.left != None:
                    queue.append(node.left)

                if node.right != None:
                    queue.append(node.right)

            level += 1
        
        return(level)
    