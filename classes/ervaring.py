class Ervaring:
    def __init__(self, ervaringsgraad,naam):
        self.ervaringsgraad = ervaringsgraad
        self.naam = naam

    def __repr__(self):
        return f"Ervaringsgraad: {self.ervaringsgraad} Naam: {self.naam}"