# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while(root or stack):
            while(root):
                # go to the left as much as possible
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if(k == 0):
                return root.val
            
            # when left is done we go to the right
            root = root.right