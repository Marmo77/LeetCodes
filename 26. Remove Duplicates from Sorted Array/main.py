# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        no_duplicate_array = []
        
        for idx, num in enumerate(nums):
            # print(idx, num)
            
            # no_duplicate_array += str(num)
            # print(no_duplicate_array[idx])
            if idx < len(nums):
                # print(idx, num)
                no_duplicate_array+= str(num)
                if no_duplicate_array[idx-1] != num:
                    print(num)
                # jeśli numer akutalny jest taki sam jak poprzedni to pomiń ten punkt

                    
                
            
        
        
        print(no_duplicate_array)
        # return len(no_duplicate_array)
        
        
solution = Solution()

print(solution.removeDuplicates([1,1,2]))