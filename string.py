# Define a string variable
message = "Hello Guys, I am your friend"

# Print the string
print(message)

# Access individual characters in the string
first_character = message[0]
print("The first character is:", first_character)

# Find the length of the string
length = len(message)
print("The length of the string is:", length)



#
# Get user input for the name
name = input("Please enter your name: ")
#
#



# Concatenate (combine) two strings
greeting = "Hello, " + name + "!"+ " Nice to meet you!"
print(greeting)

# Use string methods
uppercase_message = greeting.upper()
print("Uppercase message:", uppercase_message)

# Check if a substring is in the string
contains_Burn = "Burn" in greeting
print("Does the message contain 'Burn'? ", contains_Burn)

# Replace part of the string
new_message = message.replace("Burn", "Hi")
print("Updated message:", new_message)
