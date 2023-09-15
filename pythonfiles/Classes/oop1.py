class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species ='mammal'

    def __init__(self,breed, name):

        # Attributes
        # We take in the arguement
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        
    

    # METHODS ARE LIKE OPERATIONS / ACTIONS
    def bark(self, number):
        print(f"WOOF! My name is {self.name} and my number is {number}")


my_dog = Dog('Lab','Frankie')

new = my_dog.species
my_dog.bark(2)

print(new)


