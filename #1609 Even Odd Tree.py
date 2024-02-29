# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def check_evenodd(root,level):
    if root!=None:
        if level%2==0:
            if root.val%2 == 1:
                return True and check_evenodd(root.left,level+1) and check_evenodd(root.right,level+1)
            return False
        else:
            if root.val%2==0:
                return True and check_evenodd(root.left,level+1) and check_evenodd(root.right,level+1)
            return False
    return True

def height(root):
    if root!=None:
        return 1 + max(height(root.left),height(root.right))
    return 0

def fetch_list(root,level,l):
    if root!=None:
        l[level].append(root.val)
        l = fetch_list(root.left,level+1,l)
        l = fetch_list(root.right,level+1,l)
    return l

def check_order(root,l):
    l = fetch_list(root,0,l)

    n = len(l)

    for i in range(n):
        m = len(l[i])
        if i%2==0:
            for j in range(m-1):
                if l[i][j]>=l[i][j+1]:
                    return False
        else:
            for j in range(m-1):
                if l[i][j]<=l[i][j+1]:
                    return False
    return True

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        check_even_odd = check_evenodd(root,0)
        h = height(root)
        check_order_levels = check_order(root,[[] for i in range(h)])

        print(check_even_odd)
        print(check_order_levels)
        if check_even_odd and check_order_levels:
            return True
        return False
        
