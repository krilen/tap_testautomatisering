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

.