class Kunde:

    def __init__(self, epost, melding):
        self.epost = epost
        self.melding = melding
        self.melding = f"{self.epost} lurte på: {melding}"


