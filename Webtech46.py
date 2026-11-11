class FamilyMember:
    def __init__(self, eye_color, height):
        self.eye_color = eye_color
        self.height = height

    def show_traits(self):
        print("Eye Colour:", self.eye_color)
        print("Height:", self.height)

class kid(FamilyMember):
     def __init__(self, name, age, eye_color, height):
         self.name = name
         self.age = age
         super(). __init__(eye_color, height)  

     def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()


     def favourite_hobby(self, hobby):
         print(self.name, "love", hobby)

child = kid("Maya", 10, "brown", 140)


child.show_traits()
child.favourite_hobby("Sketching")

print("Is Kid a subclass?", issubclass(kid, FamilyMember))



