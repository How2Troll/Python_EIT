#Zadanie 03
#Przy użyciu pętli for i funkcji range() napisz program, który dla podanego słowa wypisze je w odwrotnej kolejności.

print("Podaj slowo")   
REKIN = input() 
back = ""
for i in REKIN:
    back = i +back 
    print(back)
    
print(back)
