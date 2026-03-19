class Gemeente:
    def __init__(self, naam, postcode):
        self.naam = naam
        self.postcode = postcode
    
    def __str__(self):
        return f"{self.naam} ({self.postcode})"