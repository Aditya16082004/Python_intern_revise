#!/usr/bin/env python
# coding: utf-8

# In[1]:


class ElectronicDevice:
  def __init__(self, brand):
    self.brand = brand

  def turn_on(self):
    print(f"Turning on the {self.brand} device")

class Laptop(ElectronicDevice):
  def __init__(self, brand, model):
    super().__init__(brand)  # Call the parent class constructor
    self.model = model

  def turn_on(self):
    print(f"Booting up {self.brand} {self.model} laptop")

class Smartphone(ElectronicDevice):
  def __init__(self, brand, operating_system):
    super().__init__(brand)
    self.operating_system = operating_system

  def turn_on(self):
    print(f"Waking up {self.brand} smartphone with {self.operating_system}")

# Usage
my_laptop = Laptop("Acme", "X3000")
my_phone = Smartphone("Zenith", "HarmonyOS")

my_laptop.turn_on()  # Output: Booting up Acme X3000 laptop
my_phone.turn_on()  # Output: Waking up Zenith smartphone with HarmonyOS


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


def calculate_area(length, width):
  try:
    area = length * width
  except ZeroDivisionError:
    print("Error: One or both dimensions cannot be zero")
    return None  # Or handle the error differently
  else:
    return area

# Usage
result = calculate_area(5, 3)
print(result)  # Output: 15.0

result = calculate_area(0, 10)
# Output: Error: One or both dimensions cannot be zero

