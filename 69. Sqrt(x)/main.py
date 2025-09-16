
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1,x+1):
            if i*i == x: 
                return i
                # example: x = 8
                # i = 1, if 1*1 = 1 not equal or greater then 8
                # i = 2, if 2*2 = 2 not equal or greater then 8
                # i = 3, if 3*3 = greater then 8 \/ 
            elif i*i > x:
                # is greater then 8, so 3-1 = 2.828... but we round it down to nearest int.
                return i-1
                
        return 0
        
        
solution = Solution()

print(solution.mySqrt(8))

