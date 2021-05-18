#Zadanie 04
#przy użyciu pętli while wypisz liczby z przedziału <100,150>, pomijając te, które są podzielne przez 5 i 7.

#Użyj instrukcji continue.


x = 99

while x <= 150:
    x += 1
    if(x // 7 == x / 7 and x /5 == x //5):
        print("Nie wypisuje ", x)
        continue
    else:
        print(x)
