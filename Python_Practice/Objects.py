class Person:
  
  # constructor (creates objects)
  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height
    
   # destrcutor (deletes objects)
   # not used often
   def __del__(self):
    print("Object deleted!")
    
   # type-cast into a string 
   def __str__(self):
    return ("Name: (), Age: (), Height: ()".format(self.name, self.age, self.height))
    
    
person1 = ("Elvin", 25, 170)
print(person1.name)
print(person1.age)
print(person1.height)

# person1.name = "Geek"
# print(person1.name)

# del person1

print(person1)




# ------------ PART 2 ---------------------


  # class variables, not unique for each object but are the same value for each object
  # global variable
  amount = 0
  

  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height
    Person.amount += 1 #when you access Person you access the whole class vs Person1 which access the object
    
  def __del__(self):
    Person.amount -= 1
    
   # type-cast into a string 
   def __str__(self):
    return ("Name: (), Age: (), Height: ()".format(self.name, self.age, self.height))
    
    
    
    # this is a function, (so far defining attributes)
    def get_older(years):
      self.age += years
    
    
    
 person 1 = Person("Elvin", 25, 170)
 print(person1)
 
 person2 = Person("Tiffany", 24, 165)
 del person2 # if you delete person2 amount will be 1
 
 print(Person.amount) # when you add person 2 it will output 2 for amount
