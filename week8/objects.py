class Book:
    def __init__(self, name, serialNumber):
        self.name = name
        self.serialNumber = serialNumber
    def getName(self):
        return self.name


class Person:
    def __init__(self, name, id, age, book):
        self.name = name
        self.id = id
        self.age = age
        self.book = book
        
    def getPersonName(self):
        return self.age
    
    def ageIn2030(self):
        return 5+self.age
    
    def ageInYears(self, years):
        return years+self.age
    def getBookDetails(self):
        return f"{self.name} favourite book is {self.book.getName()}"


book1 = Book("Harry Potter", 12345)
print(book1.getName())   
tom = Person("Tom", 1234, 20, book1)
# tom2 = Person("Tom", 1234, 20)
ben = Person("Ben", 1000, 50, book1)
# print(tom.ageIn2030())
# print(ben.ageIn2030())
print(tom.getBookDetails())