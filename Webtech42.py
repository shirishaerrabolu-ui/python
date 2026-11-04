
class Parrot:

    species = "bird"


    def __init__(self, name, age):
        self .name = name
        self .age = age

blu = Parrot("Blu", 10)
Wu = Parrot("Wu", 15)


print("Blu is a {}".format(blu.species))
print("Wu is a {}".format(Wu.species))

print("{} is {}".format(blu.name, blu.age))        
print("{} is {}".format(Wu.name, Wu.age))        