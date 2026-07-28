class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            leftover = target - num

            if leftover in seen:
                return [seen[leftover] + 1, i + 1]

            seen[num] = i 
        