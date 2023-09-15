class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):
        
        self.radius = radius
        self.area = radius * radius * Circle.pi #or self.pi

    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle  = Circle(30)

new = my_circle.radius
area = my_circle.area


new2 = my_circle.get_circumference()
print(new2)
print(area)
print(new)