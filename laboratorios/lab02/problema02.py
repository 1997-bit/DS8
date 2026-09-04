
cosumoTotal = 0.0
costoTotal = 0.0

while True:
    nombreEquipo = input("Ingrese el nombre del electrodoméstico(o detener): ")
    
    if nombreEquipo == "detener":
        break

    consumoEquipo = float(input("Ingrese el consumo de potencia(watts): "))
    
    horasEstimadas = float(input("Ingrese las horas estimadas diarias(horas): "))

    kwh = (consumoEquipo * horasEstimadas)/1000

    if kwh > 2.5:
        kwhprecio = 0.18
        tipotarifa = "alta"
 
    else:
        kwhprecio = 0.12
        tipotarifa = "baja"

    preciofinal = kwhprecio * horasEstimadas 
    print(f"consumo acomulado:{kwh} kWh" + " | " +f"tu costo es + {preciofinal}" + " | "+ f"tarifa: + {tipotarifa}")

    cosumoTotal += kwh
    
    costoTotal += preciofinal

print("=====================SMART GRID REPORT ==================")
print(f"consumo total acomulado es: {cosumoTotal}" + " kWh" )

print(f"costo total acomulado es: ${costoTotal}" )
