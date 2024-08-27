import pandas as pd


filename = 'data.csv'
df = pd.read_csv(filename)


print(df)


import pandas as pd

# Чтение данных из CSV-файла
csv_file = 'data.csv'  # Замените 'data.csv' на ваш файл
df = pd.read_csv(csv_file)

# Преобразование данных в JSON и запись в файл
json_file = 'data.json'  # Имя выходного JSON-файла
df.to_json(json_file, orient='records', lines=True, force_ascii=False)

print(f'Данные успешно сохранены в {json_file}')

# df.to_json(json_file, orient='index')  # Преобразует строки в словари с индексами в качестве ключей
