class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ""
        for i in s:
            nums += str(ord(i)-96)
        for i in range(k):
            s = 0
            for j in nums:
                s+=int(j)
            
            nums = str(s)
        return int(nums)
