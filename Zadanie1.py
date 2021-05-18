print("Podaj temp w celcjuszach (np. 21C) lub Fahrenheitach (np. 37F)")
temp = input()
if("F" in temp):
    temp = temp[:-1] #usuwanie literki
    C = (int(temp) - 32) * 5/9 #zamiana C->f
    print("W celcjusazch:", C)
    print("W Fahrenheitach:", temp)


elif("C" in temp):
    temp = temp[:-1] #usuwanie litery
    F =  (int(temp) * 9/5) + 32 #zamian f->c
    print("W celcjusazch:", temp)
    print("W Fahrenheitach:", F)


else:
    print("THATS A WRONG NUMBER~!")
