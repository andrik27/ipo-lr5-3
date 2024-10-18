ttt = open('text.txt','r', encoding="utf-8").read() #Открываем и читаем файл
words = ttt.split()  # Разделяем строку на слова по пробелам
print("Количество слов:", len(words))  # Вывод на экран