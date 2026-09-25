"""
Laboratorio 4 - Grupo A | Rol: Nodo Emisor
Genera lecturas simuladas de 3 tipos de sensores y las guarda en un archivo JSON
para que el Grupo B (Gateway Receptor) pueda leerlas.

Formato JSON generado (coordinado para Grupo B):
{
  "nodo_emisor": str,
  "total_ciclos": int,
  "rangos_seguros": {...},
  "dispositivos": [
    {
      "id_dispositivo": str,      # ej: "TEMP-01"
      "tipo_sensor": str,         # "temperatura" | "humedad" | "presion"
      "unidad": str,              # "°C" | "%" | "hPa"
      "rango_seguro": {"min": x, "max": y},
      "lecturas": [
        {
          "ciclo": int,
          "valor": float,
          "estado": "normal" | "critica",  # identifica lectura fuera de rango
          "es_critica": bool,
          "timestamp": str
        }
      ]
    }
  ]
}
Rangos seguros definidos por Grupo A:
  - Temperatura: 10 a 35 °C
  - Humedad:     30 a 70 %
  - Presion:     980 a 1050 hPa
"""

import json
import random
from datetime import datetime

ARCHIVO_SALIDA = "lecturas_grupoA.json"

# --- Definicion de dispositivos (lista de diccionarios) ---
# Cada dispositivo representa un tipo de sensor distinto.
dispositivos = [
    {
        "id_dispositivo": "TEMP-01",
        "tipo_sensor": "temperatura",
        "unidad": "°C",
        "rango_seguro": {"min": 10.0, "max": 35.0},
        # Rango de generacion mas amplio para forzar lecturas criticas a veces
        "rango_generacion": {"min": 0.0, "max": 50.0},
        "lecturas": []
    },
    {
        "id_dispositivo": "HUM-01",
        "tipo_sensor": "humedad",
        "unidad": "%",
        "rango_seguro": {"min": 30.0, "max": 70.0},
        "rango_generacion": {"min": 0.0, "max": 100.0},
        "lecturas": []
    },
    {
        "id_dispositivo": "PRES-01",
        "tipo_sensor": "presion",
        "unidad": "hPa",
        "rango_seguro": {"min": 980.0, "max": 1050.0},
        "rango_generacion": {"min": 950.0, "max": 1080.0},
        "lecturas": []
    },
]


def es_critica(valor, rango_seguro):
    """Retorna True si el valor esta fuera del rango seguro."""
    return not (rango_seguro["min"] <= valor <= rango_seguro["max"])


def generar_lectura(dispositivo, ciclo):
    """Genera una lectura aleatoria para un dispositivo en un ciclo dado."""
    valor = round(random.uniform(
        dispositivo["rango_generacion"]["min"],
        dispositivo["rango_generacion"]["max"]
    ), 2)
    critica = es_critica(valor, dispositivo["rango_seguro"])
    return {
        "ciclo": ciclo,
        "valor": valor,
        "estado": "critica" if critica else "normal",
        "es_critica": critica,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def pedir_ciclos():
    """Solicita el numero de ciclos con validacion."""
    while True:
        try:
            cantidad = int(input("Numero de ciclos a ejecutar: ").strip())
            if cantidad <= 0:
                print("Debe ingresar un numero entero mayor que 0.")
                continue
            return cantidad
        except ValueError:
            print("Entrada invalida. Ingrese un numero entero.")
        except (EOFError, KeyboardInterrupt):
            print("\nEjecucion cancelada.")
            raise SystemExit(0)


def main():
    cantidad_ciclos = pedir_ciclos()

    print(f"\n--- Nodo Emisor iniciado: {cantidad_ciclos} ciclos ---")
    print(f"Dispositivos registrados: {len(dispositivos)}\n")

    # Bucle principal de ciclos
    for ciclo in range(1, cantidad_ciclos + 1):
        print(f"=== Ciclo {ciclo}/{cantidad_ciclos} ===")
        for disp in dispositivos:
            lectura = generar_lectura(disp, ciclo)
            disp["lecturas"].append(lectura)

            pendientes = cantidad_ciclos - ciclo
            marca = "CRITICA/FUERA DE RANGO" if lectura["es_critica"] else "normal"
            print(f"  [{disp['id_dispositivo']} | {disp['tipo_sensor']}] "
                  f"valor={lectura['valor']} {disp['unidad']} -> {marca} | "
                  f"Ciclos pendientes para este dispositivo: {pendientes}")
        print()  # linea en blanco entre ciclos

    # Estructurar datos finales (sin claves internas de generacion)
    datos_salida = {
        "nodo_emisor": "GrupoA-Nodo01",
        "total_ciclos": cantidad_ciclos,
        "fecha_generacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rangos_seguros": {
            d["tipo_sensor"]: d["rango_seguro"] for d in dispositivos
        },
        "dispositivos": [
            {
                "id_dispositivo": d["id_dispositivo"],
                "tipo_sensor": d["tipo_sensor"],
                "unidad": d["unidad"],
                "rango_seguro": d["rango_seguro"],
                "lecturas": d["lecturas"]
            }
            for d in dispositivos
        ]
    }

    # Guardar lista completa en JSON
    with open(ARCHIVO_SALIDA, "w", encoding="utf-8") as f:
        json.dump(datos_salida, f, indent=4, ensure_ascii=False)

    # Resumen final en consola
    print(f"Proceso finalizado. Datos guardados en '{ARCHIVO_SALIDA}'.")
    print("--- Resumen por dispositivo ---")
    for d in dispositivos:
        criticas = sum(1 for l in d["lecturas"] if l["es_critica"])
        normales = len(d["lecturas"]) - criticas
        print(f"  {d['id_dispositivo']} ({d['tipo_sensor']}): "
              f"{len(d['lecturas'])} lecturas | "
              f"{normales} normales | {criticas} criticas")


if __name__ == "__main__":
    main()
