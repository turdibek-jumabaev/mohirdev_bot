class talaba:
    def __init__(self, ism, familiya, t_yil):
        self.name = ism
        self.surname = familiya
        self.borthday = t_yil

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self, yil=2022):
        return yil-self.t_yil


talaba1 = talaba('habib', 'hamroyev', 2007)
talaba2 = talaba("elbek", "hamroyev", 2003)
print(talaba1.get_surname())
