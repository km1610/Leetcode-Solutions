# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_max(root, val):
    if root!=None:
        return max(abs(val - root.val),find_max(root.right,val),find_max(root.left,val))
    return -100000

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root!=None:
            v = max(find_max(root.left,root.val),find_max(root.right,root.val))
            return max(v,self.maxAncestorDiff(root.left),self.maxAncestorDiff(root.right))
        return -100000
