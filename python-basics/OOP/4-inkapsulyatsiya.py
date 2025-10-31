# Inkapsulyatsiya va Classga oid xususiyat va metodlar

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


#avto1 = Avto("GM", "Malibu", "Qora", 2025, "60000", 1000)
#print(avto1.model)
#print(avto1.get_km())
#print(avto1.get_id())

#avto1.add_km(1000)
#print(avto1.get_km())

avto1 = Avto("GM", "Malibu", "Qora", 2025, "60000", 1000)
avto2 = Avto("GM", "Lacetti", "Qora", 2025, "50000", 1400)
avto3 = Avto("GM", "Nexia-3", "Qora", 2025, "40000", 1800)
print(Avto.get_num_avto())
