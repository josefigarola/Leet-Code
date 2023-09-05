# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(not root):
            return

        while(root):
            print(root.val)
            if(root.left):
                # Find the rightmost node in the left subtree
                rightmost = root.left
                #print('rightmost',rightmost.val)
                while(rightmost.right):
                    rightmost = rightmost.right
                
                # Connect the rightmost node's right pointer to root's right subtree
                rightmost.right = root.right
                #print('rightmost.right',rightmost.right.val)
                
                # Move the entire left subtree to the right
                #print('root.left',root.left.val)
                root.right = root.left
                root.left = None
            
            # Move to the next node in the flattened structure
            root = root.right