# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if(not node):
                return 0
            
            current_sum = current_sum * 10 + node.val  # Update the current number
            
            if(not node.left and not node.right):  # If its a leaf node
                return current_sum
            
            left_sum = dfs(node.left, current_sum)   # Calculate sum for left subtree
            right_sum = dfs(node.right, current_sum) # Calculate sum for right subtree
            
            return(left_sum + right_sum)
        
        return dfs(root, 0)