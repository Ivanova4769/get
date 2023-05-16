import matplotlib
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['font.family'] = 'montserrat'
fig, ax = plt.subplots()
data = []
#d = float(input('ведите частоту отображений маркеров: '))
# Запись данных из файлов
with open('data.txt', 'r') as f:
    data = list(map(int, f.readlines()))
with open('settings.txt', 'r') as f:
    ch_disc = float(f.readline())
    shag_kvant = float(f.readline())

zar_time = 24.21
raz_time = 35.79
all_time = zar_time + raz_time

if data != []:
    # Построение графика
    x = np.array([i * all_time / len(data) for i in range(len(data))])
    y = np.array([i / 256 * 3.3 for i in data])
    plt.plot(x, y, c='blue', label='V(t)', linewidth=1)
    plt.scatter(x[0:x.size:20], y[0:y.size:20], marker='o', c='blue', s=25)
    plt.xlabel('Время, с', fontsize=20)
    plt.ylabel('Напряжение, В', fontsize=20)
    ax.minorticks_on()
    ax.grid(True, which='both')
    ax.grid(which='major', color='k', linewidth=1)
    ax.grid(which='minor', color='k', linestyle=':')
    plt.title('Процесс заряда и разряда конденсатора в RC-цепочке ', fontsize=20, wrap=True, pad=20)
    ax.legend(shadow = False, loc = 'right', fontsize = 30)
    plt.axis([round(min(x), 1), round(max(x), 1), round(min(y), 1), round(max(y), 1)])
    ax.text(41.1, 2.1, 'Время заряда = {} с \n\nВремя разряда = {} с'.format(zar_time, raz_time), fontsize=20)
    plt.show()