import csv

from ..models import Post, Book


DUMP_PATH = r'C:\Users\15314\source\repos\MySite\MySite\blog\data\data_dump'

def export_books():
    """Export books into a csv file"""

    book_fields = [field.name for field in Book._meta.fields] # Gets data base field names
    all_books = Book.objects.all()
    
    all_books_data = []
    for book in all_books:
        this_book_data = []
        for field in book_fields:
            field_value = getattr(book, field)
            this_book_data.append(field_value)
        all_books_data.append(this_book_data)

    with open(DUMP_PATH + r'\books.csv', 'w', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(book_fields) # Column headers
        writer.writerows(all_books_data)
