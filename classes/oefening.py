class oefening():
    def __init__(self,spier=None,instructie=None,beschrijving=None):
        self.spier = spier
        self.instructie = instructie
        self.beschrijving = beschrijving

    def __repr__(self):
        return f'Oefening={self.spier}, Instructie={self.instructie}, Beschrijving= {self.beschrijving}'
    
    
    

        