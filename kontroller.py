import subprocess
import os
from lagring import  spara_servrar
from datetime import datetime


def kontrollera_server(server, servrar):

    if os.name == "nt":
        kommando = ["ping", "-n", "1", server["adress"]] #ping for windows
    else:
        kommando = ["ping", "-c", "1", server["adress"]] # ping for Linux

    try:
        svar= subprocess.run(
            kommando, #ping
            capture_output=True, #Return ping
            text=True, #The format being returned will be in text
            timeout=4
            )

        if svar.returncode == 0:
            server["status"] = "up"
        else:
            server["status"] = "down"

    except subprocess.TimeoutExpired:
        server["status"] = "down"

    server["senast_kontrollerad"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    spara_servrar(servrar)
    print(f"Server: {server['namn']} har status: {server['status']}")
    return server

def kontrollera_alla(servrar):
    for server in servrar:
        kontrollera_server(server, servrar)

    print("Samtliga servrar har kontrollerats.")

    for server in servrar:
        print(f"Server: {server['namn']}")
        print(f"Status: {server['status']}")
        print(f"Senast kontrollerad: {server['senast_kontrollerad']}")
    return servrar
