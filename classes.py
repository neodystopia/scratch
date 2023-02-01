class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sayHello(self):
        print ("Hello, World!")

    def sayName(self):
        print (f"My name is {self.name}")

    
# create an instance of the Person Class to create an object
randomPerson = Person("Myles Nichols", 7)

# checking attributes thru dot notation
print("Name of the person: " + randomPerson.name)
print("Age of the person: " + str(randomPerson.age) + " years")

randomPerson.sayHello()
randomPerson.sayName()