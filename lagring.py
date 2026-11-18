from pathlib import Path
import csv
from datetime import datetime
import json
import os

def las_in_servrar():
    filnamn = Path(os.getenv("INVENTORY_DATAFIL", "servrar.json"))
    #checks if json-file exist
    if not filnamn.exists():
        return[]
    #read servers from json-file
    with open(filnamn, "r", encoding="utf-8") as fil:
        servrar= json.load(fil)

    return servrar


def exportera_som_csv(servrar):

    #Create "rapport" folder if it does not already exist
    Path("rapporter").mkdir(exist_ok=True)

    #Create filename with the current time and date
    tid = datetime.now().strftime("%Y%m%d%H%M%S")
    filnamn = "rapporter/inventering_" + tid + ".csv"


    with open(filnamn, "w", newline="", encoding="utf-8") as fil:
        server_csv = csv.writer(fil)

        server_csv.writerow([#Writing header for the csv file
            "namn",
            "adress",
            "miljo",
            "roll",
            "status",
            "senast_kontrollerad"
            ])
        #write servers in csv file as a row
        for server in servrar:
            server_csv.writerow([
                server["namn"],
                server["adress"],
                server["miljo"],
                server["roll"],
                server["status"],
                server["senast_kontrollerad"]
                ])
    print(f"Export till CSV-fil lyckades.: {filnamn}")
#saves the servers in json-file
def spara_servrar(servrar):
    filnamn = Path(os.getenv("INVENTORY_DATAFIL", "servrar.json"))

    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(servrar, fil, indent=5, ensure_ascii=False)