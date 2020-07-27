"""I want to make an easy interface for importing excel files into my models. 
Mainly just the knowledge repo for now."""

import openpyxl
from ..models import Knowledge, Book


IMPORT_PATH = r'C:\Users\15314\source\repos\MySite\MySite\blog\data\data_dump\websiteDB.xlsx'


def import_knowledge():
    """Take knowledge rec's from excel spreadsheet and upload the to sql database"""
    
    #add ability for it to only update records that are not already in there

    wb = openpyxl.load_workbook(IMPORT_PATH)
    sht = wb['Knowledge']

    for i in range(2, get_last_row(sht, 'B') + 1):
        new_knowledge = Knowledge()
        new_knowledge.author = sht["B" + str(i)].value
        new_knowledge.description = sht["C" + str(i)].value
        new_knowledge.source = sht["D" + str(i)].value
        new_knowledge.save()
        # You must save the model to db before adding tags
        new_knowledge.tags.add(sht["E" + str(i)].value)


def import_books():
    """Take books from excel spreadsheet and upload the to sql database"""
    
    #add ability for it to only update records that are not already in there

    wb = openpyxl.load_workbook(IMPORT_PATH)
    sht = wb['Books']

    for i in range(2, get_last_row(sht, 'B') + 1):
        new_book = Book()
        new_book.book_title = sht["B" + str(i)].value
        new_book.slug = sht["C" + str(i)].value
        new_book.author = sht["D" + str(i)].value
        new_book.cover_description = sht["E" + str(i)].value
        new_book.body = sht["F" + str(i)].value
        new_book.image_name = sht["G" + str(i)].value       
        new_book.created = sht["H" + str(i)].value 
        new_book.save()


def get_last_row(sht, column='A'):
    """Return the last row with data in a worksheet for that column
    This should actually start from the bottom and come up but I am not
    sure how to work backwars other than using some arbitrary big number"""
    
    row = 1
    while sht[f'{column}{row}'].value is not None:
        row += 1
    return row

