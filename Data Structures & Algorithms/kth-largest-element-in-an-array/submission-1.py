class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kthLargest = 0

        while k:
            kthLargest = max(nums)
            nums.remove(kthLargest)
            k -= 1
        
        return kthLargest