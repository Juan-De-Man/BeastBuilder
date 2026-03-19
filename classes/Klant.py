class Klant():
    def __init__(self,lidnr=None,vnaam=None,naam=None,geboortejaar=None,telnummer=None,gewicht=None,lengte=None,lidstart=None,lidstop=None,straat=None,huisnummer=None,email=None):
        self.lidnr= lidnr
        self.vnaam = vnaam
        self.naam = naam
        self.geboortejaar = geboortejaar
        self.telnummer = telnummer
        self.gewicht = gewicht
        self.lengte = lengte
        self.lidstart = lidstart
        self.lidstop = lidstop
        self.straat = straat
        self.huisnummer = huisnummer
        self.email = email

    #Weergeven van de gegevens(representen)
    def __repr__(self):
        return f'Klant(lidnr={self.lidnr},voornaam={self.vnaam},\
            naam={self.naam},geboortejaar={self.geboortejaar},telefoonnummer={self.telnummer},gewicht={self.gewicht},\
            lengte={self.lengte},lidstart={self.lidstart},lidstop={self.lidstop},huisnummer={self.huisnummer},email={self.email})'


        