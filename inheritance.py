class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.ratings = 0 #set ratings to 0 by default

    def get_book_details(self):
        book = {
            "name": self.name,
            "author": self.author,
            "ratings" : self.ratings
        }

        return book

    # update ratings of the book 
    def __update_ratings__(self,rating):
        self.ratings = rating

#A SubCategory of books is SelfImprovementBooks(inherited class)
class SelfImprovementBooks(Book):
    def __init__(self,topic):
        super().__init__
        self.type = "selfImprovement"
        self.deals_with = topic

    def get_ratings(self):
        self.ratings 
    
    # add some more details to super class(Book) attributes
    def get_book_details(self):
        details = super().get_book_details
        details["type"] = self.type
        details["deals_with"] = self.deals_with

    
book1 = Book("AnimalFarm","George Orwell")
print(book1.get_book_details())
book2 = SelfImprovementBooks("psychology")
print(book2.get_book_details())