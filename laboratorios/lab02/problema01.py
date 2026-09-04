alertas = 0

for n in range(1, 6):
    while True:
        try:
            temperatura = float(input(f"Ingrese la temperatura de la muestra #{n} (°C): "))
            break
        except ValueError:
            print("Error: Ingrese una temperatura válida.")

    while True:
        try:
            humedad = float(input(f"Ingrese la humedad relativa de la muestra #{n} (%): "))
            if 0.0 <= humedad <= 100.0:
                break
        except ValueError:
            print("Error: Ingrese la humedad correcta.")

    if temperatura > 30.0 and humedad > 75.0:
        print("¡ALERTA!: Ambiente crítico para hongo.")
        alertas += 1

print("============= REPORTE OPERATIVO FINAL =============")
print(f"Total de alertas críticas por hongo detectadas: {alertas}")

if alertas >= 3:
    print("ESTADO: Acción correctiva requerida (Activar extractor).")
else:
    print("ESTADO: Sistema Operando Estable.")