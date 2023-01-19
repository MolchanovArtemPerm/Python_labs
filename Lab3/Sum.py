#Посчитать сумму ряда 
from pyDatalog import pyDatalog 
pyDatalog.create_terms('arrSum, N')

arrSum[N] = N + arrSum[N-1];
arrSum[1] = 1;
print(arrSum[100]==N);
