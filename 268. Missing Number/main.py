
#problem: https://leetcode.com/problems/missing-number/
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #moje podejscie:
        # przyklad
        # Input: nums = [3,0,1]
        #są 3 numery, wiec numery musza byc w range [0,3] if nie ma to return brakujaca
        # brakujacy bedzie ten ktory nie pojawia sie w tym range'u.
        for num in range(0,len(nums)+1): #dla kazdej liczby od range [0, x] x => długość tabeli + 1
            if num not in nums: # jeśli liczba aktualnie sprawdzana nie znajduje się w range[0, x], jest to brakujaca liczba
                return num #zwraca brakującą liczbę
            
        #nie jest to najoptymalniejsze podejscie ale poprawyn tok myslenia :D
            
sol = Solution()

print(sol.missingNumber([3,0,1]))