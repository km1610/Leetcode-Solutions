# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root!=None:
            if root.left==None and root.right==None:
                if root.val==1:
                    return True
                return False
            else:
                l = self.evaluateTree(root.left)
                r = self.evaluateTree(root.right)
                if root.val == 2:
                    return l or r
                return l and r
