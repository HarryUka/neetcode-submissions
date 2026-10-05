class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1 
        right = max(piles)
        res = right 


        def hours_to_eat(hr):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/hr)
            return hrs 


        while left <= right :
            mid = (left + right)// 2 
            hours = hours_to_eat(mid)
            if hours <= h:
                res = min(res,mid)
                right = mid - 1
            else:
                left = mid + 1
        return res 
                
        