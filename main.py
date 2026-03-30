#задание 5
from books import EBook #импорт класса

def main(): #главная функция
    title=input('Введите название книги: ') #данные для программы
    author=input('Введите автора книги: ')
    year=int(input('Введите год выпуска книги: '))
    file_size=input('Введите размер книги (количество страниц): ')
    format=input('Книга в электронном или в бумажном варианте? (электронный/бумажный) ')
    free=input('Можно ли получить книгу бесплатно? (да/нет) ')
    a=EBook(title,author,year, file_size, format, free) #присваивание переменной
    a.info() #вызов функции класса
    a.actual()
    a.is_available()
    a.is_free()
if __name__=='__main__': 
    main()