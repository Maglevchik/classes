class Library:
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' добавлена в библиотеку.")

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"'{book_name}' удалена из библиотеки.")
        else:
            print(f"Ошибка: '{book_name}' нет в библиотеке.")

    def display_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            print("Книги в библиотеке:")
            for book in self.books:
                print(f"- {book}")
    
    def __init__(self):
        self.books = []

#Создаём экземпляр библиотеки
my_library = Library()

print("--- Изначальное состояние библиотеки ---")
my_library.display_books() 

print("\n--- Добавляем книги ---")
my_library.add_book("Мастер и Маргарита")
my_library.add_book("Властелин колец")
my_library.add_book("Путешествие в стране солнечных зайчиков")

print("\n--- Текущие книги в библиотеке ---")
my_library.display_books()

print("\n--- Удаляем книгу ---")
my_library.remove_book("Властелин колец")

print("\n--- Пробуем удалить несуществующую книгу ---")
my_library.remove_book("Нарния")

print("\n--- Окончательный список книг ---")
my_library.display_books()