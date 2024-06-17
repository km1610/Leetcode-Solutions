class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = set()
        sqrt = int(c**(0.5))+1
        for i in range(sqrt):
            squares.add(i**2)
        for i in range(sqrt):
            target = c - (i**2)
            if target in squares:
                return True
        return False
