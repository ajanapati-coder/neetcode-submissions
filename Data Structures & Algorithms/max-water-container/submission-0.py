class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        
        for i in range(len(heights)):
            left, right = i, len(heights) - 1

            while left < right:
                currWater = (right - left) * min(heights[left], heights[right])
                maxWater = max(maxWater, currWater)
                right -= 1
        
        return maxWater


        