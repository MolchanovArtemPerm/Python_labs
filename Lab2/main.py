from company import *
from employee import *
from client import *
from person import *

company = Company("ДНС", 
    [
        Employee("Молчанов", "Артем", "Андреевич", 20, 40000),
        Employee("Возисов", "Максим", "Игоревич", 19, 30000)
    ], 
    [
        Client("Фищев", "Андрей", "Михайлович", 19, "Asus VivoBook"),
        Client("Харцызов", "Михаил", "Григорьевич", 25, "MSI TITAN GT77"),
        Client("Ложкин", "Максим", "Игоревич", 20, "Apple TV")
    ]);
SerializeCompany(company, "test.json");
print(company);
deserialized = DeserializeCompany("test.json");
print(deserialized);
