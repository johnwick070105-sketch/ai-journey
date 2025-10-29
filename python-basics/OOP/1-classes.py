# Klasslar (Classes)
# Klassning ichidagi o'zgaruvchilar uning xususiyatlari, funksiyalar esa metodlari deyiladi.

class Talaba:
    # Klassning xususiyatlari __init__ funksiyasining ichiga yoziladi:
    def __init__(self, ism, familiya, tyil): # Klassning ichidagi funksiyaga yana obyektning o'zini uzatishimiz uchun self ishlatiladi.
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    # Metodlar:
    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.familiya

    def get_age(self, yil):
        return yil - self.tyil

    def tanishtir(self):
        return f'Ismim {self.ism} {self.familiya}, tug`ilgan yilim {self.tyil}-yil.'


talaba1 = Talaba("Sardorbek", "Tursunov", 2005)
talaba2 = Talaba("Tolibjon", "Aliyev", 2008)
talaba3 = Talaba("Davron", "Turdiyev", 1995)

print(talaba1.tanishtir())
print(talaba2.tanishtir())
print(talaba3.tanishtir())
print(talaba1.get_name())
print(talaba1.get_age(2025))
print(talaba2.get_lastname())
