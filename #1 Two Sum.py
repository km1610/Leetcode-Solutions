class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {} #to save the remaining target in the hashmap
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in hash: #check if remaining target is in hashmap
                return [i,hash[temp]]
            hash[nums[i]] = i #save the key value pair as remaining target and their index
