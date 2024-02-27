# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if root!=None:
        return 1+max(height(root.right),height(root.left))
    return 0

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root!=None:
            right = height(root.right)
            left = height(root.left)
            if left==0:
                left=-1
            if right==0:
                right=-1

            return max(height(root.right)+height(root.left),self.diameterOfBinaryTree(root.right),self.diameterOfBinaryTree(root.left))
        return 0
