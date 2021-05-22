#Zadanie 06
#Utwórz trzy klasy następujących obiektów: kwadrat, koło i trójkąt równoboczny.
#Dodajnty z kompone informacjami potrzebnymi do obliczenia obwodów i pól figur.
#Dodaj konstruktory dla poszczególnych klas, których argumentami będą wartości dla komponentów z punktu 2.
#Dodaj metody wyświetlające obliczone obwody i pola figur.

import math

class square:
    def __init__(self, bok):
        print("Mamy nowy kwadrat!")
        self.bok = bok

    def pole(self):
        print(self.bok*self.bok)
        return self.bok*self.bok

    def obwod(self):
        print(4*self.bok)
        return self.bok*4


class circle:
    def __init__(self, r):
        print("Mamy nowe kolo!")
        self.r = r
    def pole(self):
        print(math.pi * self.r *self.r)
        return math.pi * self.r *self.r
    def obwod(self):
        print(2*math.pi*self.r)
        return 2*math.pi*self.r



class equilateral_triangle:
    def __init__(self, bok):
        print("Mamy nowy trojkat rownoboczny!")
        self.bok = bok
    def pole(self):
        print(self.bok*self.bok*0.25*math.sqrt(3))
        return self.bok*self.bok*0.25*math.sqrt(3)
    def obwod(self):
        print(3*self.bok)
        return 3*self.bok


#program testowy
kwadrat = square(5)
kwadrat.pole()
kwadrat.obwod()

kolo = circle(2)
kolo.pole()
kolo.obwod()

trojkat = equilateral_triangle(10)
trojkat.pole()
trojkat.obwod()
