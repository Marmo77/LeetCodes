class Solution:
    #Polecenie:
    # masz 2 stringi a i b, zreturnuj ich sume jako binarny string
    
    #solution help -> https://www.youtube.com/watch?v=keuWJ47xG8g
    
    def addBinary(self, a: str, b: str) -> str:
        
        #dodawanie binarne polega na sumowaniu 0 i 1
        #przykład:
        #   100
        # +1101
        #------
        # 10001
        res = "" #wynik (result)
        carry = 0 # jest to liczba która zostaje przenoszona do następnepnego [i], podczas przechodzenia przez petle. Jesli  digitA = 1, digitB = 0 ale wczesniej bylo 1+1 = 2 to carry = 1, a char = 0 (czyli char zostaje nie ruszony, wpisujemy w [i] 0, a carry przenosi do następnego dodawania czyli tego digA i digB carry = 1 -> 1+0+1 = 2 wiec tutaj char = 0, carry = 1 i sie przenosi dalej itd. do konca funckji), 
        
        a, b = a[::-1], b[::-1] # idziemy poprostu od tylu reversed() stringa zamiast od przodu
        
        for i in range(max(len(a), len(b))): #max, ponieważ zeby nie bylo range limit, czyli przechodzi przez tą dłużsża wartość np. (a= 1010, b= 111) wybiera a, poniewaz jest dluzsze
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0 #rozwiązuje problem z tym że jeśli jest nie równo znaków to stawia zero, czyli jeśli a jest krótsze od b to zapuste miejsce [i] podstawia 0 czyli jesli jest (a = 11, b = 1) => b = 10
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0 # ord() convertuje string w int wiec jesli b[i] = "1" to inaczej ord("1") - ord("0") = 1: int
            print(digitA,digitB)
            
            total = digitA + digitB + carry
            char = str(total % 2) # jeśli wynik np. jest 0 to = 0, jeśli jest 1 % 2 = 0, jeśli jest 2, czyli chcemy aby sie przenioslo dalej i zotalo nam 0 to 2 % 2 = 0,
            # jeśli jest już np. 3 czyli przenosimy 1 dalej ale zostawiamy też 1 to 3 % 2 = 1 (rozwiązuje ten problem jeśli jest total > 2)
            res = char + res # robimy na odwrot dodajemy do przodu string'a.
            carry = total // 2
            #jeśli total =2, carry = 1, jeśli total = 1, carry = 0
        if carry:
            res = "1" +res
            
        return res
                
        
        
solution = Solution()
print(solution.addBinary("101", "10"))