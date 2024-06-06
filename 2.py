import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100
data1 = np.random.rand(num_samples)
data2 = np.random.rand(num_samples)

# Построение диаграммы рассеяния
plt.scatter(data1, data2, color='blue', alpha=0.5)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Данные 1')
plt.ylabel('Данные 2')

# Показ графика
plt.show()