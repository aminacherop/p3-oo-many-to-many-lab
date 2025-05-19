
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("name must be a string")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __str__(self):
        return f"Author: {self.name}"

class Book:
    def __init__(self,title):
        self.title = title
        
    def contracts(self):
     return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
     return [contract.author for contract in Contract.all if contract.book == self]


   # pass

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [contract for contract in cls.all if contract.date == date]
    
    def __repr__(self):
     return f"Contract(author={self.author.name}, book={self.book.title}, date='{self.date}', royalties={self.royalties})"

    

a1 = Author("Alice")
b1 = Book("Book A")
b2 = Book("Book B")

Contract(a1, b1, "2025-01-01", 1000)
Contract(a1, b2, "2025-01-01", 2000)

print(Contract.contracts_by_date("2025-01-01"))  

