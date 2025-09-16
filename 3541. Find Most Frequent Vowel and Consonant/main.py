class Solution:
    
    vowel = "aeiou"
    frequency_arr = []
    
    def maxFreqSum(self, s: str) -> int:
        # ZADANIE WYDAWALO SIE O WIELE PROSTRZE NIZ SIE OKAZALO, CHCIALEM ZROBIC w [[]] ale skonczylem na pomycy AI i zrobione z dictionary -> {}
        frequency_dict = {}
        for char in s:
            # print(char)
            if char not in frequency_dict:
                frequency_dict[char] = 1
                # print(frequency_dict)
            else:
                frequency_dict[char] +=1
        print(frequency_dict)
        
        max_vowel = 0
        max_consonant = 0
        
        for char,freq in frequency_dict.items():
            if char in self.vowel:
                max_vowel = max(max_vowel,freq)
            else:
                max_consonant = max(max_consonant,freq)
                
        result = max_vowel + max_consonant
        return result
                
solution = Solution()

solution.maxFreqSum("successes")

# PROBA samodzielna
        # count= 0
        # for i in range(len(s)):
        #     if s[i] not in self.frequency_arr: 
        #         self.frequency_arr.append(s[i])
        #     else:
        #         lb = count = count + 1
        #         print(f"jest juz {s[i]}, po raz {lb}")
        #         for char in self.frequency_arr:
                    
                
            
        # print(self.frequency_arr)
        
        # for j in self.frequency_arr:
        #     # print(j)
        #     print(f"Częstotliwość {j} wynosi: ")