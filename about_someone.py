class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."
    
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! mehrish  {self.age} years old."


if __name__ == "__main__":
    
    person1 = Person("mehrish", 13)

    print(person1.introduce())
    print(person1.have_birthday())
    