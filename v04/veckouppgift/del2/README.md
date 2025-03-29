# BDD

## Del 2

Här kommer du behöva tänka till och forska på egen hand. Du skall vidareutveckla
uppgiften till att inkludera ytterligare funktionalitet samt några svårare testfall.

Extra krav som skall implementeras (du skall göra minst tre av dem):

- **Rabattfunktion.** Om användaren köper ﬂer än tre böcker skall hon få 10% rabatt
  på hela kundkorgen. Testa ﬂera olika fall, inklusive värden som är osannolika som
  -1000 och 64000 böcker.
- **Lagerhantering.** Varje bok skall ha en lagerstatus. Om användaren försöker köpa
  ﬂer exemplar än vad som ﬁnns i lagret, visas ett tydligt meddelande och antalet
  begränsas till lagersaldot.
- **Login.** Användaren måste logga in med giltiga användaruppgifter innan köpet kan
  genomföras. Testa både lyckade och misslyckade inloggingar med Scenario
  Outline.
- **Beställningshistorik.** Användaren skall kunna se historiken över sina tidigare
  beställningar. Testa att beställningar visas korrekt.
- **Kvitto.** När en beställning är genomförd skickas ett kvitto automatiskt via e-post
  (detta simulerar du i Python, du behöver inte skicka mailet på riktigt). Testa att
  kvittot skapas och skickas iväg.

### Uppgiften:

1. Gör research online för att hitta bra sätt att implementera funktionerna i Python,
   utan att använda komplex webbteknik som ramverk och liknande.
2. Skriv tydliga och underhållbara scenarier i Gherkin som testar varje vald
   extrafunktion.
3. Implementera steps-deﬁnitionerna i Behave och Python. Använd klasser,
   funktioner och variabler för att simulera funktionerna.
4. Se till att testfallen fungerar och kör utan fel med kommandot behave.

### Min lösning

Jag gjorde denna också och de tre första testfallen (Rabatt, Lager och Login). Varför jag valde dem vet jag inte kanske tog jag bara dem i ordning.

**OBS!!!** För att köra min kod behövs "requests" också installeras via pip.

När det gällde "lagar" så valde jag en liten annan väg eftersom jag skapade en api klient/fråga som gjorde en request till https://dummyjson.com/.

Därför är min "products.py" bara en fråga till backend:et som det skall vara i verkligenten. Dock så valde jag att begränsa min fråga till mobiler och deras "title", price" och "stock" via request frågan (https://dummyjson.com/products/category/smartphones?select=title,price,stock). Det är därför min "cart.feature" innehåller items med id 124, 125 etc eftersom dessa är "verkliga" id på mobilerna hos DummyJSON. Detta gör att min kontroll via 'behave' tar lite längre tid (uppåt 30 sek) eftersom den i verkligenheten tar kontakt med ett backend.

När jag valde att gå över till ett verkligt backend krävde det lite modifkationer av min kod från "del1" men jag upptäckte senare att vissa saker som efterfrågades i testfallen gjorde att jag skrev mer och mer kod i "step_cart.py" för att lösen dem. Tillslut var det mer kod i "step_cart.py" än vad jag hade i min "cart.py" och det gillade jag inte, kändes som om jag löste problem med testen än problem med min kod. Därför valde jag i slutet av veckan att tänka om min hur min kundkorg var uppbyggs. Jag valde därför att bygga om min kundkorg samt de tillhörande metoderna. Däefter kunde jag mycket enklare hantera testfallen och jag slapp ha så mycket kod i "step_cart.py" plus att vissa saker som behövdes läggas till i "cart.py" inte bara kunde lösas rakt upp och ner utan ändå krävde en förändring (meddelande on lagarbegränsningarna).

Dessutom skulle jag vilja informeran om att jag nu förstår "Scenario otline" som jag i del1 sa att jag valde att skippa.

Det största problemet jag hade var login och behandlingen av blanka eller tomma fält som input värden vid test av login. Sökte via Google och det pratades om parse och definera typer men jag kom ingenstans med det. Tillslut frågade jag ChatGPT om lite hjälp men även var det svaret var inte helt korrekt dock gav det mig en ledtråd på hur det skulle kunna lösas. Problemet var att att allt kom in med " runt sig (ex:"john", "") att bara använda 'slice" hjälpte inte. Tillslut löste jag det men att det var en verklig omväg för ett sådan enkelt problem.
