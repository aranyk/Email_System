class Ansatt:


    def __init__(self, brukernavn, passord):
        self.brukernavn = brukernavn
        self.passord = passord
        self.mail = f"{brukernavn}@hotmail.com"



    def new_mail(self, brukernavn):
        work_mail = f"{brukernavn}@hotmail.com"

        if self.mail == work_mail:

            work_mail = str(input("enter value for new mail"))

            return f"{work_mail}@hotmail.com"

        else:
            return work_mail




    def logg_inn_bekreftelse(self):

        bruker = "mosti"
        passw =  "Nettavisen123"

        if self.mail == bruker and passw == self.passord:
            print(f"Du er logget inn i systemet")
            return 1
        else:
            print("brukernavnet eller passordet er feil")
            return -1


