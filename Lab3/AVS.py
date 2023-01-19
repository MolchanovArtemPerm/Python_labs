# Среднее значение ряда
from pyDatalog import pyDatalog 
pyDatalog.create_terms('N, AVS')

AVS[N] = (N + 1)/2
print(AVS[100]==N)