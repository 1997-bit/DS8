# Laboratorio #2
**Universidad Tecnológica de Panamá | FISC | Desarrollo de Software VIII**

---

## Problema 1: Simulador de Invernadero Inteligente

**Contexto:** Automatizar un invernadero agrícola mediante monitoreo cíclico de temperatura y humedad ambiental. Adquirir lote fijo de mediciones, analizar niveles seguros del cultivo y consolidar reporte operativo final.

### Requisitos del Software

- Solicitar al operador hasta **5 muestras de telemetría**. Cada muestra: temperatura (°C) y humedad relativa (0–100%).
- Si `temperatura > 30.0°C` **Y** `humedad > 75.0%` → imprimir alerta inmediata:
  ```
  ¡ALERTA!: Ambiente crítico para hongo.
  ```
- Llevar registro acumulado de alertas críticas.
- Al finalizar, mostrar reporte con total de alertas.
  - Si `alertas >= 3` → imprimir: `ESTADO: Acción correctiva requerida (Activar extractor).`
  - Si no → imprimir: `ESTADO: Sistema Operando Estable.`

### Ejemplo de Entrada/Salida

```
>>> Ingrese la temperatura de la muestra #1 (°C): 28.5
>>> Ingrese la humedad relativa de la muestra #1 (%): 60.0
>>> Ingrese la temperatura de la muestra #2 (°C): 32.5
>>> Ingrese la humedad relativa de la muestra #2 (%): 80.0
¡ALERTA!: Ambiente crítico para hongo.
>>> Ingrese la temperatura de la muestra #3 (°C): 25.0
>>> Ingrese la humedad relativa de la muestra #3 (%): 55.0
>>> Ingrese la temperatura de la muestra #4 (°C): 31.0
>>> Ingrese la humedad relativa de la muestra #4 (%): 82.0
¡ALERTA!: Ambiente crítico para hongo.
>>> Ingrese la temperatura de la muestra #5 (°C): 33.0
>>> Ingrese la humedad relativa de la muestra #5 (%): 78.0
¡ALERTA!: Ambiente crítico para hongo.

============= REPORTE OPERATIVO FINAL =============
Total de alertas críticas por hongo detectadas: 3
ESTADO: Acción correctiva requerida (Activar extractor).
```

---

## Problema 2: Analizador de Consumo en Smart Grid

**Contexto:** Simular carga de electrodomésticos en red eléctrica inteligente, calcular costo bajo tarifa escalonada y finalizar registro de forma segura.

### Requisitos del Software

- Bucle continuo.
- Fórmula de consumo: `kWh = (Watts × horas) / 1000`
- Por iteración, solicitar:
  - Nombre del electrodoméstico (o `'detener'` para finalizar)
  - Potencia (float, Watts)
  - Horas de uso diario (float)
- Tarifa escalonada:
  - `kWh > 2.5` → Tarifa Alta: **$0.18/kWh**
  - `kWh <= 2.5` → Tarifa Regular: **$0.12/kWh**
- Imprimir consumo y costo individual por equipo.
- Al detener: mostrar consumo total acumulado y costo total acumulado.

### Ejemplo de Entrada/Salida

```
>>>> Ingrese el nombre del electrodoméstico (o 'detener'): Refrigeradora
>>> Ingrese consumo de potencia (Watts): 350
>>> Ingrese horas estimadas de uso diario (horas): 24
Consumo calculado: 8.40 kWh | Tarifa: Alta ($0.18/kWh) | Costo: $1.512

>>>> Ingrese el nombre del electrodoméstico (o 'detener'): Bombillo LED
>>> Ingrese consumo de potencia (Watts): 12
>>> Ingrese horas estimadas de uso diario (horas): 10
Consumo calculado: 0.12 kWh | Tarifa: Regular ($0.12/kWh) | Costo: $0.014

>>>> Ingrese el nombre del electrodoméstico (o 'detener'): detener

================ SMART GRID REPORT ================
Consumo Total Acumulado: 8.52 kWh
Costo Total Acumulado Estimado: $1.53
```

---

## Problema 3: Calibrador Dinámico de Deriva en Sensores de Presión

**Contexto:** Leer serie de datos de prueba de sensor de presión, calcular desviación absoluta respecto a valor patrón de laboratorio y clasificar el lote.

### Requisitos del Software

- Bucle para hasta **10 mediciones secuenciales**.
- Referencia patrón: **1013.25 hPa** (presión estándar).
- Por lectura: `desviación_abs = |lectura - 1013.25|`
- Si `desviación > 5.0 hPa` → imprimir:
  ```
  ¡ADVERTENCIA!: Medición fuera de tolerancia.
  ```
  Si no → imprimir: `Estado: Tolerancia Aceptable.`
- Al finalizar: calcular desviación promedio del lote.
  - Si `promedio > 3.0 hPa` → `CLASIFICACIÓN: Sensor requiere Recalibración en Laboratorio.`
  - Si no → `CLASIFICACIÓN: Sensor Aprobado para Operación.`

### Ejemplo de Entrada/Salida

```
>>> Ingrese la medición de presión #1 (hPa): 1012.0
Desviación absoluta: 1.25 hPa | Estado: Tolerancia aceptable.
>>> Ingrese la medición de presión #2 (hPa): 1005.0
¡ADVERTENCIA!: Medición fuera de tolerancia. Desviación: 8.25 hPa
>>> Ingrese la medición de presión #3 (hPa): 1018.5
¡ADVERTENCIA!: Medición fuera de tolerancia. Desviación: 5.25 hPa
>>> Ingrese la medición de presión #4 (hPa): 1011.0
Desviación absoluta: 2.25 hPa | Estado: Tolerancia aceptable.

============= DIAGNÓSTICO DEL SENSOR =============
Desviación promedio del lote: 4.25 hPa
CLASIFICACIÓN: Sensor requiere Recalibración en Laboratorio.
```

---

## Problema 4: Firewall Lógico de Mensajería para Redes IoT

**Contexto:** Simular inspección de cabeceras de paquetes entrantes en Gateway de seguridad, aplicar reglas de filtrado y evaluar nivel de amenaza de la sesión.

### Requisitos del Software

- Bucle para inspeccionar **5 mensajes consecutivos**.
- Por paquete, solicitar: protocolo (`MQTT`/`HTTP`/`FTP`), tamaño del payload (bytes), puerto de red.
- Reglas de bloqueo:

| Protocolo | Condición de BLOQUEO |
|-----------|----------------------|
| HTTP | Puerto ≠ 80 |
| FTP | Puerto no es 20, 21, 22, 990, ni rango 1024–49151 (excl. 3306) |
| MQTT | Puerto no es 1883, 8883, ni 443 |
| Cualquiera | Payload > 1024 bytes |

- Imprimir por paquete: `[ACCIÓN]: BLOQUEADO` o `[ACCIÓN]: PERMITIDO`.
- Llevar registro de paquetes bloqueados.
- Al finalizar:
  - Si `bloqueados >= 3` → `ESTADO DE LA RED: Alerta Roja, posible intrusión en proceso.`
  - Si no → `ESTADO DE LA RED: Monitoreo Normal.`

### Ejemplo de Entrada/Salida

```
>>> [Paquete #1] Ingrese protocolo (MQTT/HTTP/FTP): HTTP
>>> [Paquete #1] Ingrese puerto de red: 8080
>>> [Paquete #1] Ingrese tamaño del payload (bytes): 512
[ACCIÓN]: BLOQUEADO

>>> [Paquete #2] Ingrese protocolo (MQTT/HTTP/FTP): MQTT
>>> [Paquete #2] Ingrese puerto de red: 1883
>>> [Paquete #2] Ingrese tamaño del payload (bytes): 128
[ACCIÓN]: PERMITIDO

>>> [Paquete #3] Ingrese protocolo (MQTT/HTTP/FTP): FTP
>>> [Paquete #3] Ingrese puerto de red: 21
>>> [Paquete #3] Ingrese tamaño del payload (bytes): 64
[ACCIÓN]: BLOQUEADO

>>> [Paquete #4] Ingrese protocolo (MQTT/HTTP/FTP): HTTP
>>> [Paquete #4] Ingrese puerto de red: 80
>>> [Paquete #4] Ingrese tamaño del payload (bytes): 2048
[ACCIÓN]: BLOQUEADO

>>> [Paquete #5] Ingrese protocolo (MQTT/HTTP/FTP): MQTT
>>> [Paquete #5] Ingrese puerto de red: 1883
>>> [Paquete #5] Ingrese tamaño del payload (bytes): 256
[ACCIÓN]: PERMITIDO

============= SEGURIDAD DE RED IOT =============
Total de paquetes bloqueados: 3 de 5
ESTADO DE LA RED: Alerta Roja, posible intrusión en proceso.
```

---

## Problema 5: Controlador Inteligente de Luminarias Públicas (Eco-LED)

**Contexto:** Luminarias urbanas regulan brillo dinámicamente según sensor LDR y % de batería solar. Sistema evalúa eficiencia energética en ciclo continuo.

### Requisitos del Software

- Bucle indefinido (termina con LDR = `-1.0`).
- Por iteración: solicitar LDR (0.0–100.0%) y nivel de batería (0.0–100.0%).
- Reglas de brillo:

| Condición | Brillo |
|-----------|--------|
| Batería < 20% | 10% (Modo Eco) |
| Batería >= 20% y LDR < 40% (oscuridad) | `100% - LDR` |
| Batería >= 20% y LDR >= 40% (día) | 0% (Apagado) |

- Contabilizar: total de lecturas en **modo ecológico**.
- Calcular: promedio de energía utilizada (excluir modo eco y lecturas de día).
- Mostrar resumen al finalizar.

### Ejemplo de Entrada/Salida

```
>>> Ingrese Lectura del LDR (0.0 a 100.0) o -1.0 para salir: 30.0
Ingrese nivel de carga de la batería (%): 85.0
[MODO NORMAL] Brillo de LED calculado: 70.0%

>>> Ingrese Lectura del LDR (0.0 a 100.0) o -1.0 para salir: 45.0
Ingrese nivel de carga de la batería (%): 15.0
[MODO ECO ACTIVADO] Batería baja (<20%). Brillo forzado al 10.0%.

>>> Ingrese Lectura del LDR (0.0 a 100.0) o -1.0 para salir: 55.0
Ingrese nivel de carga de la batería (%): 90.0
[DÍA DETECTADO] Brillo de LED calculado: 0.0% (Apagado).

>>> Ingrese Lectura del LDR (0.0 a 100.0) o -1.0 para salir: -1.0

============= SIMULACIÓN FINALIZADA =============
Lecturas totales en modo ecológico: 1
Energía utilizada de iluminación promedio: 70.0%
```
