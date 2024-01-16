# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse(root,l):
    if root!=None:
        l = traverse(root.left,l)
        l.append(root.val)
        l = traverse(root.right,l)
    return l

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l = []
        l.extend(traverse(root1,[]))
        l.extend(traverse(root2,[]))
        l.sort()
        return l
