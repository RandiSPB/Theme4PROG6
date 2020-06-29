# Программирование (Python)
# 6 семестр, тема 1

# Лабораторная работа 2

"""

Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), визуализируйте данные стоимости билетов пассажиров.

"""

import pandas  # импортирование библиотеки для считывания данных
import matplotlib.pyplot as plt # импорт библиотеки для отрисовки графика 
import numpy as np # импорт библиотеки для реализации вычислений значений


# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")



prices = data.sort_values('Fare')
prices = prices["Fare"].value_counts()

count = prices.tolist()
print(count[0])

x = np.linspace( 0, count[0],  len(count))
y = prices.keys()


fig = plt.figure()
ax = fig.add_subplot(111)
plt.xticks(np.arange(0, max(count)+5, 5.0))
plt.yticks(np.arange(0, max(prices.keys()+50), 50.0))
ax.set_xlabel('количество пассажиров купивших  билеты за эту стоимость')
ax.set_ylabel('Стоимость билетов')
ax.scatter(x, y, color = 'black', s = 2)
fig.savefig('graph.png')
