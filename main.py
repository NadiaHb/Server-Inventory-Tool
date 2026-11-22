from meny import kor_meny, visa_alla, visa_miljospecifik
from lagring import las_in_servrar, exportera_som_csv
from kontroller import kontrollera_server, kontrollera_alla
import argparse
import sys

def main():

    #Creating arguments for terminal
    parser = argparse.ArgumentParser(
        description="Server Inventory Tool"
    )

    parser.add_argument(
        "--lista",
        help="Visa servrar",
        action="store_true"
    )
    parser.add_argument(
        "--miljo",
        help="Visa miljöspecifik server"
    )
    parser.add_argument(
        "--kontrollera-alla",
        action="store_true",
        help="Kontrollera alla servrar"
    )
    parser.add_argument(
        "--kontrollera",
        help="Kontrollera en server"
    )
    parser.add_argument(
        "--export",
        action="store_true",
        help="Exportera server som csv"
    )
    args = parser.parse_args()
    servrar = las_in_servrar()#reads servers from the JSON file

    if args.miljo: #Show servers in specifik enviroment
            visa_miljospecifik(servrar, args.miljo)

    elif args.lista: #Checking all servers
        visa_alla(servrar)

    elif args.kontrollera: #Checking only one server
        hittad = False

        for server in servrar:
            if server["namn"] == args.kontrollera:
                kontrollera_server(server, servrar)
                hittad = True
                if server["status"] == "down":

                    sys.exit(1)
                break

        if not hittad:
            print("Server hittades ej")
            sys.exit(1)

    elif args.kontrollera_alla:#Checking all servers
        kontrollera_alla(servrar)

        for server in servrar:
            if server["status"] == "down":
                sys.exit(1)

    elif args.export:#Exporting servers to CSV
        exportera_som_csv(servrar)

    else:
        kor_meny(servrar) #To start the menu with no arguments

if __name__ == "__main__":
    main()