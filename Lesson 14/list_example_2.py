# Gets # of swimmers from user
num_swimmers = int(input())

# Keeps Track of the Total
total = 0

# List to Hold Swim Times
times = []

# Loop to get all swim times
for i in range(num_swimmers):
    
    # Get Each Individual Time
    swim_time = int(input())
    
    # Puts Time in List
    times.append(swim_time)
    
    # Updates the Total
    total = total + swim_time

# Calculates the Average
average = total / num_swimmers

# Keeps Track of Num Below Avg
total_below_avg = 0

# Loop to Compare Every time to the Avg
for i in range(num_swimmers):
    if times[i] > average:
        total_below_avg = total_below_avg + 1

# Print the Final Results
print(average)
print(total_below_avg)


    
    
