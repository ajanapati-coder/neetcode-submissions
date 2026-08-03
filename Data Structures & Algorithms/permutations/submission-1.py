class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(used, current):
            if len(current) == len(nums):
                result.append(current.copy())
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                
                used.add(i)
                current.append(nums[i])
                backtrack(used, current)
                current.pop()
                used.remove(i)
        
        backtrack(set(), [])
        return result


            