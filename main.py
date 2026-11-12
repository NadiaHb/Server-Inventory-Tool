from servrar import servrar
from lagring import lagring

def meny():
    while True:
        visa_meny()
        val = input("Ditt val är: ")
        if val == "1":
            visa_alla(servrar)
        elif val == "2":
            visa_miljospecifik(servrar)
        elif val == "3":
            lagg_till(servrar)
        elif val == "4":
            kontrollera_en(servrar)
        elif val == "5":
            kontrollera_alla(servrar)
        elif val == "6":
            exportera_som_csv(lagring)
        elif val == "7":
            print(f"Avslutar program. Välkommen åter")
            break
        else:
            print(f"Ogiltligt val, testa igen.")

if __name__ == "__main__":
    main()