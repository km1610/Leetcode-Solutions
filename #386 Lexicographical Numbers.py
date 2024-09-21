class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        d = 0
        t = n

        while t:
            d += 1
            t = t//10

        def func(i):
            if i>n:
                return
            res.append(i)
            func(i*10)
            if i%10==9:
                return
            func(i+1)

        func(1)

        return res
