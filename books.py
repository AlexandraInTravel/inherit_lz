#задание 5
class Book: #родительский класс
    def __init__(self, title, author, year): #конструктор
        self.title = title
        self.author = author
        self.year = year

    def info(self): #метод, который выводит информацию о книге
        print('Название книги:', self.title)  
        print('Автор книги:', self.author)
        print('Год выпуска книги:', self.year)
    
    def is_actual(self): #метод, проверяющий актуальность книги
        a = 2026 - self.year #будем сравнивать с 2026 годом
        if a > 5: #если больше 5 лет, то
            print('Книга уже не актуальна')
        else: #в другом случае
            print('Книга актуальна')


class EBook(Book): #дочерний класс
    def __init__(self, title, author, year, file_size, format,free): #конструктор
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format
        self.free=free

    def info(self): #расширение информации о книге
        super().info() #наследование из родительского класса в дочерний метода info()
        print('Размер книги:', self.file_size)
        print('Формат книги:', self.format)
    def is_available(self): #метод, который проверяет: книга электронная (есть в наличии) или бумажная (нет в наличии)
        if self.format=='электронный':
            print('Есть в наличии')
        elif self.format == 'бумажный':
            print('Нет в наличии')
        else:
            print('Неверный формат книги')

    def is_free(self): 
        if self.free == 'да':
            print('Книгу можно получить бесплатно')
        elif self.free == 'нет':
            print('Книгу нельзя получить бесплатно')
        else:
            print('Неверный статус получения книги')

    def actual(self): #доп метод
        super().is_actual() #наследование 


