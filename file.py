#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt

with open('referat.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(len(content))
    words = len(content.split())
    print(words)

    with open('referat.txt', 'r', encoding='utf-8') as f:
        with open('referat2.txt', 'w', encoding='utf-8') as f2:
            for ln in f:
                ln = ln.replace('.', '!')
                f2.write(ln)