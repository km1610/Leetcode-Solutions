# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_string(root,l,s):
    if root!=None:
        s = chr(root.val+97) + s
        if root.left==None and root.right==None:
            l.append(s)
        else:
            l = get_string(root.left,l,s)
            l = get_string(root.right,l,s)
    return l

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        return min(get_string(root,[],""))
