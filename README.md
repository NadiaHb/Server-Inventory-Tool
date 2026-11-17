# Beskrivning av Server Status Tool och vad programmet gör:
Detta är ett python program vars funktion är att kontrollera servrar och dess status.

Programmet visar information om de olika servrarna, exempelvis vilken miljö de befinner sig i samt en lista där man kan se samtliga registrerade servrar. All information om servrarna sparas i JSON- fil vilket gör att listan hålls uppdaterad och informationen om servrarna inte går förlorad när programmet stängs ned. 

## Hur programmet körs

För att kunna köra Server Status Tool behöver du:

-En terminal

-Python 3

Python-filerna från projektet

## Hur programmet startas

Programmet kan användas på två olika sätt - antingen via en textmeny i terminalen eller via argument(CLI).

För att komma åt textmenyn i terminalen skriver man: python3 main.py och då följer programmets 8 menyval.

För att använda programmet med hjälp av argument kan man exempelvis använda si utav: python3 main.py -lista (Denna funktion visar alla registrerade servrar)

## Programmets struktur

Programmet är uppdelat i flera moduler med tydliga ansvarsområden för att göra koden tydilig och enkel både att förstå och att felsöka och arbeta med. 

De olika modulerna och deras ansvarsområden är följande:

main.py - Här startar programmet. Det är även här programmet kontrollerar hur användaren vill köra programmet. Om användaren inte angett något argument startas texymenyn, annars körs argumentkomandot.

meny.py- Meny innehåler själva textmenyn som visas när programmet startat utan argument och innehåller 8 olika menyval. Här kan man interagera med programmet och göra olika va kopplade till servrarna, exempelvis visa alla servrar och ta bort servrar. Denna modul innehåller också alla funktioner kopplade till menyvalen.

servrar.json - Här finns all den sparade informationen om de olika servrarna. Denna fil uppdateras och sparae ändringar finns kvar även efter programmet stängs ned. 

lagring.py- Lagring läser in och sparar information till JSON och har hand om exporten av information till CSV.

status.py- Här finns funktioner för att kontrollera och visa status för seevers.

test_status.py - test_status testar funktionerna i status.py

kontroller.py- Kontrollerar om servrar svarar på ping och uppdaterar servrarna med information om när de sist kontrollerats.
Funktionerna i kontroller.py används både av menyn men också från CLI. Logiken behöver alltså inte upprepas igen.

## Hur programmet använder miljövariabeln 

All serverinformation sparas i JSON-fil. Programmet använder servrar.json som standardfilen där den informationen sparas.

Miljövariabel är en variabel/kommando som används för att bestämma vilken JSON fil man vill använda.  
I mitt program finns följande kod(i lagring.py):

filnamn= Path(os.getenv("INVENTORY_DATAFIL", "servrar.json"))

I detta kodblock används os.getenv() för att fråga om det finns en miljövariabel vid namn "INVENTORY_DATAFIL"
Och om det då finns en miljövariabel med det filnamnet så används den filen för lagringen, annars används servrar.json(som ju är standarden).



