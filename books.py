#задание 5
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self): 
        print('Название книги:', self.title)  
        print('Автор книги:', self.author)
        print('Год выпуска книги:', self.year)
    
    def is_actual(self):
        a = 2026 - self.year
        if a > 5:
            print('Книга уже не актуальна')
        else:
            print('Книга актуальна')


class EBook(Book):  
    def __init__(self, title, author, year, file_size, format,free):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format
        self.free=free

    def info(self):
        super().info()
        print('Размер книги:', self.file_size)
        print('Формат книги:', self.format)
    def is_available(self):
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

    def actual(self):
        super().is_actual()


