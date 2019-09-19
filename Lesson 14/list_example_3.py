# Creating an empty list to store the names
names = []

# Get a name from the user
name = input()

# Keeps looping until the name is "DONE"
while name != "DONE":
    # Adds the name to a list
    names.append(name)
    
    # Gets the next name from the user
    name = input()
    
# Prints out all of the names
for i in range(len(names)):
    print(names[i])
    
