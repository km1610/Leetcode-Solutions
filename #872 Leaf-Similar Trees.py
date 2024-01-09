# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getSequence(root, seq):
            if root==None:
                return seq
            if root.left==None and root.right==None:
                seq.append(root.val)
            else:
                seq = getSequence(root.left,seq)
                seq = getSequence(root.right,seq)
            return seq

        if getSequence(root1,[])==getSequence(root2,[]):
            return True
        return False

