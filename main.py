from meny import kor_meny, visa_alla, visa_miljospecifik, kontrollera_en
from lagring import las_in_servrar, exportera_som_csv
from kontroller import kontrollera_server, kontrollera_alla
import argparse
import sys

def main():

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
        "--kontrollera-alla-servrar",
        action="store_true",
        help="Kontrollera alla servrar"
    )
    parser.add_argument(
        "--kontrollera-en-server",
        help="Kontrollera en server"
    )
    parser.add_argument(
        "--exportera-som-csv",
        action="store_true",
        help="Exportera server som csv"
    )
    args = parser.parse_args()#reads argument user puts in terminal
    servrar = las_in_servrar()#reads servers from the json file

    if args.lista:
        if args.miljo:
            visa_miljospecifik(servrar)
        else:
            visa_alla(servrar)

    elif args.kontrollera_en_server:
        hittad = False

        for server in servrar:
            if server["namn"] == args.kontrollera_en_server:
                kontrollera_server(server, servrar)
                hittad = True
                if server["Status"] == "down":
                    sys.exit(1)
                break

        if not hittad:
            print("Server hittades ej")
            sys.exit(1)

    elif args.kontrollera_alla_servrar:
        kontrollera_alla(servrar)

        for server in servrar:
            if server["Status"] == "down":
                sys.exit(1)

    elif args.exportera_som_csv:
        exportera_som_csv(servrar)

    else:
        kor_meny(servrar)

if __name__ == "__main__":
    main()