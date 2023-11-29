# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(root):
    if root!=None:
        return 1 + max(height(root.left) ,height(root.right))
    return 0

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root!=None:
            if abs(height(root.left)-height(root.right))<=1:
                return True and Solution().isBalanced(root.right) and Solution().isBalanced(root.left)
            return False
        return True
