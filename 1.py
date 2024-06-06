import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.hist(data, bins='auto', alpha=0.75, color='blue', edgecolor='black')
plt.title('Гистограмма случайных данных')
plt.xlabel('Значения')
plt.ylabel('Частота')

# Добавление кривой нормального распределения
x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 1000)
p = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
plt.plot(x, p, 'r-', linewidth=2)

# Показ графика
plt.show()