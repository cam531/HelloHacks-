score = 0
grammar = 0
spelling = 0
vocab = 0

#user presses "Begin" button
while True:
    s = input("Welcome to the English Quiz! Type the word 'start' to continue!")
    if s != "start":
        print("Please type 'start' to start the quiz")
    else:
        break

q1 = input("Question 1: My teacher (am/is/are) going to the library")
if q1 == "is":
    print("Correct!")
    score += 1
    grammar += 1
else:
    print("Incorrect!")

q2 = input("Question 2: You can find the bus stop over (their/they're/there)")
if q2 == "there":
    print("Correct!")
    score += 1
    grammar += 1
else:
    print("Incorrect!")

q3 = input("Question 3: ")


q4 = input("Question 4: ")


q5 = input("Question 5: ")


q6 = input("Question 6: ")


q7 = input("Question 7: ")


q8 = input("Question 8: ")


q9 = input("Question 9: ")


q10 = input("Question 10: ")

