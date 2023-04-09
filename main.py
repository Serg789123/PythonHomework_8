import function

while True:
    print('1. ввод, 2. добавление, 3. поиск, 4. изменение')
    mode = int(input())
    if mode == 1:
        function.shou_data()
    elif mode == 2:
        function.add_data()
    elif mode == 3:
        function.find_data()
    elif mode == 4:
        function.change_data()
    else:
        break

with open('book.txt', 'w', encoding='utf-8') as f:
    f.write('фио | номер телефона')

with open('book.txt', 'a', encoding='utf-8') as f:
    f.write('\nфио1 | номер телефона1')

with open('book.txt', 'r', encoding='utf-8') as f:
    f.print(f.read())