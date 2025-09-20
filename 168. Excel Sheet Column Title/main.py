# https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    
    # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def convertToTitle(self, columnNumber: int) -> str:
        # #co chce - ile razy trzeba bedzie znaków wsadzić, czyli ile razy przeszlismy przez alphabet. np. colN = 5, 0 razy przesliszmy czyli wynik bedzie 1, jesli np colN 32 = 1
        # signs_quanity = 0
        # if columnNumber // len(self.alphabet) > 0:
        #     signs_quanity = columnNumber // len(self.alphabet)
        # else:
        #     signs_quanity = columnNumber-1
            
        # if signs_quanity > 0:
        #     # dla ilosci ile jest signs quanity tyle trzeba popodstawiac
            
        # # print(signs_quanity)
        # # mając to teraz trzeba za tą długośc podstawiać literki alfabetu np. signs_quanity = 0, to bierzemy signs_quanity idx i wypisujemy do returna, jesli signs_quanity = 1, to bierzemy idx i zwracamy literke na tym idx'e ('B')
        
        # columnNumber = self.alphabet[signs_quanity]
        # return str(columnNumber)
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        # Tutaj tworzymy string zawierający cały alfabet – 26 znaków, od A do Z.
        # Dzięki temu możemy używać indeksów 0–25, aby wybierać konkretne litery.

        result = []  
        # Lista, do której będziemy dodawać litery (od końca do początku).
        # Używamy listy, bo dodawanie do niej jest łatwe, a na końcu złączymy ją w string.

        while columnNumber > 0:  
            # Pętla działa tak długo, aż "columnNumber" nie spadnie do 0.
            # W każdej iteracji obliczamy jedną literę (od końca do początku nazwy kolumny).

            columnNumber -= 1  
            # Odejmujemy 1, ponieważ w Excelu A = 1, a w indeksach stringa A = 0.
            # Dzięki temu wyrównujemy przesunięcie i możemy korzystać z indeksów 0–25.

            result.append(alphabet[columnNumber % 26])  
            # Obliczamy resztę z dzielenia "columnNumber % 26".
            # To mówi nam, którą literę wstawić (np. 0 → A, 25 → Z).
            # Następnie dodajemy tę literę do listy "result".

            columnNumber //= 26  
            # Dzielimy liczbę całkowitą przez 26.
            # To przesuwa nas "w lewo" – np. po obliczeniu ostatniej litery sprawdzamy,
            # czy jeszcze trzeba dodać kolejne (np. przy 28 → po "B" jeszcze zostaje "A").

        return "".join(reversed(result))  
        # Odwracamy kolejność listy "result", bo litery dodawaliśmy od końca (najmłodsza cyfra pierwsza).
        # Łączymy listę w jeden string i zwracamy go jako wynik.
                
sol = Solution()

#wrocic do tego kiedys samodzielnie (nieoddane na leet)

print(sol.convertToTitle(32))