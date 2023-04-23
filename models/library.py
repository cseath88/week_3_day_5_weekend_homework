from models.book import *

book1 = Book("Blood Meridian", "Cormac McCarthy", "Western", checked_out=True)
book2 = Book("City Of Thieves", "David Benioff", "Historical Fiction", checked_out=True)
book3 = Book("American Kingpin", "Nick Bilton", "True Crime", checked_out=False)

library = [book1, book2, book3]

def add_new_book(book):
    library.append(book)

def delete_book(book_name):
    book_to_delete = None
    for book in library:
        if book.title == book_name:
            book_to_delete = book
            break

    library.remove(book_to_delete)