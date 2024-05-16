#Sets are unordered collections of unique elements in Python. 
#They are often used when you need to work with a collection of 
#items where duplicates are not allowed, 
#or when you need to perform set operations like union and intersection.

# Create a set
foods = {"nasi lemak", "roti canai", "waffle", "nasi ayam"}

# Add an element to the set
foods.add("keropok lekor")

# Remove an element from the set
foods.remove("waffle")

# Check if an element is in the set
contains_spaghetti = "spaghetti" in foods
contains_nasiayam = "nasi ayam" in foods

# Iterate through the set
print("Foods:")
for food in foods:
    print(food)

# Create another set
favourite_foods = {"keropok lekor", "sosej", "mi sup"}

# Perform set operations
union_favourite_foods = foods.union(favourite_foods)
intersection_favourite_foods = foods.intersection(favourite_foods)
difference_favourite_foods = foods.difference(favourite_foods)

# Print the results
print("Contains 'spaghetti'? ", contains_spaghetti)
print("Contains 'nasi ayam'? ", contains_nasiayam)
print("Union of foods and favourite foods:", union_favourite_foods)
print("Intersection of foods and favourite foods:", intersection_favourite_foods)
print("Difference between foods and favourite foods:", difference_favourite_foods)
