# Dunder methods -> '__method'

from uuid import uuid4 # bu hech qachon takrorlanmaydigan id kod yaratib beradi


class Avto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km # '__' bilan inkapsulyatsiya qilingan, ya'ni yashirilgan xususiyat
        self.__id = uuid4() # inkapsulyatsiya qilingan xususiyat
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi.")

    # Dunder methods:
    # def __str__(self):
        # return f"Avto: {self.make} {self.model}"

    def __repr__(self):
        return f"Avto: {self.make} {self.model}"

    def __eq__(self, y):
        return self.narh == y.narh

    def __lt__(self, y):
        return self.narh < y.narh

    def __le__(self, y):
        return self.narh <= y.narh


class AvtoSalon:
    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f'{self.name} avtosaloni.'

    def __setitem__(self, key, value):
        self.avtolar[key] = value

    def __getitem__(self, index):
        return self.avtolar[index]

    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto): # isinstance(a, b) -> bu a obyekt b klassga tegishli ekanligini tekshiradi
                self.avtolar.append(avto) # agar tegishli bo'lsa Avto klassining avtolariga qo'shsak bo'ladi, boshqa klassning obyektlarini qo'shib bo'lmaydi, chunki ular avtomobil bo'lmaslugi mumkin.
            else:
                print("Avto kiriting!")

    def __len__(self):
        pass



avto1 = Avto("GM", "Malibu", "Qora", 2025, "60000", 1000)
avto2 = Avto("GM", "Lacetti", "Qora", 2025, "50000", 1400)
avto3 = Avto("GM", "Nexia-3", "Qora", 2025, "40000", 1800)
#print(avto1)
#print(avto1 == avto2)
#print(avto1 > avto2)
#print(avto1 <= avto2)

salon1 = AvtoSalon("MaxAvto")
print(salon1)

salon1.add_avto(avto1, avto2, avto3)
print(salon1[0])
print(salon1[1])
print(salon1[:])

salon1[0] = Avto("GM", "BMW M5", "Oq", 2025, "260000", 1200)
print(salon1[:])
