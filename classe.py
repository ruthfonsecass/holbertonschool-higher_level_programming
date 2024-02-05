class Vehicle():
    def __init__(self, type, roues) -> None:
        self.type = type
        self.roues = roues

garage = {}

class Voiture(Vehicle):
    def __init__(self, marque: str, modele: str, plaque: str):
        super().__init__("Voiture", 4)
        self.marque = marque
        self.modele = modele
        self.plaque = plaque
        garage.setdefault(self.plaque, self)

    @staticmethod
    def get(plaque: str):
        return garage.get(plaque)

voiture_1 = Voiture("Peugeot", "206", "TEST")
voiture_2 = Voiture("Renault", "Clio", "ADONIS")

print(voiture_1.marque, voiture_1.modele, voiture_1.roues, voiture_1.type)
print(voiture_2.marque, voiture_2.modele)
voiture_2.modele = "Scenic"
print(voiture_2.modele)

print(Voiture.get("TEST").modele)