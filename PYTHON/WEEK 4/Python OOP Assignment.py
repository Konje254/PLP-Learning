class Person:
    global_variable = "Hey There"
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("Your name is ", self.name, " , age is ", self.age, ", and you are", self.gender, ". Welcome to PLP")

p1 = Person("Ephraim", 32, "Male")
p1.introduce()
