class Person:
    global_variable = "Hey There"
    def __init__(self, name, age, fav_col):
        self.name = name
        self.age = age
        self.fav_col = fav_col

    def displayInfo(self):
        print("Your name is ", self.name, " , age is ", self.age, ", and favourite color is", self.fav_col)

p1 = Person("Ephraim", 32, "Green")
p1.displayInfo()
print(p1.global_variable)