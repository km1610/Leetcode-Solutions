# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getnums(root,nums,num):
    if root!=None:
        num = num + str(root.val)
        if root.left==None and root.right==None:
            nums.append(num)
            return nums
        nums = getnums(root.left,nums,num)
        nums = getnums(root.right,nums,num)
    return nums

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = getnums(root,[],'')
        s = 0
        for i in nums:
            s+= int(i)
        return s
