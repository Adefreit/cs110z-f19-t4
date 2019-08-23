# GOAL:  Get User Inputs Until He/She Types DONE

# Initialize:  This one is a little different than a counting loop.
# Here, we are declaring a variable that keeps track of what the user
# has input.  We will exit the loop once this variable is set to "DONE"
user_value = ''

# Test:  Exit the loop while user_value is "DONE"
while user_value != "DONE":
    # Execute & Modify:  Since the loop exits based on user_value,
    # this line serves as both our execute and modify steps
    user_value = input()

# A simple print statement to let you know when you leave the loop
print("Loop Complete")