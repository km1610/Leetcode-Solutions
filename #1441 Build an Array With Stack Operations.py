class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        array = []
        out = []
        ind=0
        for i in range(1,n+1):
            if len(array)==len(target):
                break
            array.append(i)
            out.append('Push')
            if target[ind]!=array[ind]:
                array.pop()
                out.append('Pop')
            else:
                ind+=1
        return out


        
