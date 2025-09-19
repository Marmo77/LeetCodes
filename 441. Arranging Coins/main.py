#problem : https://leetcode.com/problems/arranging-coins/description/?envType=problem-list-v2&envId=math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        staircase_lvl = 0
        if n == 1:
            return 1
        while n >= 0:
            staircase_lvl += 1
            n -= staircase_lvl
            # print(n)
            if n < 0:
                # print("POZIIOM",staircase_lvl)
                return staircase_lvl-1
                
            
        
    
sol = Solution()
print(sol.arrangeCoins(8))