# Create a list
vegetables = ["potato", "carrot", "broccoli", "cauliflower", "tomato"]

# Append: Add an element to the end
vegetables.append("onion")
print("After append:", vegetables)  # Output: ["potato", "carrot", "broccoli", "cauliflower", "tomato", "onion"]

# Insert: Add an element at a specific position
vegetables.insert(2, "spinach")  # Insert "spinach" at index 2
print("After insert:", vegetables)  # Output: ["potato", "carrot", "spinach", "broccoli", "cauliflower", "tomato", "onion"]

# Remove: Remove the first occurrence of an element
vegetables.remove("broccoli")
print("After remove:", vegetables)  # Output: ["potato", "carrot", "spinach", "cauliflower", "tomato", "onion"]

# Copy (Shallow): Create a new list referencing the same elements
shallow_copy = vegetables.copy()
shallow_copy.append("cucumber")  # Modify the shallow copy
print("Original list:", vegetables)  # Output: ["potato", "carrot", "spinach", "cauliflower", "tomato", "onion"]
print("Shallow copy:", shallow_copy)  # Output: ["potato", "carrot", "spinach", "cauliflower", "tomato", "onion", "cucumber"]

# Count: Find the number of occurrences of an element
count = vegetables.count("carrot")
print("Count of 'carrot':", count)  # Output: Count of 'carrot': 1

# Extend: Add elements from another iterable
salad_vegetables = ["lettuce", "cucumber", "bell pepper"]
vegetables.extend(salad_vegetables)
print("After extend:", vegetables)  # Output: ["potato", "carrot", "spinach", "cauliflower", "tomato", "onion", "lettuce", "cucumber", "bell pepper"]

# Index: Get the index of an element
index = vegetables.index("tomato")
print("Index of 'tomato':", index)  # Output: Index of 'tomato': 4

# Sort: Sort the list (ascending by default)
vegetables.sort()  # Sorts alphabetically
print("After sort:", vegetables)  # Output: ["bell pepper", "carrot", "cauliflower", "cucumber", "lettuce", "onion", "potato", "spinach", "tomato"]

# Reverse: Reverse the order of elements
vegetables.reverse()
print("After reverse:", vegetables)  # Output: ["tomato", "spinach", "potato", "onion", "lettuce", "cucumber", "bell pepper", "cauliflower", "carrot"]

# Clear: Remove all elements from the list
vegetables.clear()
print("After clear:", vegetables)  # Output: After clear: []

# Pop: Remove and return the element at a specific position (or last by default)
last_vegetable = vegetables.pop()  # Since the list is empty, this will raise an IndexError
# To avoid the error, check if the list is not empty before popping
if vegetables:
    last_vegetable = vegetables.pop()
    print("Removed element:", last_vegetable)

# Create a tuple of vegetables
veggie_tuple = ("potato", "carrot", "broccoli", "cauliflower")

# Access elements by index (similar to lists)
first_vegetable = veggie_tuple[0]  # first_vegetable will be "potato"

# Tuples are immutable (cannot be changed after creation)
# veggie_tuple[1] = "tomato"  # This will cause a TypeError

# Loop through elements
for vegetable in veggie_tuple:
    print(vegetable)

# You can create a tuple from a list
veggie_tuple2 = tuple(vegetables)  # veggie_tuple2 will be the same as the original vegetables list

# Create a set of vegetables (duplicates are removed)
veggie_set = {"potato", "carrot", "carrot", "cauliflower", "beans"}  # beans will be added, but the extra "carrot" will be removed

# Sets are unordered, so iterating won't guarantee the order
for vegetable in veggie_set:
    print(vegetable)  # Output order may vary

# Check if an element is in the set
if "tomato" in veggie_set:
    print("tomato is present")
else:
    print("tomato is not present")

# Add elements to a set using the `add` method
veggie_set.add("tomato")
print(veggie_set)  # Now "tomato" is included

# Sets are not directly changeable, but you can create a new set with modifications
updated_veggie_set = veggie_set.union({"onion"})  # Add "onion" using union
print(updated_veggie_set)

# Create a dictionary with vegetables as keys and their colors as values
veggie_colors = {
    "potato": "brown",
    "carrot": "orange",
    "broccoli": "green",
    "cauliflower": "white",
}

# Access values using keys
potato_color = veggie_colors["potato"]  # potato_color will be "brown"

# Add new key-value pair
veggie_colors["tomato"] = "red"

# Update an existing value
veggie_colors["broccoli"] = "dark green"  # Change color

# Check if a key exists
if "onion" in veggie_colors:
    print("onion is a key")
else:
    print("onion is not a key")

# Loop through key-value pairs
for vegetable, color in veggie_colors.items():
    print(f"{vegetable} is {color}")

# Remove a key-value pair using `del`
del veggie_colors["cauliflower"]
print(veggie_colors)

