# Python Lesson 2
#
# 1. Версии packedge
    pip install icecream
    или 
    pip install ucecream == 2.1.1

# 2. Environment (Virtualenv)

    1. Создаем виртуальную среду
    py install virtualenv
    py  -m virtualenv env
    2. Включаем
    .\env\Scripts\active
    3. Добавляем еще packadge
    4. Coхраняем в файл txt
    pip freeze > requirements.txt
    5. обновить путь к этому файлу в случае удаления папки с надстройками
    сначала сделать пункт 1 и 2
    потом:
    pip install - r.\requirements.txt

# 3. Pip list 
## показывает какие надстройки установлены

# 4. Terminal (Path)
## cd
## .. 
## cd\
## dir
## .

# 4. Debbuger  F5

# 5. Enum

# 6. Enumerate

# 7. Python 
## List - это упорядоченная изменяемая коллекция объектов в Python. Списки могут содержать элементы любых типов данных (например, числа, строки, другие списки) и поддерживают индексацию и срезы.
    # Создание списка
    my_list = [1, 2, 3, 4, 5]

    # Добавление элемента в список
    my_list.append(6)

    # Доступ к элементу по индексу
    print(my_list[2])  # Вывод: 3

    # Изменение значения элемента по индексу
    my_list[1] = 10

    # Удаление элемента
    my_list.remove(10)

    print(my_list)  # Вывод: [1, 3, 4, 5, 6]

## Tuple - это упорядоченная неизменяемая коллекция объектов. Как и списки, кортежи могут содержать элементы любых типов данных, но в отличие от списков, кортежи неизменяемы (их нельзя модифицировать после создания).
    # Создание кортежа
    my_tuple = (1, 2, 3, 4, 5)

    # Доступ к элементу по индексу
    print(my_tuple[1])  # Вывод: 2

    # Попытка изменить элемент (вызовет ошибку)
    # my_tuple[1] = 10  # Ошибка: 'tuple' object does not support item assignment

    # Использование кортежа для возврата нескольких значений из функции
    def get_coordinates():
        return (10.0, 20.0)

    x, y = get_coordinates()
    print(x, y)  # Вывод: 10.0 20.0

## Dictionary - это неупорядоченная коллекция пар "ключ-значение". Ключи в словаре уникальны и могут быть объектами неизменяемых типов данных (например, строки, числа), а значения могут быть любыми объектами.
    # Создание словаря
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

    # Доступ к значению по ключу
    print(my_dict['name'])  # Вывод: Alice

    # Добавление новой пары ключ-значение
    my_dict['email'] = 'alice@example.com'

    # Изменение значения по ключу
    my_dict['age'] = 26

    # Удаление пары ключ-значение
    del my_dict['city']

    print(my_dict)  # Вывод: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

    # Перебор ключей и значений
    for key, value in my_dict.items():
        print(f'{key}: {value}')


# 8. CSV 
# 9. Pandas
## df - dataframe
## import pandas as pd
        filename = 'data.csv'
        df = pd.read_csv(filename)

        print(df.tail(8))

### .tail  конец списка
### .head начало списка
### .info информация о файле

# 10. Cоздать из файла csv  файл Json

    import pandas as pd

    # Чтение данных из CSV-файла
    csv_file = 'data.csv'  # Замените 'data.csv' на ваш файл
    df = pd.read_csv(csv_file)

    # Преобразование данных в JSON и запись в файл
    json_file = 'data.json'  # Имя выходного JSON-файла
    df.to_json(json_file, orient='records', lines=True, force_ascii=False)

    print(f'Данные успешно сохранены в {json_file}')

# 11.  Открыть файл csv в терминале  
## пример 1
        import pandas as pd


        filename = 'data.csv'
        df = pd.read_csv(filename)


        print(df)

## # Преобразует строки в словари с индексами в качестве ключей
        # df.to_json(json_file, orient='index')  

# 12. DataBases
## - Oracle
## - Microsoft
## - IBM 

# 13. SQL управление базами данных
##  DDl data Definition Langurdge используется для определения и управления структурой базы данных
### create
### drop
### alter

## DML Data Manipulation Language используется для манипуляции данными в таблицах.

## Select
    SELECT * From CUstomers   ## столбцы
## Where
    Where Country = "Germany"  ## строки

    

