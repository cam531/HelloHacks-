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

q3 = input("Question 3: Convert this sentence into past tense: “I am going to read a book at school today.")
if q3 == "I read a book at school today.":
    print("Correct!")
    score += 1
    grammar += 1
else:
    print("Incorrect!")

q4 = input("Question 4: I want to (where/wear/ware) this new outfit tomorrow")
if q4 == "wear":
    print("Correct!")
    score += 1
    spelling += 1
else:
    print("Incorrect!")

q5 = input("Question 5: Hannah and Harold (jumped/ arrived/ flew) at the bus station early.")
if q5 == "arrived":
    print("Correct!")
    score += 1
    vocab += 1
else:
    print("Incorrect!")

q6 = input("Question 6: That student (wrote/ ate/ slept) the best essay in the class last month.")
if q6 == "wrote":
    print("Correct!")
    score += 1
    vocab += 1
else:
    print("Incorrect!")

q7 = input("Question 7: My favourite animal is a (table, dog, chips)")
if q7 == "dog":
    print("Correct!")
    score += 1
    vocab += 1
else:
    print("Incorrect!")

q8 = input("Question 8: If only you believe you can (achieve/ acheive/ acheeve)!")
if q8 == "achieve":
    print("Correct!")
    score += 1
    spelling += 1
else:
    print("Incorrect!")

q9 = input("Question 9: I like to eat (dessert/ desert/ desertt)")
if q9 == "dessert":
    print("Correct!")
    score += 1
    spelling += 1
else:
    print("Incorrect!")

print("Congrats on finishing your quiz! Your score is " + str(score) + "/9!")

scores = [vocab, spelling, grammar]
scores.sort()

if scores[0] == scores[1] and scores[1] == scores[2]:
    print("You should practice all three topics!")
elif vocab == scores[0]:
    print("You should practice your vocabulary choice!")
elif spelling == scores[0]:
    print("You should practice your spelling!")
else:
    print("You should practice your grammar!")



