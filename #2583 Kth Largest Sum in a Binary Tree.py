# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if root:
        return 1 + max(height(root.left),height(root.right))
    return 0
  
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        h = height(root)
      
        if k>h:
            return -1
          
        sums = [0 for i in range(h)]
      
        def traverse(root, level):
            if root:
                sums[level] += root.val
                traverse(root.left, level+1)
                traverse(root.right, level+1)
              
        traverse(root, 0)
        sums.sort()
        return sums[-(k)]
