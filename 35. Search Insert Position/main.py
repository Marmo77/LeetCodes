class Solution:
    def searchInsert(self, nums = [1,3,5,6], target = 5) -> int:
        for idx, num in enumerate(nums): # działa tak samo jak .map w react tylko ze na odwrot ze pierwszy jest index a pozniej numer ( przynajmniej jesli chodzi o tablice [] ) 
            
            if target == num: # jesli target jest taki samo jak numer przez który aktualnie przechodzi pętla
                print(f"Znaleizonon number: {num} o indexie {idx}")
                return idx
            elif target < num: # jeśli target jest mniejszy od numeru aktualnie sprawdzanego (logika że jeśli jest mniejszy od aktualnego elementu posortowanej listy to zwracamy index tego zeby tutaj mozna go bylo z'appendowac)
                return idx
            
        return len(nums) # jesli target jest wiekszy od wszystkich numerow to podaje ostatni index (dlugosc listy) (chodzi ze jest wiekszy od wszyskitch elementow wiec powinien byc na koncu)
            
        
solution = Solution()
solution.searchInsert()