# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def listnodes(root,l):
    if root!=None:
        l.append(root.val)
        l = listnodes(root.left,l)
        l = listnodes(root.right,l)
    return l

def substree(root,hashmap):
    if root!=None:
        root.val = hashmap[root.val]
        substree(root.left,hashmap)
        substree(root.right,hashmap)

class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:

        nodes = listnodes(root,[])

        nodes.sort()

        hashmap = {}

        for i in range(len(nodes)):
            hashmap[nodes[i]] = sum(nodes[i::])

        substree(root,hashmap)

        return root
