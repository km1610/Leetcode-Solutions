class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1

        while l<=r:
            mid = (l+r)//2

            if letters[mid] < target:
                l = mid + 1
            if letters[mid] == target:
                l = mid + 1
            if letters[mid] > target:
                if mid>0:
                    if letters[mid-1] > target:
                        r = mid-1
                    else:
                        return letters[mid]
                else:
                    return letters[mid]


        return letters[0]
