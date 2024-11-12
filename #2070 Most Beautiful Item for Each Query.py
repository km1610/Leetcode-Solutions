def search_nearest(price, prices):
    l, r = 0, len(prices)-1
    while l<r:
        mid = (l+r)//2
        if price>prices[mid] and price<prices[mid+1]:
            return prices[mid]
        if price>prices[mid]:
            l = mid+1
        if price<prices[mid]:
            r = mid
    return prices[l]

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        pb = defaultdict(int)

        for i in items:
            pb[i[0]] = max(pb[i[0]], i[1])

        prices = sorted(list(pb.keys()))

        for i in range(1,len(prices)):
            pb[prices[i]] = max(pb[prices[i]], pb[prices[i-1]])
        
        ans = []
        for i in queries:
            if i in pb:
                ans.append(pb[i])
            elif i<prices[0]:
                ans.append(0)
            else:
                p = search_nearest(i, prices)
                ans.append(pb[p])
        return ans
