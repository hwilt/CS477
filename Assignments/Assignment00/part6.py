class Person:
    num_people = 0 # static variable

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person.num_people += 1
    
    def celebrate_birthday(self):
        self._age += 1
    
    def __str__(self):
        return "Person name is {}, age is {}".format(self._name, self._age)



# Run some tests on the method
chris = Person("chris", 31)
celia = Person("celia", 30)
james = Person("james", 23)
brock = Person("brock", 80)
print("Person.num_people = ", Person.num_people)