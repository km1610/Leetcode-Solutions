# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            if preorder[0] in inorder:
                root = TreeNode(preorder[0])
                n = len(preorder)
                pivot = inorder.index(preorder[0])
                x = len(inorder[pivot::])
                root.right = self.buildTree(preorder[n-x+1::],inorder[pivot+1::])
                root.left = self.buildTree(preorder[1:n-x+1],inorder[:pivot])
                return root
        return None
        
