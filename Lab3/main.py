from pyDatalog import pyDatalog;
import random;
pyDatalog.create_terms('sumr, median, srr, proiz, result, N');

f = open('output.txt','w')

#Задание 1 (сумма ряда)
sumr[N] = N + sumr[N-1];
sumr[1] = 1;
print('Сумма ряда ')
print(sumr[100] == N);
check = "Сумма ряда: " + (str)(sumr[100] == N) + '\n' + '--'*5 + '\n'*2
f.write(check)

#Задание 2 (среднее значение ряда)
srr[N] = (1 + N) / 2;
print('\nСреднее значение ряда')
print(srr[100] == N);
check = "Среднее значение ряда: " + (str)(srr[100] == N) + '\n' + '--'*5 + '\n'*2
f.write(check)

#Задание 3 (произведение некоторого кол-ва случайных чисел)
proiz[N] = random.randint(1, 100) * proiz[N - 1];
proiz[0] = 1;
print('\nПроизведение некоторого кол-ва случайных чисел')
print(proiz[100] == N);
check = "Произведение некоторого кол-ва случайных чисел: " + (str)(proiz[100] == N) + '\n' + '--'*5 + '\n'*2
f.write(check)

#Задание 4 (медиана  некоторого кол-ва случайных чисел)
result[N] = random.randint(1, 100) + result[N - 1];
result[0] = 0;
median[N] = result[N] / N;
print('\nМедиана')
print(median[100] == N);
check = "Медиана: " + (str)(median[100] == N) + '\n' + '--'*5 + '\n'*2
f.write(check)
f.close()
