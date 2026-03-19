class Trainingschema:
    def __init__(self, naam, nummer, datum):
        self.naam = naam
        self.nummer = nummer
        self.datum = datum
    
    def __str__(self):
        return f"Naam: {self.naam}, Nummer: {self.nummer}, Datum: {self.datum}"
    
    