# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if postorder:
            if postorder[-1] in inorder:
                root = TreeNode(postorder[-1])
                n = len(postorder)
                pivot = inorder.index(postorder[-1])
                x = len(postorder[pivot::])
                root.right = self.buildTree(inorder[pivot+1::],postorder[n-x:n-1])
                root.left = self.buildTree(inorder[:pivot],postorder[:n-x])
                return root
        return None
