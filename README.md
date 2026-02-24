# Fitnesslogboek - BeastBuilder
    Where real beast are made
## Inleiding

Dit project is een fitnesslogboek opgebouwd volgens een drie-lagenarchitectuur.
- De presentation layer toont de gebruikersinterface waarin sporters trainingen oefeningen en voortgang kunnen invoeren en bekijken.
- De business-logic-layer bevat de applicatielogica zoals het verwerken van invoer berekenen van statistieken en het aansturen van de datastromen. 
- De data access layer verzorgt de opslag en het ophalen van trainingsgegevens uit een database of bestand.

De scheiding van lagen zorgt voor overzicht onderhoudbaarheid en uitbreidbaarheid van het systeem.

## Doel

Het doel van dit project is het ontwikkelen van een gestructureerd en gebruiksvriendelijk fitnesslogboek waarmee gebruikers hun trainingen kunnen registreren analyseren en opvolgen. Het systeem ondersteunt inzicht in prestaties consistentie en vooruitgang door een duidelijke scheiding tussen presentatie logica en dataopslag.

## Aanleiding

Sport is een belangrijk onderdeel van ons eigen leven. Vanuit die interesse is het idee ontstaan om een fitnesslogboek te maken dat deze passie vertaalt naar een praktisch informaticaproject. Door onze interesse in sport te combineren met technologie willen we anderen motiveren om actiever te bewegen en bewuster met hun gezondheid om te gaan. Het project is bedoeld om sport toegankelijker en leuker te maken en zo bij te dragen aan een gezondere levensstijl.

## Betrokkenen

#### Betrokken partijen
- JIMS Maldegem
- Basic Fit Maldegem
- Bit4Motion Maldegem

#### Product Owner

- Ibe Franckeart
- Arjuna Veldhuizen

#### Stakeholders

- Klanten
- Eigenaars fitnessen
- Aandeelhouders


## Projectscope

### Welke problemen worden opgelost

* training schema's zijn toegangkelijker 

* Geen centrale plaats om trainingen op te slaan

* Gebrek aan overzicht in voortgang en prestaties

* Verlies van motivatie door onduidelijke resultaten

* Foutgevoelige en ongestructureerde handmatige registratie

* Te complexe of niet-persoonlijke bestaande fitnessapps


### Wat zit er in de scope

- Trainings schema's

- Consistentie

- Vooruitgang bekijken

- Training opslaan


## Eisen

### Functionele eisen

Het project moet trainingschema's kunnen maken en analyseren, door de opgeslagen of ingegeven data. Ook moet het meer gepersonaliseerd zijn voor elk lichaamstype. Het moet tonen als je consistent bezig bent en je meer motiveren door je vooruitgang weertegeven. Ook moet het eerdere training opslaan.

### Technische eisen

Het project heeft een database, ERD, Klassediagram, HTML-code en Klasses via python code nodig.

### Wettelijk kader

Dit project houdt rekening met het wettelijk kader rond gegevensbescherming en privacy. Omdat er persoonlijke gegevens zoals naam leeftijd en trainingsgegevens worden verwerkt wordt de Algemene Verordening Gegevensbescherming nageleefd. Er worden enkel noodzakelijke gegevens verzameld met een duidelijk omschreven doel en deze gegevens worden niet gedeeld met derden of commercieel gebruikt. De opslag van data gebeurt op een beveiligde manier binnen de data access layer. Gebruikers hebben het recht om hun gegevens in te zien aan te passen of te laten verwijderen.

