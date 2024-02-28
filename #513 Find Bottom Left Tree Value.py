# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if root!=None:
        return 1 + max(height(root.left),height(root.right))
    return 0

def dfs(root,level,height):
    if root!=None:
        if level==height:
            return root.val
        l = dfs(root.left,level+1,height)
        r = dfs(root.right,level+1,height)
        if l!=None:
            return l
        elif r!=None:
            return r
    return None
        
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        h = height(root)
        return dfs(root,1,h)

        
