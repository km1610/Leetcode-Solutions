class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = {}

        for i in arr:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            
            if count[i]>(len(arr)//4):
                return i
        return -1
        
