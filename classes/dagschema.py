class Dagshema:
    def __init__(self, aantal, rust, herhaling, uitgevoerd, datum):
        self.aantal = aantal
        self.rust = rust
        self.herhaling = herhaling
        self.uitgevoerd = uitgevoerd
        self.datum = datum

    def __str__(self):
        return f"Aantal: {self.aantal}, Rust: {self.rust}, Herhaling: {self.herhaling}, Uitgevoerd: {self.uitgevoerd}, Datum: {self.datum}"