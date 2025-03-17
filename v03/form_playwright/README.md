# Testa formulär

## User Stories

[U1] Som en besökare 
     vill jag bli påmind med ett vänligt felmeddelande om jag inte skrivit i mitt namn
     så att jag fyller i formuläret korrekt

[U2] Som en besökare
     vill jag kunna registrera mig genom att klicka på knappen när jag fyllt i alla fält korrekt
     så att jag kan använda tjänsten

## Accepantskriterier

[U1.A1] Om namnfältet är tomt, skall det visas ett felmedelande
[U1.A2] Om namnfältet innehåller minst 1 tecken skall felmeddealndet inte visas

[U2.A1] Kanppen ska gå att klicka på när alla fält är korrekt ifyllda.
[U2.A1] Kanppen ska int gå att klicka på om minst ett fält är felaktigt ifyllt.


## Testscenaroer

[T1]
1. Kontrollera att testfältet inte är tomt.
2. Kontrollera att felmeddelandet inte visas.
3. Sudda det som finns i fältet.
4. Kontrollera att felmeddeandet visas.

[T2]
1. Kontrollera att knappen är avstängd. (disabled)
2. Skriv in "password" i lösenordsfältet.
3. Kontrollera att knappen är aktiverad. (ej disabled)