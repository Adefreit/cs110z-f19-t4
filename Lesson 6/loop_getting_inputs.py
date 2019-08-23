# GOAL:  Get X inputs from the user

# Initialize the Loop Control Variable
i = 0
user_value = int(input())

# Test:  the loop needs to run user_value times
while i < user_value:
    
    # Execute:  All we are doing is printing the number
    print(i)
    
    # Modify:  We are incrementing the loop counter
    i = i + 1

# A simple print statement to let you know when you leave the loop
print("Loop Complete")