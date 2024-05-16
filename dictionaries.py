# Create a dictionary of student information
student = {
    "name": "Joyce",
    "age": int(23),
    "major": "Decision Science",
    "grades": {
        "math": 100,
        "english": 99,
        "history": 90
    }
}

# Access dictionary values by keys
student_name = student["name"]
student_age = student["age"]

# Modify dictionary values
student["age"] = 24
student["grades"]["history"] = 75

# Add a new key-value pair
student["gender"] = "Female"

# Check if a key exists in the dictionary
has_major = "major" in student
has_gender = "gender" in student

# Get the list of keys and values
keys = student.keys()
values = student.values()

# Iterate through the dictionary
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Remove a key-value pair
del student["grades"]

# Print the updated dictionary
print("\nStudent Information after removing 'grades':")
for key, value in student.items():
    print(f"{key}: {value}")
    
print("Contains 'major'? ", has_major)
print("Contains 'gender'? ", has_gender)
