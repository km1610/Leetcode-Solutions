class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        curr_depth = 0
        o = False
        for i in s:
            if i=="(":
                if not o:
                    o=True
                curr_depth+=1
            elif i==")":
                depth=max(depth,curr_depth)
                curr_depth-=1
                if curr_depth==0:
                    o=False
        return depth
                    
        
