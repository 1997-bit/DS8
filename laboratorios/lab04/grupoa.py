import random
import json

datos = {
    "temp": [],
    "humedad": [],
    "presion": [] 
}

cantidad_ciclos = int(input("Num de ciclos a ejecutar"))


for a in range (cantidad_ciclos):

    print("agua")

    valor_t=random.randint(0,100)
    if valor_t < 40:
        datos["humedad"].append(valor_t)

        print(datos["temp"])

    valor_t=random.randint(0,100)
    if valor_t < 40:
        datos["temp"].append(valor_t)
        print(datos["temp"])

        valor_t=random.randint(0,100)
    if valor_t < 40:
        datos["temp"].append(valor_t)
        print(datos["temp"])