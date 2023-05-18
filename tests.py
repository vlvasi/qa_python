from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book(self):
        books_collector = BooksCollector()

        books_collector.add_new_book("The Great Gatsby")
        assert books_collector.get_books_rating == {"The Great Gatsby": 1}


    def test_set_book_rating(self):
        books_collector = BooksCollector()

        books_collector.add_new_book("The Great Gatsby")
        books_collector.set_book_rating("The Great Gatsby", 8)
        assert books_collector.get_book_rating("The Great Gatsby") == 8

    def test_get_books_with_specific_rating(self):

        books_collector = BooksCollector()

        books_collector.add_new_book("The Great Gatsby")
        books_collector.add_new_book("1984")
        books_collector.add_new_book("Animal Farm")

        books_collector.set_book_rating("The Great Gatsby", 8)
        books_collector.set_book_rating("1984", 6)
        books_collector.set_book_rating("Animal Farm", 6)

        assert books_collector.get_books_with_specific_rating(6) == ["1984", "Animal Farm"]

     def test_get_books_rating(self):
        books_collector = BooksCollector()

        books_collector.add_new_book("The Great Gatsby")
        books_collector.add_new_book("1984")
        books_collector.add_new_book("Animal Farm")

        books_collector.set_book_rating("The Great Gatsby", 8)
        books_collector.set_book_rating("1984", 6)
        books_collector.set_book_rating("Animal Farm", 6)

        # Получаем словарь books_rating
        assert books_collector.get_books_rating() == {
            "The Great Gatsby": 8,
            "1984": 6,
            "Animal Farm": 6
        }

    def test_add_book_in_favorites(self):
        books_collector = BooksCollector()

        books_collector.add_new_book("The Great Gatsby")
        books_collector.add_new_book("1984")

        books_collector.add_book_in_favorites("The Great Gatsby")
        assert books_collector.get_list_of_favorites_books() == ["The Great Gatsby"]


    def test_delete_book_from_favorites(self):

        books_collector = BooksCollector()

        books_collector.add_new_book("The Great Gatsby")
        books_collector.add_new_book("1984")

        books_collector.add_book_in_favorites("The Great Gatsby")
        books_collector.delete_book_from_favorites("The Great Gatsby")
        assert books_collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        books_collector = BooksCollector()

        books_collector.add_new_book("The Great Gatsby")
        books_collector.add_new_book("1984")

        books_collector.add_book_in_favorites("The Great Gatsby")
        books_collector.add_book_in_favorites("1984")

        assert "The Great Gatsby" in books_collector.get_list_of_favorites_books()




