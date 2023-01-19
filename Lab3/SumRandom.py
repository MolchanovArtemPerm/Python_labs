# Сумма ряда случайных чисел [1,100]
from pyDatalog import pyDatalog 
import random
pyDatalog.create_terms('N, arrRandom')

arrRandom[N] = random.randint(1,100) + arrRandom[N - 1]
arrRandom[1] = random.randint(1,100)
print(arrRandom[100]==N)
