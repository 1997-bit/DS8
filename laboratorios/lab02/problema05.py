# Controlador Inteligente de Luminarias Públicas (Eco-LED)

lecturas_ecologicas = 0
suma_iluminacion = 0.0
contador_iluminacion = 0

while True:
    ldr = float(input("Ingrese la lectura del LDR (0.0 a 100.0) o -1.0 para salir: "))

    if ldr == -1.0:
        break

    if ldr < 0.0 or ldr > 100.0:
        print("Error: La lectura del LDR debe estar entre 0.0 y 100.0.")
        continue

    bateria = float(input("Ingrese el nivel de carga de la batería (0.0 a 100.0): "))

    if bateria < 0.0 or bateria > 100.0:
        print("Error: La batería debe estar entre 0.0 y 100.0.")
        continue

    if bateria < 20.0:
        brillo = 10.0
        lecturas_ecologicas += 1
    elif ldr < 40.0:
        brillo = 100.0 - ldr
        suma_iluminacion += brillo
        contador_iluminacion += 1
    else:
        brillo = 0.0

    print(f"Brillo calculado: {brillo:.1f}%")

if contador_iluminacion > 0:
    promedio = suma_iluminacion / contador_iluminacion
else:
    promedio = 0.0

print(f"Total de lecturas en modo ecológico: {lecturas_ecologicas}")
print(f"Promedio general de la energía de iluminación utilizada: {promedio:.2f}%")
