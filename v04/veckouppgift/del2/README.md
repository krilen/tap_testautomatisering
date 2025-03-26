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
