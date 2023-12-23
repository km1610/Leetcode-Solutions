class Solution:
    def isPathCrossing(self, path: str) -> bool:
        covered = {(0,0):0}
        x=y=0
        i=0
        n=len(path)
        while i<n:
            if path[i]=='N':
                y+=1
            elif path[i]=='S':
                y-=1
            elif path[i]=='E':
                x+=1
            else:
                x-=1


            if (x,y) in covered:
                return True
            covered[(x,y)] = i+1
            i+=1
            
        return False

    
