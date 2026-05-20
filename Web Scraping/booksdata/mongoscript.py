from pymongo import MongoClient
import datetime

client  = MongoClient("mongodb+srv://amit:amit2005@cluster0.fbr8pud.mongodb.net")

db = client.books_scrape
posts = db.books

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

post_id = posts.insert_one(post).inserted_id

print(post_id)
print(posts)