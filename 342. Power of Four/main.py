# pytanie :https://leetcode.com/problems/power-of-four/description/?envType=problem-list-v2&envId=math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        if n == 1:
            return True
        if n <= 0 or n % 4 != 0:
            return False
        while n % 4 == 0:
            n = n / 4
        print(n)
        if n==1:
            return True
        else:
            return False

        # return self.isPowerOfFour(n // 4)
        
        
sol = Solution()

print(sol.isPowerOfFour(17))