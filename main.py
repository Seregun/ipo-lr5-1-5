stroka = input("Введите строку: ") # Ввод строки
indexes = [] # Инициализация списка для хранения индексов вхождения буквы "е"
for i in range(len(stroka)): # Проверка каждого символа в веденной строке
    if stroka[i].lower() == 'е': # Если символ равен "е"        
        indexes.append(i) # Добавление индекса в список indexes
if indexes: # Если список indexes не пустой    
    print("Индексы вхождений буквы 'е' в строке:", indexes) # Вывод всех индексов вхождений буквы "е"
else: # Если буквы "е" нет в строке
    print("Буква 'е' не найдена в строке.") # Вывод об отсутствии буквы "е" в строке
