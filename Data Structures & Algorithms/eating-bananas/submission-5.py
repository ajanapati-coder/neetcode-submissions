class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int: 
        left, right = 1, max(piles) + 1
        result = right

        while left <= right:
            mid = (right + left) // 2

            currTime = 0
            for pile in piles:
                currTime += math.ceil(pile/mid)
            
            if currTime <= h:
                result = mid
                right = mid -1
            else:
                left = mid + 1
        
        return result