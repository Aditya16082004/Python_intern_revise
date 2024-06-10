#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Parent class
class Animal:
    def _init_(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
# Child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating objects of the subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!


# In[ ]:


try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This block always executes.")

# Custom Exception
class CustomError(Exception):
    def _init_(self, message):
        self.message = message
    
    def _str_(self):
        return self.message

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)


# In[ ]:




