class Parrot:
    #   class attribute
      species = "bird"

    #   instance attribute
     def __init__(self,name,age):
     self.name = name
     self.age = age

    # instance method
    def sing(self,song):
        return"{} sing {}".format(self.name, song)
    def dance(self,dance):
        return"{} dances".format(self.name,) 

 blu parrot("blu", 10)

print( blu.sing("summertime sadness")) 
print(blu.dances())




# instace of parrot

blu = Parrot("blu", 10)
woo = Parrot("woo", 15)


# access class attribute
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))

# access the instance atrribute
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))




