class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) #dzieli i zwraca -1 czyli ostatni
    
solution = Solution()

print(solution.lengthOfLastWord("Hello World"))