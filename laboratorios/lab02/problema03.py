"""
Problema 3: Calibrador Dinámico de Deriva en Sensores de Presión
Contexto: Los sensores de presión industriales sufren descalibraciones temporales (deriva o 'drift'). El 
software de calibración debe leer de forma secuencial una serie de datos de prueba del sensor, calcular la 
desviación absoluta respecto al valor patrón de laboratorio y clasificar el lote.
Requisitos del Software:
 Establecer un bucle para registrar hasta 10 mediciones secuenciales del sensor.
 Definir el valor de referencia patrón, por ejemplo, 1013.25 hPa (Presión estándar).
 Para cada lectura ingresada (en hPa), calcular la desviación absoluta, esta se calcula de la siguiente
manera, a cada lectura se le resta la presión estándar (desviación absoluta individual).
 En caso una lectura individual presenta una desviación superior a 5.0 hPa con respecto a la referencia
patrón, el programa debe imprimir: '¡ADVERTENCIA!: Medición fuera de tolerancia'. De lo contrario imprimir
“Estado: Tolerancia Aceptable”.
 Al finalizar el ciclo, calcular la desviación promedio de todo el conjunto de lecturas. Clasificar el sensor: si el 
promedio de desviación absoluta supera los 3.0 hPa, imprimir un mensaje que indique: 'CLASIFICACIÓN: 
Sensor requiere Recalibración en Laboratorio'. De lo contrario, imprimir: 'CLASIFICACIÓN: Sensor 
Aprobado para Operación'.
Ejemplo de Entrada/Salida en Consola (Problema 3):
>>> Ingrese la medición de presión #1 (hPa): 1012.0
Desviación absoluta: 1.25 hPa | Estado: Tolerancia aceptable.
>>> Ingrese la medición de presión #2 (hPa): 1005.0
¡ADVERTENCIA!: Medición fuera de tolerancia. Desviación: 8.25 hPa
>>> Ingrese la medición de presión #3 (hPa): 1018.5
¡ADVERTENCIA!: Medición fuera de tolerancia. Desviación: 5.25 hPa
Universidad Tecnológica de Panamá | FISC | Desarrollo de Software VIII
Página 3
>>> Ingrese la medición de presión #4 (hPa): 1011.0
Desviación absoluta: 2.25 hPa | Estado: Tolerancia aceptable.
============= DIAGNÓSTICO DEL SENSOR =============
Desviación promedio del lote: 4.25 hPa
CLASIFICACIÓN: Sensor requiere Recalibración en Laboratorio.
"""
suma_desviaciones = 0
while True:
    lecturas = int(input("¿Cuántas mediciones de presión desea registrar? (máx. 10): "))
    if 1<= lecturas <=10:
            
            for i in range(1, lecturas + 1):
                presion_texto = input(f"Ingrese la medición de presión #{i} (hPa): ")
                presion = float(presion_texto)
                desviacion = abs(presion - 1013.25)
                if desviacion > 5.0:
                    print(f"¡ADVERTENCIA!: Medición fuera de tolerancia. Desviación: {desviacion:.2f} hPa")   
                else:
                    print(f"Desviación absoluta: {desviacion:.2f} hPa | Estado: Tolerancia aceptable.")
                suma_desviaciones += desviacion
            desviacion_promedio = suma_desviaciones / lecturas
            print("============= DIAGNÓSTICO DEL SENSOR =============")
            print(f"Desviación promedio del lote: {desviacion_promedio:.2f} hPa")
            if desviacion_promedio > 3.0:
                print("CLASIFICACIÓN: Sensor requiere Recalibración en Laboratorio.")
            else:
                print("CLASIFICACIÓN: Sensor Aprobado para Operación.")
    else:
            print("cantidad de lecturas no aceptadas")
    break

 
        