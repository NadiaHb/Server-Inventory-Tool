from lagring import spara_servrar, exportera_som_csv
from kontroller import kontrollera_server, kontrollera_alla
from status import visa_status

def visa_meny():
    print(" ===Server Inventory Tool === ")
    print()
    print(" 1. Visa alla servrar")
    print(" 2. Visa miljöspecifik server")
    print(" 3. Lägg till server")
    print(" 4. Ta bort server")
    print(" 5. Kontrollera en server")
    print(" 6. Kontrollera alla servrar")
    print(" 7. Exportera rapport som CSV")
    print(" 8. Avsluta")
    print()

def kor_meny(servrar):
    while True:

        visa_meny()

        val= input("Välj menyval: ")

        if val == "1":
            visa_alla(servrar)
        elif val == "2":
            visa_miljospecifik(servrar)
        elif val == "3":
            lagg_till(servrar)
        elif val == "4":
            ta_bort(servrar)
        elif val == "5":
            kontrollera_en(servrar)
        elif val == "6":
            kontrollera_alla(servrar)
        elif val == "7":
            exportera_som_csv(servrar)
        elif val == "8":
            print("Avslutar")
            break
        else:
            print("Ogiltligt val")

#Lists all servers in columns.
def visa_lista(servrar):
    print(f"{'Namn':<15} {'Adress':<15} {'Miljö':<15} {'Roll':<15} {'Status':<15}")

    for server in servrar:
        print(
            f"{server['namn']:<15}" #Fixes widths
            f"{server['adress']:<15}"
            f"{server['miljo']:<15}"
            f"{server['roll']:<15}"
            f"{visa_status(server['status']):<15}"
        )

def visa_alla(servrar):
    print("--- Alla servrar ---")

    if len(servrar) == 0: #Checking if there are any servers
        print("Inga servrar hittades")
        return

    visa_lista(servrar) #Using the pre-existing list function to avoid having to write list everytime needed.

def visa_miljospecifik(servrar,miljo=None):
    if miljo is None:
        miljo = input("Ange miljön: dev/test/prod: ").strip()

    hittad = False
    servrar_i_miljo = [] #Making a list for servers in the specific environment

    for server in servrar:
        if server["miljo"] == miljo:
            servrar_i_miljo.append(server)
            hittad = True
    if hittad:
        visa_lista(servrar_i_miljo)
    else:
        print("Ogiltligt val")


def lagg_till(servrar):
    #These three values for "miljo" are the only ones allowed
    alternativ_for_miljo = ["dev", "test", "prod"]

    namn = input("Vänlien ange namnet på den nya servern: ").strip()
    while namn == "":
        print("Detta fält får ej lämnas tomt")
        namn = input("Vänigen ange namnet på den nya servern: ").strip()

    for server in servrar:
        #Checks if the servername user enter already exist
        if server["namn"] == namn:
            print("Servern existerar redan")
            return

    adress = input("Vänligen ange adress: ").strip()
    while adress == "":
        print("Detta fält får ej lämnas tomt")
        adress = input("Vänligen ange adress: ").strip()

    roll = input("Ange rollen för server: ").strip()
    while roll == "":
        print("Detta fält får ej lämnas tomt")
        roll = input("Ange rollen för servern:  ").strip()

    while True: #Display the menu until user chose exit option
        miljo = input("Vänligen ange miljön för den nya servern: ").strip()

        if miljo in alternativ_for_miljo:
            break

        print("Ogiltlig miljö")

    ny_server = {
        "namn": namn,
        "adress": adress,
        "miljo": miljo,
        "roll": roll,
        "status": "unknown",
        "senast_kontrollerad": None
    }
    servrar.append(ny_server)
    spara_servrar(servrar)
    print("Servern har lagts till.")

def ta_bort(servrar):

    namn= input("Ange servernamn:").strip()

    for server in servrar:
       if server["namn"] == namn:
           #Checks if the server is in prod, if so double checks before removal
           if server["miljo"] == "prod":
               godkannande = input(
                   "Obs, denna server ligger i produktionsmiljö. Vänligen bekräfta borttagning med ja eller nej. "
               )
               if godkannande.lower() != "ja":
                   print("Server har ej tagits bort")
                   return

           servrar.remove(server)
           spara_servrar(servrar)
           print("Servern har tagits bort")
           return

    print(f"Servern '{namn}' hittades inte.")


def kontrollera_en(servrar):
    namn = input("Ange servernamn: ").strip()

    for server in servrar:
        if server["namn"] == namn:
            kontrollera_server(server, servrar)

            print(f"Server: {server['namn']}")
            print(f"Status: {visa_status(server['status'])}")
            print(f"Senast kontrollerad: {server['senast_kontrollerad']}")
            return

    print(f"Servern '{namn}' hittades ej")
