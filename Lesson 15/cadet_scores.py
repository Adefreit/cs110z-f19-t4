# Make my lists
names = []
scores = []
total = 0

name = input()

while name != 'LAST':
    # Adds the name to the list
    names.append(name)
    
    # Gets the Score and add it to the list
    score = int(input())
    scores.append(score)
    
    total = total + score

    # Gets the next name
    name = input()

# Calculates the Average
average = total / len(names)

# Looking at each score to see if it is bigger than the average
for i in range(len(scores)):
    if scores[i] > average:
        print(names[i])