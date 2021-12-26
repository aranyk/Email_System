from Ansatt import Ansatt
from Systemet import Systemet

arany = Ansatt("arany98", "Cutie")
system = Systemet("mosti", 10)
navn = input("Navn: ")
år = input("År: ")
system = Systemet(navn, år)


arany.logg_inn_bekreftelse()

