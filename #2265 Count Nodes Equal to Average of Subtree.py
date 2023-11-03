# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sumRoot(root):
    if root!=None:
        return root.val + sumRoot(root.left) + sumRoot(root.right)
    return 0

def countNodes(root):
    if root!=None:
        return 1 + countNodes(root.left) + countNodes(root.right)
    return 0

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if root!=None:
            s = sumRoot(root)
            c = countNodes(root)
            avg = s//c
            Bool = 0
            if avg == root.val:
                Bool=1
            return Bool + Solution().averageOfSubtree(root.left) + Solution().averageOfSubtree(root.right)
        return 0
        
