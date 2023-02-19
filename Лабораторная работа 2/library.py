BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int = None, name: str = None, pages: int = None):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return 'Книга ' + '"' + self.name + '"'

    def __repr__(self) -> str:
        return self.__class__.__name__ + f"(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Library
class Library:
    def __init__(self, books: list = []):
        self.books = books

    def get_next_book_id(self) -> int:
        if len(self.books) != 0:
            return self.books[-1].id + 1
        else:
            return 1

    def get_index_by_book_id(self, id_: int):
        for book_ in enumerate(self.books):
            if book_[1].id == id_:
                return book_[0]
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
