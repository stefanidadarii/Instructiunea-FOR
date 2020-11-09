#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură).
a = eval(input("a = "))
b = eval(input("b = "))
for i in (range(a,b+1)):
    if i%2!=0: 
        print(i, end=' ')