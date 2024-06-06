import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import matplotlib.pyplot as plt

def replace_price(price):
    price = price.replace(' ', '').replace('.', '').replace('руб', '')
    return int(price)

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("https://www.divan.ru/category/divany-i-kresla")

# Подождем, пока страница полностью загрузится
time.sleep(3)

# Нахождение всех элементов с информацией о светильниках
divans = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

with open('divan_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена'])  # Заголовки столбцов

    # Парсинг информации о каждом светильнике и запись в CSV файл
    for divan in divans:
        name = divan.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = divan.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        writer.writerow([name, price])

print("Данные успешно сохранены в divan_prices.csv")

# Чтение данных из CSV файла
df = pd.read_csv('divan_prices.csv')

# Очистка данных в столбце 'Цена'

df['Цена'] = df['Цена'].apply(replace_price)

# Сохранение изменений в CSV файл
df.to_csv('divan_prices.csv', index=False)

print("Данные успешно обновлены в divan_prices.csv")

# Расчет средней цены
average_price = df['Цена'].mean()
print(f'Средняя цена на диваны: {average_price:.2f} ₽')

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=20, edgecolor='black')
plt.title('Распределение цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(True)
plt.savefig('price_histogram.png')
plt.show()