# Veckouppgift 6

## Vecka 15, 7/4

*1 Du ska lösa uppgiften självständigt eller tillsammans med en annan student. Men vid minst ett tillfälle ska du göra code review i en grupp.*

*2 Du får ta hjälp av AI för att förklara koncept och lösa fel. Du får inte be AI lösa uppgiften åt dig direkt. Om du gör det, kommer du inte att lära dig grunderna, och inte kunna lösa svårare problem.*

---

### Mina vänner

*Denna uppgift är öppet utformad. Tänk på att arbeta enligt TDD-metoden: red, green, refactor. Lägg till ett scenario i taget och gå inte vidare förrän det är grönt. Om du tror att du inte kommer att hinna med hela uppgiften, prioritera den viktigaste funktionaliteten.*

1 Betrakta [https://forverkliga.se/JavaScript/my-contacts/\#/](https://forverkliga.se/JavaScript/my-contacts/#/) . Skriv user stories som beskriver vad användaren ska kunna göra.   
Tips: Här är nuvarande funktionalitet:

* Visa lista med alla mina vänner  
  * Ändra uppgifter för en vän  
    * Formuläret visar ett felmeddelande om inte båda fälten är ifyllda  
  * Ta bort en vän  
  * Söka baserat på namn, oberoende av stora eller små bokstäver  
  * Söka baserat på e-post, oberoende av stora eller små bokstäver  
* Lägga till ny vän  
  * Formuläret visar ett felmeddelande om inte båda fälten är ifyllda

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

**US01**  
som en användare  
vill jag kunna komma åt sidan  
så att jag kan se vad jag kan göra
 
**US02**  
som en användare  
vill jag kunna komma åt sidan  
så jag har möjlighet att se start, vänlista och ny vän länk

**US03**  
som en användare  
vill jag kunna se i min vänlista  
så jag kan se vilka vänner jag har

**US04**  
som en användare  
vill jag kunna ändra min väns namn  
så jag håller informationen uppdaterad

**US05**  
som en användare  
vill jag kunna ändra min väns epost  
så jag håller informationen uppdaterad

**US06**  
som en användare  
vill jag kunna ta bort en vän  
så att min lista av vänner minskas

**US07**  
som en användare  
vill jag kunna ta bort alla mina vänner  
så att min lista av vänner blir tom  

**US08**  
som en användare  
vill jag kunna söka upp en vän  
så att snabbt får fram vännens uppgifter

**US09**  
som en användare  
vill jag kunna lägga till vän  
så att min lista av vänner ökar

