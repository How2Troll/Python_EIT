#Zadanie 02
#Napisz program, który wczytuje dwie liczby całkowite reprezentujące numer dnia i numer miesiąca, a następnie zwraca nazwę pory roku dla podanych wartości
print("Podaj dzien miesiaca (1-31)")
day = int(input())
print("Podaj miesiac (1-12)")
month = int(input())

if(month == 12 and day >= 21 or month < 3 or month == 3 and day <= 20):
    print("To zima!")

elif(month == 3 and day >= 21 or month > 3 and month <  6  or month == 6 and day <= 20):
    print("To wiosna!")

elif(month == 6 and day >= 21 or month > 6 and month <  9 or month == 9 and day <= 21):
    print("To lato!")

elif(month == 9 and day >= 22 or month > 9 and month < 12 or month == 12 and day <= 20):
    print("To jesien!")

else:
    print("To mamy syf") #ewentualny blad z datami wynika z mojej glupoty przy granicach ale logika jest ok 
