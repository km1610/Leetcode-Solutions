# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def addonerow(root,val,depth):
    if root!=None:
        if depth-1==1:
            node_l = TreeNode(val)
            node_r = TreeNode(val)
            l,r=root.left,root.right
            root.left=node_l
            root.right=node_r
            node_l.left=l
            node_r.right=r
        else:
            addonerow(root.left,val,depth-1)
            addonerow(root.right,val,depth-1)
        return root

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            node = TreeNode(val)
            node.left=root
            return node
        else:
            return addonerow(root,val,depth)
