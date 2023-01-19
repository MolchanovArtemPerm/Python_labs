import person
class Client(person.Person):
    def __init__(self, surname : str = "NOVALUE", name : str = "NOVALUE", patronymic : str = "NOVALUE", age : int = 0, purchase : str = "NOVALUE"):
        super().__init__(surname, name, patronymic, age);
        self.purchase = purchase;

    def __str__(self) -> str:
        return super().__str__() + f"\tЗаказ: {self.purchase}";

    def __repr__(self)-> str:
        return "Client: " + self.__str__();