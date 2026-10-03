#TO DO: import your Dog class and your Rescue class from their respective files that you create
import random
from animals import Dog
from businesses import Rescue

#TO DO: create an instance of your Rescue class

my_rescue = Rescue()

#TO DO: set the capacity of the Rescue class to 20

Rescue.set_capacity(20)

print(Rescue.capacity)

breed_options = ["Retriever", "Lab", "Poodle", "Dachshund", "Mutt"]
colors = ["Blue", "Brown", "Gray", "Black", "White", "Golden"]

# Add 10 random dogs
for i in range(10):
    breed = random.choice(breed_options)
    color = random.choice(colors)
    age = random.randint(1,3)
    #TO DO: using the add_dog method you write for your Rescue class, add a new instance of your Dog class to the
    #Rescue using the breed, color, and age randomly generated in the lines above
    random_dog = Dog(breed, color, age)
    Rescue.add_dog(random_dog)


search_dog = Dog("Lab", "Brown", 2)

print("You are looking for a ", search_dog.color,
      search_dog.breed, " that is ", str(search_dog.year) + " years old.")
print()

# flag for dog availability
is_dog_available = False

# search through your rescue's inventory and compare each dog in inventory to the search_dog variable.
# If they are equal, then change the dog availability flag to true and break out of the search
    
if is_dog_available:
    print("We have that dog available!")
else:
    print("We don't have that dog available, sorry!")
