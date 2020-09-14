from ValueArray import ValueArray

lista = ValueArray()

numIntervalos = int(input("numero de intervalos: "))

i = 0
while i < numIntervalos:
    lista.values.append(int(input("Intervalo #"+str(i+1)+": ")))
    i+=1

lista.CreateTable()

print("Mark | Freq ")
i = 0 
while i < len(lista.tableFreq):
    print(str(lista.tableFreq[i].Mark)+"|"+ str(lista.tableFreq[i].Freq))
    i+=1

print("Moda: "+str(lista.CalcularModa()))
print("Media: "+str(lista.CalcularMedia()))
print("Mediana: "+str(lista.CalcularMediana()))
print("Varianza: "+str(lista.CalcularVarianza()))
print("Desviacion Estandar: "+str(lista.CalcularDesviacionEstandar()))

