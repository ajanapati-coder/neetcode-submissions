class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            sum = 0
            str_version = str(n)

            for i in range(len(str_version)):
                sum += int(str_version[i]) * int(str_version[i])
            
            if sum in seen:
                return False
            
            seen.add(sum)

            n = sum
        
        return True
            
            