def shou_data() -> None:
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')

def find_data() -> None:
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print(search(tel_book, data))

def search(book: str, info: str) -> str:
    book = book.split('\n')
    return '\n' .join([post for post in book if info in post])

def change_data() -> None:
    with open('book.txt', 'r', encoding='utf-8') as f:
        a = (f.read().split('\n'))
        for index, value in enumerate(a, 1):
            print(index, value) 
        x = int(input('Введите номер удаляемой записи: '))              
        a.pop(x-1)
        temp = ("\n".join(a))
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{temp}')

