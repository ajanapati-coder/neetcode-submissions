class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        maxLen = 0

        for i in range(len(s)):
            left = right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left: right + 1]) > maxLen:
                    result = s[left: right + 1]
                    maxLen = right + 1 - left
                left -= 1
                right += 1
           
            left, right = i, i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left: right + 1]) > maxLen:
                    result = s[left: right + 1]
                    maxLen = right + 1 - left
                left -= 1
                right += 1
        
        return result

        
        