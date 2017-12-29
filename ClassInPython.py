class person:
    __Name=""
    __Email=""

    def set_Name(self, Name):
        self.__Name = Name
    def get_Name(self):
        return self.__Name

    def set_Email(self, Email):
        self.__Email = Email
    def get_Email(self):
        return self.__Email

a = person()
a.set_Name("Rameez")
a.set_Email("rameez@gmail.com")

print(a.get_Name() + "\n" + a.get_Email())