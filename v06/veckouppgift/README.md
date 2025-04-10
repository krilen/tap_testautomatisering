# Veckouppgift 6

## Vecka 15, 7/4

_1 Du ska lösa uppgiften självständigt eller tillsammans med en annan student. Men vid minst ett tillfälle ska du göra code review i en grupp._

_2 Du får ta hjälp av AI för att förklara koncept och lösa fel. Du får inte be AI lösa uppgiften åt dig direkt. Om du gör det, kommer du inte att lära dig grunderna, och inte kunna lösa svårare problem._

---

### Mina vänner

_Denna uppgift är öppet utformad. Tänk på att arbeta enligt TDD-metoden: red, green, refactor. Lägg till ett scenario i taget och gå inte vidare förrän det är grönt. Om du tror att du inte kommer att hinna med hela uppgiften, prioritera den viktigaste funktionaliteten._

1 Betrakta [https://forverkliga.se/JavaScript/my-contacts/\#/](https://forverkliga.se/JavaScript/my-contacts/#/) . Skriv user stories som beskriver vad användaren ska kunna göra.  
Tips: Här är nuvarande funktionalitet:

- Visa lista med alla mina vänner
  - Ändra uppgifter för en vän
    - Formuläret visar ett felmeddelande om inte båda fälten är ifyllda
  - Ta bort en vän
  - Söka baserat på namn, oberoende av stora eller små bokstäver
  - Söka baserat på e-post, oberoende av stora eller små bokstäver
- Lägga till ny vän
  - Formuläret visar ett felmeddelande om inte båda fälten är ifyllda

2 Diskutera och jämför dina user stories inom studiegrupperna eller med minst en annan klasskamrat. (Ni får vara hur många som helst\!) Målet är att genom att jämföra och se vad ni har tänkt olika, kan ni lära er mer om vad som är lämpligt och användbart att testa.

3 Skapa ett projekt med pytest, Playwright och behave. Använd mappstrukturen från presentationen. Skapa en tom feature-fil för varje feature som behövs för att uppfylla dina user stories.

4 Skriv scenarier med Gherkin (step-filer) för dina feature-filer.

5 Skriv step-filer med Playwright och pytest. Använd @given osv för att koppla dem till motsvarande feature-fil och scenario.

Efter hand som du skriver kod, försök abstrahera funktioner till Pages-filer. Använd gärna "Page Object" modellen, där funktionerna finns inuti en klass.

---

## Lösning

### Intryck

- sidan består av en header och main. header: rubrik och 3 länkar, main: här visa informationen
- startknappen tar en till huvudsidan
- vänlistan tar en till en lista med 5 personer som har namn och epost
- sökfältet söker på allt både namn och epost
- ändra på en vän dock måste båda fälten vara ifyllda utan att varnings meddelande dyker upp sam knappen aktiv
- att lägga till en "Ny vän" går inte att göra utan at lägga till båda fälten endast då blir spara knappen aktiv
- ta bort anändare vi knappen
- ...

### User stories

#### Start

**US01**  
som en användare  
vill jag kunna komma åt sidan  
så att jag kan se att jag är på rätt ställe.

**US02**  
som en användare  
vill jag se att jag kan navigera på webbplatsen genom länkar  
så jag har möjlighet att se start, vänlista och ny vän länk.

**US03**  
som en användare  
vill jag bekräfta att de olika länkarna har rätt url  
så att jag vet att ingen förändring har gjorts.

**US04**  
som en användare  
vill jag säkerställa att jag är på start sidan
och att "start" länken är aktiv (skiljer sig åt)
så att jag vet säker på var jag är.

#### Vänlista

**US05**  
som en användare  
vill jag säkerställa att jag är på sidan för vänlista
och att "vänlista" länken är aktiv (skiljer sig åt)
så att jag vet säker på var jag är.

**US06**  
som en användare  
vill jag kunna se min vänlista  
så jag kan se mina vänners information.

**US07**  
som en användare  
vill jag kunna se hur många vänner jag har  
så jag kan ta bort dem alla och börja om.

#### Ny vän

**US08**  
som en användare  
vill jag säkerställa att jag är på sidan för att lägga till en vän  
och att "spara" knappen inte är aktiv  
så att jag vet säker på var jag är.

**US09**  
som en användare  
vill jag kunna lägga till en vän  
så att min lista över vänner ökar med 1

**US10**  
som en användare  
vill säkarställa att all information (alla fält skrivs in)  
så att en vän då endast läggs till.

#### Kombo

**US11**  
som en användare  
vill jag kunna ändra min väns information  
så jag håller informationen uppdaterad

**US12**  
som en användare  
vill jag kunna söka upp en vän  
så att snabbt får fram vännens uppgifter

**USxx**  
som en användare  
vill jag kunna ta bort en vän  
så att min lista av vänner minskas

...
