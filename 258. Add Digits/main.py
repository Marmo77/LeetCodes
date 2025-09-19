# problem: https://leetcode.com/problems/add-digits/description/?envType=problem-list-v2&envId=math

class Solution:
    def addDigits(self, num: int) -> int:
        
        # print(len(str(num)))
        
        # length_num = len(str(num))
        # print(length_num)
        
        # adding = num
        # finished = False
        # while finished != True: # do momentu gdy nie bedzie 1 digit
        #     for idx, nums in enumerate(str(num)):
        #         adding += int(nums)
                
        #         # response += 
        #     adding = adding-num
        #     finished = True    
        #     if len(str(adding)) > 1 :
        #         finished = False
        #     if len(str(adding)) == 0:
        #         print("JP")
        #         break
            # zrobic
            # o co chodzi?
            # do momentu gdy dlugosc num nie bedzie == 0 to powtarzaj petle tylko podmieniaj w for'ze num na wynik koncowy dodawania jesli np == 11, to do for'a wstaw ta 11 zamiast np, 38 poprzedniego itd od momentu gdy len(num) == 1 :D

            prev = num
            finished = False
            while finished != True:
                new_num = 0
                res = prev
                for idx in range(len(str(res))):
                    nums = str(res)[idx] 
                    new_num += int(nums)

                # print(new_num)

                if len(str(new_num)) > 1:
                    prev = new_num
                    continue
                else:
                    finished = True
                    return new_num

                
                
            # if len(str(res)) == 1:
            #     # print(res)
            #     print("FINISHED")
                
sol = Solution()
print(sol.addDigits(38))