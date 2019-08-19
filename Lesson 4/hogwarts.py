# Storing Points
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# QUESTION #1
q1_answer = input("How would you describe yourself?\n a) brave,\n b) studious,\n c) loyal,\n d) ambitious?\n")

if q1_answer == 'a':
    gryffindor = gryffindor + 1
elif q1_answer == "b":
    ravenclaw = ravenclaw + 1
elif q1_answer == "c":
    hufflepuff = hufflepuff + 1
elif q1_answer == "d":
    slytherin = slytherin + 1
  
# QUESTION #2
q2_answer = input("What can you be found doing on the weekends?\n a) Going on adventures\n b) Doing my homework\n c) Spending time with family or friends\n d) Plotting revenge on my enemies\n")

if q2_answer == 'a':
    gryffindor = gryffindor + 1
elif q2_answer == "b":
    ravenclaw = ravenclaw + 1
elif q2_answer == "c":
    hufflepuff = hufflepuff + 1
elif q2_answer == "d":
    slytherin = slytherin + 1

# QUESTION #3
q3_answer = input("What would you do if the Dark Lord was going to invade your school?\n a) Fight him\n b) Look up some good defensive curses in a book\n c) Stand by my friends no matter what\n d) Help the Dark Lord invade the school as an inside spy\n")

if q3_answer == 'a':
    gryffindor = gryffindor + 1
elif q3_answer == "b":
    ravenclaw = ravenclaw + 1
elif q3_answer == "c":
    hufflepuff = hufflepuff + 1
elif q3_answer == "d":
    slytherin = slytherin + 1

# Determines what house you are in
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("GRYFFINDOR!!!!!!!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("RAVENCLAW!!!!!!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("HUFFLEPUFF!!!!!!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("SLYTHERIN!!!!!!")
else:
    print("Too difficult to decide . . . ")
