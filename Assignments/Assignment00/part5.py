class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def celebrate_birthday(self):
        self._age += 1


    def reset_birthday(self):
        self._age = 0
    
    
    def __str__(self):
        return "Person name is {}, age is {}".format(self._name, self._age)

# Run some tests on the method
chris = Person("chris", 31)
chris.reset_birthday()
for i in range(32):
  chris.celebrate_birthday()
print(chris)