#Медиана ряда случайных чисел
from pyDatalog import pyDatalog
import random
pyDatalog.create_terms('N, arrRandom2, arrRandomMedian')

arrRandom2[N] = random.randint(1,100) + arrRandom2[N - 1]
arrRandom2[1] = random.randint(1,100)
arrRandomMedian[N] = arrRandom2[N] / N
print(arrRandomMedian[100] == N)
