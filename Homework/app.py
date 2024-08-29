import pandas as pd

filename = 'color_srgb.csv'
df = pd.read_csv(filename)

# print(df.tail(3))
# print(df.head(3))
# print(df.info)

json_file = 'color_srgb.json'  # Имя выходного JSON-файла
df.to_json(json_file, orient='records', lines=True, force_ascii=False)

print(f'Данные успешно сохранены в {json_file}')