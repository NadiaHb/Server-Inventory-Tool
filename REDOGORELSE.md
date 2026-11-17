# 1. Välj tre olika konstruktioner i koden, till exempel ett villkor, en loop och en funktion med parametrar och return. Förklara hur syntaxen fungerar och vad koden gör.


## Villkor

i meny.py 

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

Detta kodblocket är för att kontrollera om en server befinner sig i produktionsmiljön(prod). Denna kontrollen vill jag ha med eftersom det ska krävas en kontroll innan servrar som befinner sig i produktionsmiljö kan tas bort(menyval 4).

Den första if satsen: 

**if server["namn"] == namn:**

Kontrollerar om namnet som användaren skrev in som servernamn faktiskt matchar ett servernamn som finns registrerat. 

**if server["miljo"] == "prod":
               godkannande = input(
                   "Obs, denna server ligger i produktionsmiljö. Vänligen bekräfta borttagning med ja eller nej. "
               )**

Den andra if-satsen  om den valda servern ligger i miljön "prod". Om den gör det så ska användaren få upp texten. Obs detta gäller enbart om servern ligger i "prod".

"Obs, denna server ligger i produktionsmiljö. Vänligen bekräfta borttagning med ja eller nej. "

Och därefter invänta att användaren skriver in "ja"

**if godkannande.lower() != "ja":
                   print("Server har ej tagits bort")
                   return**

**if godkannande.lower() != "ja":
                   print("Server har ej tagits bort")
                   return**

Här kontrolleras om användaren angett något annat än just "ja", vilket krävs för att ta bort servern. Med != kontrolleras att svaret inte är lika med "ja". .lower används för att göra om text till små bokstäver så att även "JA" matchar. 
  Funktionen avslutas sedan med return om användaren inte bekräftat med ett "ja". Servern tas då inte bort

## Loop

i main.py 

  **for server in servrar:
            if server["status"] == "down":
                sys.exit(1)**


**for server in servrar:**

for är koden som startar själva loopen
Kodblocket innebär att programmet ska loopa igenom listan med servrar och kolla på en server åt gången.

**if server["status"] == "down":
                sys.exit(1)**

för varje server programmet kontrollerar så kontrolleras det om serverns status är "down".
Om servern har statusen "down" så ska programmer avslutas med exitkod 1, vilket betyder att någonting har gått fel.

## Funktion

i status.py 

**def kontrollera_status(status):
    if status in status_varden:
        return True
    else:
        return False**

**def kontrollera_status(status):**

def skapar en funktion. kontrollera_status är funktionens namn.
Funktionen ska ta emot ett värde (för status) som den sedan ska kontrollera.

**if status in status_varden:**

if satsen kontrollerar om värdet som funktionen fått finns med i listan "status_varden". Listan innehåller de 3 värdena som är godkända för status.

**return True**

Om statusen finns med i listan status_varden skickas True tillbaka.

**return False**

Om statusen inte finns med i listan status_varden skickas False tillbaka.

Return används alltså för att skicka tillbaka resultatet till den kod som anropat funktionen.


# 2. Varför passar en lista med dictionaries för att lagra servrarna? Vilka datatyper har värdena i en server?

Att använda en lista med dictionaries gör att det är enkelt att lägga till, ta bort och hålla reda på servrarna, vilket passar bra i ett program som detta då programmet har hand om flera servrar. Med listan blir det enkelt att felsöka och uppdatera efter behov. 

Listan är byggd på att varje enskild server har sin egen dictionary med nycklar. 
Jag kan därför välja precis vilken unik server jag vill titta närmare på och på så sätt hålls serverinformationen organiserad.

i servrar.json hittar man nedan:

Servrarna består av värden och datatyper:

namn- sträng

adress- sträng

miljo- sträng

roll- sträng

status- sträng

senast_kontrollerad- None tills kontroll gjorts, därefter sträng.

# 3. Varför sparar du data i JSON men exporterar rapporten som CSV?

Jag sparar data i JSON eftersom jag inte vill att data går förlorad när jag stänger och startar om mitt program på nytt. 

servrarjson sparar all information om servrarna och informationen om servrarna uppdateras baserat på hur användaren interagerar. Man kan exempelvis lägga till en server. 

Jag exporterar sedan med CSV då CSV används för att skapa rapporter. När jag exporterat en fil till CSV blir informationen väldigt lätt att läsa då den visas i rader och kolumner och kan öppnas enkelt i Excel. 

# 4. Hur är programmet uppdelat i moduler och funktioner? Vilket ansvar har varje fil?

Programmet är uppdelat i följande moduler:

main.py - Här startar programmet. Det är även här programmet kontrollerar hur användaren vill köra programmet. Om användaren inte angett något argument startas texymenyn, annars körs argumentkomandot.

meny.py- Meny innehåler själva textmenyn som visas när programmet startat utan argument och innehåller 8 olika menyval. Här kan man interagera med programmet och göra olika va kopplade till servrarna, exempelvis visa alla servrar och ta bort servrar. Denna modul innehåller också alla funktioner kopplade till menyvalen.

servrar.json - Här finns all den sparade informationen om de olika servrarna. Denna fil uppdateras och sparae ändringar finns kvar även efter programmet stängs ned. 

lagring.py- Lagring läser in och sparar information till JSON och har hand om exporten av information till CSV.

status.py- Här finns funktioner för att kontrollera och visa status för seevers.

test_status.py - test_status testar funktionerna i status.py

kontroller.py- Kontrollerar om servrar svarar på ping och uppdaterar servrarna med information om när de sist kontrollerats.
Funktionerna i kontroller.py används både av menyn men också från CLI. Logiken behöver alltså inte upprepas igen.

Det är med fördel man delar upp programmet på detta vis, dels för att få en struktur och att så kodne organiserad men även för att felsöka eller göra ändringar. Skulle allting vara i en enda stor fil så hade det blivit svårare att titta närmare på en specifik server eller ändra en specifk del av koden.

Med tydliga uppdelningar av kod och tydliga ansvarsområden vet man snabbt vart man ska leta


# 5. Vilka moduler från standardbiblioteket använder du och till vad?

sys: Ser till så att programmet avslutas med rätt exitkod.(finns t.ex i main.py)

argparse: Skapar argument användaren kan använda och ser till så argumenten hanteras.(finns t.ex i main.py)

subprocess: Startar ping kommandot(finns i kontroller.py)

os: Används för att läsa miljövariabel och kontrollera vilket operativsystem användaren har för att rätt ping kommando ska köras.(finns i t.ex kontroller.py)

pathlib: Kontrollerar sökvägarna, filer och skapade exempelvis rapportmappen(finns i lagring.py)

datetime: För att ämta aktuell tid och datum. Används i koden exempelvis i exporterade filer till rapporter.(finns t.ex i kontroller.py)

json: För att läsa och spara information i JSON format(finns i t.ex lagring.py)

csv: För att kunna skapa CSV-rapport(finns i lagring.py)

# 6. Ge tre exempel på god praxis från din kod och förklara varför de är bra.

1. Jag har delat upp programmet i tydliga moduler med tydliga ansvarsområden. Det är därför enkelt och snabbt att hitta rätt i programmet och göra ändringar. 
   
2. Jag har funktioner med tydliga uppgifter och namn. Detta gör koden enkel att förstå för andra som läser koden. Exempelvis las_in_servrar() och spara_servrar(). (i lagring.py)
   
3. Jag återanvänder kod, exempelvis vissa funktioner så jag slipper upprepa kod flera gånger i onödan. T.ex kontrollera_server() i kontroller.py som används både i main.py och meny.py. 
   
# 7. Vilka källor och hjälpmedel har du använt och till vad? Det kan till exempel vara kursboken, dokumentation, forum eller AI-verktyg.

Jag har använt både presentationerna, anteckningar från föreläsningarna samt w3Schools för att förstå själva syntax och vad viss kod betyder. 

Jag har fått hjälp av klasskamrater och AI verktyg på google för att få mer förståelse för användning av  linux terminalen samt Pycharm, för att beta av checklistan och se så allt är avklarat och för att tolka felmeddelande/buggar.
