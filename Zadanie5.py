#Zadanie 05
#Wypisz wszystkie liczby pierwsze z przedziału <2,10> wykorzystując instrukcję: for ... else lub while ... else. done 

#Użyj instrukcji break przy znalezieniu pierwszego dzielnika naturalnego innego niż 1 i dana liczba.
#W bloku else umieść informację o znalezieniu liczby pierwszej.
x = 1
while x < 10:
    x += 1
    check = 0
    for a in range(x):
        a += 1
        if( x/a == x//a):
            check += a
    if(check == x +1):
        print(x, "jest liczba pierwsza")    #totalnie zle jest to zadanie mozna je pewnie zrobic w 3 linijki, ale dziala 
