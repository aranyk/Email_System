class Systemet:

    def __init__(self, navn, år):
        self.navn = navn
        self.år = år
        self.mail = f"{navn}.{år}@hotmail.com"

    def registrer_bruker(self, navn, passord):
