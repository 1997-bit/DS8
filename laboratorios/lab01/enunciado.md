# Laboratorio #1 — Fundamentos de Python
**Universidad Tecnológica de Panamá | FISC | Desarrollo de Software VIII**

---

## Problema 1 — Conversión Voltaje → Temperatura

**Contexto:** Microcontrolador lee voltaje analógico de sensor lineal. Rango: 0.0V = 0.0°C, 3.3V = 100.0°C.

**Requisitos:**
- `input()` → voltaje medido por consola
- Casting: `str` → `float`
- Fórmula: `Temperatura = (Voltaje * 100) / 3.3`
- Mostrar voltaje y temperatura con 2 decimales

**Ejemplo:**
```
>>> Ingrese el voltaje medido (0.0 a 3.3 V): 1.5
Voltaje de Entrada: 1.5 V
Temperatura Calculada: 45.45 °C
--- Ejecución finalizada con éxito ---
```

---

## Problema 2 — Clasificación de Temperatura de Sala

**Contexto:** Software para sala de servidores FISC que clasifica temperatura ambiental y emite alertas.

**Requisitos:**
- `input()` → temperatura en °C, convertir a `float`
- Estructura condicional:

| Condición | Estado | Acción |
|-----------|--------|--------|
| `temp <= 20.0` | Óptimo | Mantener ventilación normal |
| `20.0 < temp <= 25.0` | Advertencia | Activar ventilación auxiliar |
| `temp > 25.0` | Alarma Crítica (Peligro de Sobrecalentamiento) | Apagar servidores no esenciales e iniciar refrigeración máxima |

**Ejemplos:**
```
>>> Ingrese la temperatura de la sala (°C): 26.5
Estado: Alarma Crítica (Peligro de Sobrecalentamiento)
Acción: Apagar servidores no esenciales e iniciar refrigeración máxima

>>> Ingrese la temperatura de la sala (°C): 18.2
Estado: Óptimo
Acción: Mantener ventilación normal
```

---

## Problema 3 — Promedio de Lecturas de Humedad

**Contexto:** Nodo sensor agrícola en Coclé promedia lecturas de humedad de suelo para filtrar ruido físico.

**Requisitos:**
- Solicitar número total de lecturas (`int`)
- Acumular suma total
- Bucle iterativo → solicitar cada lectura (`float`, rango 0%–100%)
- Calcular y mostrar promedio con 1 decimal

**Ejemplo:**
```
>>> ¿Cuántas lecturas va a registrar?: 3
Ingrese la lectura de humedad #1 (%): 45.5
Ingrese la lectura de humedad #2 (%): 50.2
Ingrese la lectura de humedad #3 (%): 48.3
---------------------------------------------
Total de lecturas procesadas: 3
Humedad Promedio del Suelo: 48.0 %
```

---

## Problema 4 — Monitor de Nivel de Represa (Loop + Error Handling)

**Contexto:** Sensor ultrasónico monitorea nivel de agua continuamente. Sistema debe ser robusto a entradas inválidas y detenerse con comando seguro.

**Requisitos:**
- Loop infinito → `input()` nivel en metros o `'salir'`
- Si `'salir'` → mensaje de apagado seguro
- `try/except` → manejo de entradas no numéricas
- `nivel > 4.5m` → alerta de desbordamiento; si no → "Nivel estable"

**Ejemplo:**
```
>>> Ingrese el nivel de agua (m) o 'salir': 3.2
Nivel estable.

>>> Ingrese el nivel de agua (m) o 'salir': 4.8
¡ALERTA!: Nivel de agua crítico. Peligro de desbordamiento.

>>> Ingrese el nivel de agua (m) o 'salir': agua123
Error: Entrada no válida. Por favor ingrese un número decimal o escriba 'salir'.

>>> Ingrese el nivel de agua (m) o 'salir': salir
Apagando el sistema de monitoreo de represa...
--- Proceso finalizado de forma segura ---
```

---

## Entregable

Subir a Teams → carpeta `Laboratorios/laboratorio1/GrupoN` (ej. `Grupo1`, `Grupo2`, etc.)
