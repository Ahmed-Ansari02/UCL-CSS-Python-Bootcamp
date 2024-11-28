class Person:
    def __init__(self, name, id, age):
        self.personName = name
        self.personId = id
        self.personAge = age
        
    def getPersonName(self):
        return self.personName
    
    def ageIn2030(self):
        return 5+self.personAge
    
    def ageInYears(self, years):
        return years+self.personAge
    
tom = Person("Tom", 1234, 20)
# tom2 = Person("Tom", 1234, 20)
ben = Person("Ben", 1000, 50)
# print(tom.ageIn2030())
# print(ben.ageIn2030())
print(tom.ageInYears(10))