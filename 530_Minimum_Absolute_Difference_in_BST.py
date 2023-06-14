# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def InOrder(self,node):
        if(node is None):
            return

        # Check left side of BST from the leaf to the root
        self.InOrder(node.left)

        if(self.prev is not None):
            #print('prev val ',self.prev.val, 'node val, ',node.val)
            # Get the difference between the prev node and actual node
            abs_diff = abs(node.val - self.prev.val)
            #print('abs', abs_diff, 'diff ',self.diff)
            self.diff = min(self.diff, abs_diff)
            #print('min diff ',self.diff)

        self.prev = node

        # Check the right side of BST
        self.InOrder(node.right)
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        # start the min difference with large value
        self.diff = float('inf')

        self.InOrder(root)
        return self.diff
        