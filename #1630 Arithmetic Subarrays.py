class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        q = len(l)
        ans = []
        for i in range(q):
            sub_array = nums[l[i]:r[i]+1]

            sub_array.sort()
            flag = True
            for j in range(len(sub_array)-1):
                if sub_array[j+1]-sub_array[j] != sub_array[1]-sub_array[0]:
                    flag = False
                    break
            ans.append(flag)
        return ans
