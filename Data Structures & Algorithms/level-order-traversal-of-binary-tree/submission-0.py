# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        #BFS
        queue = deque([root])

        lst = [[root.val]]

        while(queue):
            sublist = []

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    sublist.append(node.left.val)

                if node.right:
                    queue.append(node.right)
                    sublist.append(node.right.val)

            if sublist != []:
                lst.append(sublist)    

        return(lst)
