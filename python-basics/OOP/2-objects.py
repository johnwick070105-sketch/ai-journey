# Obyektlar bilan ishlash (Objects)

class Talaba:
    # Klassning xususiyatlari __init__ funksiyasining ichiga yoziladi:
    def __init__(self, ism, familiya, tyil): # Klassning ichidagi funksiyaga yana obyektning o'zini uzatishimiz uchun self ishlatiladi.
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_name(self):
        return self.ism

    def get_lastname(self):
        return self.familiya

    def get_fullname(self):
        return f'{self.ism} {self.familiya}'

    def get_info(self):
        return f'{self.ism} {self.familiya}, {self.bosqich}-bosqich talabasi.'

    def set_bosqich(self, yangi_bosqich):
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        self.bosqich += 1


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_fullname() for talaba in self.talabalar]


# Classning metodlarini ko'rish uchun funksiya:
def see_methods(klass):
    return [method for method in dir(klass) if not method.startswith('__')]


talaba1 = Talaba("Sardorbek", "Tursunov", 2005)
talaba2 = Talaba("Tolibjon", "Aliyev", 2008)

matem = Fan('Oliy matematika')
matem.add_student(talaba1)
matem.add_student(talaba2)
print(matem.get_students())

# print(dir(Talaba)) # dir(Class) - bu klassning metodlarini ko'rsatadi
print(see_methods(Talaba)) # Talaba classning metodlarini ko'rish
print(talaba1.__dict__.keys()) # Classning xususiyatlarini ko'rish
