
import sqlite3
from django.utils.text import slugify 
from ..models import Post



def import_sql():
    """Import a sql db into the django sql model"""
    

    conn = sqlite3.connect(r'C:\Users\15314\OneDrive\Desktop\MySite\MySite\scrapey.db')
    cur = conn.cursor()
    query = cur.execute("""SELECT * FROM Scrape_Posts LIMIT 3""")

    for row in query:
        new_post = Post()
        new_post.date = row[1]
        new_post.title = row[2]
        new_post.author = row[3]
        new_post.body = row[4]
        new_post.url = row[5]                
        new_post.website = row[6]
        new_post.name = row[7]
        new_post.slug = slugify(new_post.title)
        new_post.save()
