class Parrot:
    #   class attribute
      species = "bird"

    #   instance attribute
     def __init__(self,name,age):
     self.name = name
     self.age = age


# instace of parrot

blu = Parrot("blu", 10)
woo = Parrot("woo", 15)


# access class attribute
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))

# access the instance atrribute
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))




