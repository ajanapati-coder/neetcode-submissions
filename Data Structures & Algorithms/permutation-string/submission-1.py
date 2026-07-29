class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1Count = {}
        windowCount = {}

        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        for i in range(len(s1)):
            windowCount[s2[i]] = windowCount.get(s2[i], 0) + 1
        
        if s1Count == windowCount:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            windowCount[s2[right]] = windowCount.get(s2[right], 0) + 1

            windowCount[s2[left]] -= 1
            if windowCount[s2[left]] == 0:
                del windowCount[s2[left]]
            left += 1

            if s1Count == windowCount:
                return True
        
        return False

                
