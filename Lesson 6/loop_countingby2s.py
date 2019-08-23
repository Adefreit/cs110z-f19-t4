# Goal:  Counting from 0 to a user defined number by 2's

# Initialize the Loop Control Variable
i = 0
user_value = int(input())

# Test:  The loop needs to run until i >= user_value
while i < user_value:
    
    # Execute:  All we are doing for this step is printing i
    print(i)
    
    # Modify:  We are adding 2 to our loop control variable since
    # we are counting by 2's.
    i = i + 2
    
# A simple print statement to let you know when you leave the loop
print("Loop Complete")