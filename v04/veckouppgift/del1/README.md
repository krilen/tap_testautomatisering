# BDD

## Del 1

Du ska beskriva och testa ett enkelt system för en webbutik som säljer böcker. Systemet
har följande enkla krav:

- Användaren kan lägga böcker i en varukorg
- Användaren kan ta bort böcker från varukorgen
- Varukorgen visar alltid aktuell summa och antal böcker
- Om användaren försöker lägga en bok som redan ﬁnns i varukorgen ska antalet av just den boken öka istället för att skapa en ny rad
- Det skall gå att tömma varukorgen helt

### Uppgiften

1. Skriv tydliga scenarier i Gherkin som beskriver ovanstående krav. Använd gärna
   Scenario Outline där det passar.
2. Implementera step-ﬁlerna i Python med hjälp av Behave.
3. Din Python-kod behöver inte kopplas mot en riktig webbsida eller databas, det
   räcker med att simulera funktionaliteten med hjälp av enklare Python-klasser
   eller funktioner.
4. Kontrollera att alla scenarier kör utan fel med hjälp av Behave.

### Min lösning

Den var svår i början innan man kom igång med det. Sedan när felen kom blev det lättare med tiden eftersom man lärde sig att "tolka" felen.  
Jag skapade en enkel "Cart" class som sparade böckerna som placerades i lista bestående av dicts ex: [{"name": "book1", "price": 200, "count": 1}, ...]
När en bok av samma namn lades till uppdaterade jag bara "count" i dict:en för den boken.  
Det jag fastnade först på var med "Scenario Outline" och ints är man var tvungen att definera att det skulle vara en int via "{price:d}". Sedan kom jag fram till att "Senario Outline" behövdes inte eftersom detta innebär bara att hela senariot körs om. Det jag behövde vara bara att kunna lägga till flera böcker och det hittade jag hur man gjorde i dokumentationen. Detta gjorde att jag skippade "Senario Outline" tillslut.  
När det gäller kontrollen av extrema fall som om böcker kostar -1000 så kan det ju faktiskt finnas en sådan bok som kan används som en rabattkod.
