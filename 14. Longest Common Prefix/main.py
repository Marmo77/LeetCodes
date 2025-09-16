# https://leetcode.com/problems/length-of-last-word/solutions/7193099/length-of-last-word-finder/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0] # zakladamy ze pierwszy element jest prefixem
        
        for s in strs[1:]: # iteracja bez pierwszego, poniewaz pierwszy zakladamy ze jest calym prefixem
            while not s.startswith(prefix):
                # print(prefix)
                prefix = prefix[:-1] #odcinamy ostatni znak do momentu gdy nie bedzie taki sam
                if not prefix:
                    #czyli zaden znak nie jest prefixem zwracamy pusty string
                    return ""
        return prefix
                
        
        
solution = Solution()

print(solution.longestCommonPrefix(["flower","flow","flight"]))