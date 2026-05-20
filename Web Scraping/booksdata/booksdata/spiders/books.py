import scrapy
from pymongo import MongoClient
import datetime

client  = MongoClient("mongodb+srv://amit:amit2005@cluster0.fbr8pud.mongodb.net")
db = client.books

def save_to_mongo(page, img, title, price, rating):
    collection = db[page]
    post = {
        "img": img,
        "title": title,
        "price": price,
        "rating": rating,
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }
    inserted = collection.insert_one(post)
    print(inserted.inserted_id)
    
    return inserted.inserted_id


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://toscrape.com"]
    
    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
            "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
            
        self.log(f"Saved file {filename}")
        
        cards = response.css(".product_pod")
        
        for card in cards:
            img = card.css(".image_container img::attr(src)").get()
            title = card.css("h3 a::attr(title)").get()
            price = card.css(".price_color::text").get()
            rating = card.css(".star-rating::attr(class)").get()
            
            # yield {
            #     "img": img,
            #     "title": title,
            #     "price": price,
            #     "rating": rating.split()[-1],
            # }
            save_to_mongo(page, img, title, price, rating)
        pass
