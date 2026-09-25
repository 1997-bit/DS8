# Firewall Lógico de Mensajería para Redes IoT

bloqueados = 0

for i in range(1, 6):
    while True:
        protocolo = input(f">>> [Paquete #{i}] Ingrese protocolo (MQTT/HTTP/FTP): ").strip().upper()
        if protocolo in ("MQTT", "HTTP", "FTP"):
            break
        print("Error: Protocolo no válido. Ingrese MQTT, HTTP o FTP.")

    while True:
        try:
            puerto = int(input(f">>> [Paquete #{i}] Ingrese puerto de red: "))
            break
        except ValueError:
            print("Error: Ingrese un número entero válido para el puerto.")

    while True:
        try:
            payload = int(input(f">>> [Paquete #{i}] Ingrese tamaño del payload (bytes): "))
            break
        except ValueError:
            print("Error: Ingrese un número entero válido para el payload.")

    bloqueado = False

    if payload > 1024:
        bloqueado = True

    if protocolo == "HTTP":
        if puerto != 80:
            bloqueado = True
    elif protocolo == "FTP":
        puertos_validos_ftp = [20, 21, 22, 990]
        if puerto not in puertos_validos_ftp and not (1024 <= puerto <= 49151 and puerto != 3306):
            bloqueado = True
    elif protocolo == "MQTT":
        puertos_validos_mqtt = [1883, 8883, 443]
        if puerto not in puertos_validos_mqtt:
            bloqueado = True

    if bloqueado:
        print("[ACCIÓN]: BLOQUEADO")
        bloqueados += 1
    else:
        print("[ACCIÓN]: PERMITIDO")

print("\n============= SEGURIDAD DE RED IOT =============")
print(f"Total de paquetes bloqueados: {bloqueados} de 5")

if bloqueados >= 3:
    print("ESTADO DE LA RED: Alerta Roja, posible intrusión en proceso.")
else:
    print("ESTADO DE LA RED: Monitoreo Normal.")
