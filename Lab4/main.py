import csv;
import random;
FILENAME : str = "Data.csv"; # Начальный файл csv с данными
OUTPUTFILE : str = "Data_New.csv"; # Изменяемый файл csv

#Свой map
def OverrideMap(func, sourceList : list) -> list:
    resultList = list();
    for obj in sourceList:
        resultList.append(func(obj));
    return resultList;

#Свой reduce
def OverrideReduce(func, sourceList : list):
    index : int = 2;
    length : int = len(sourceList);
    result = func(sourceList[0], sourceList[1]);
    while(index < length):
        result = func(result, sourceList[index]);
        index += 1;
    return result;

#Генерация списка списков с ФИО и зарплатой человека
def GenerateData() -> list:
    Names : list = ["Артем", "Максим", "Андрей", "Семен", "Иван"];
    Surnames : list = ["Молчанов", "Возисов", "Фищев", "Соколков", "Мазунин"];
    Patronymics : list = ["Андреевич", "Максимович", "Анатольевич", "Олегович", "Сергеевич"];
    Persons = list();
    i : int = 0;
    count : int = 50;
    Persons.append(["ФИО", "Зарплата"]);
    while i < count:
        randomFullName = Surnames[random.randint(0 , len(Surnames) - 1)] + " " + Names[random.randint(0 , len(Names) - 1)] + " "  + Patronymics[random.randint(0 , len(Patronymics) - 1)];
        Persons.append([randomFullName, random.randint(1, 1000) * 1000]);
        i += 1;
    return Persons;
   
#Запись в csv из списка списков
def WriteInCSVFromList(dataSet : list, fileName : str):
     with open(fileName, "w", newline="") as file:
        writer = csv.writer(file, delimiter=',');
        writer.writerows(dataSet);

#Запись в csv из списка словарей        
def WriteInCSV(dataSet : list, fileName : str):
    with open(fileName, "w", newline="") as file:
        columns = list(dataSet[0].keys());
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',');
        writer.writeheader();   
        writer.writerows(dataSet);

#Чтение из csv в виде списка словарей
def ReadFromCSV(fileName : str) -> list:
    with open(fileName, "r", newline="") as file:
        reader = csv.DictReader(file);
        resultListDict = list();
        for dict in reader:
            resultListDict.append(dict);        
    return resultListDict;

#Разрезание записи с ключом ФИО на 3 отдельных
def SplitFullName(sourceDict : dict) -> dict:
    resultDict = dict();
    strs = sourceDict["ФИО"].split(' ');
    resultDict["Фамилия"] = strs[0];
    resultDict["Имя"] = strs[1];
    resultDict["Отчество"] = strs[2];
    resultDict["Зарплата"] = sourceDict["Зарплата"];
    return resultDict;

def GetSum(sourceDict1 : dict, sourceDict2 : dict) -> dict:
    resultDict = dict();
    resultDict["Зарплата"] = int(sourceDict2["Зарплата"]) + int(sourceDict1["Зарплата"]); 
    return resultDict;

#Генерация начального файла csv
WriteInCSVFromList(GenerateData(), FILENAME);

#Разрезать столбец ФИО с помощью map и записывать в csv
dataSet : list = ReadFromCSV(FILENAME);
newDataSet : list = OverrideMap(SplitFullName, dataSet);
WriteInCSV(newDataSet, OUTPUTFILE);

#Подсчёт суммы с помощью reduce
salarySum = OverrideReduce(GetSum, dataSet)["Зарплата"];
print("Сумма всех зарплат в файле: " + str(salarySum));
