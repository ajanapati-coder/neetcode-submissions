class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        bestLength = 0

        for num in nums:
            currLength = 1

            if num - 1 not in numSet:
                while num + 1 in numSet:
                    num += 1
                    currLength += 1 
            
            bestLength = max(currLength, bestLength)
        
        return bestLength
            
        