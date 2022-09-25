spelling = 2
vocab = 3
grammar = 1

#categoryscore = {}
#categoryscore['spelling'] = spelling


scores = [vocab, spelling, grammar]
for x in scores:
    print(x)

scores.sort()
for x in scores:
    print(x)

if scores[0] == scores[1] and scores[1] == scores[2]:
    print("You should practice all three topics!")
elif vocab == scores[0]:
    print("You should practice your vocabulary choice!")
elif spelling == scores[0]:
    print("You should practice your spelling!")
else:
    print("You should practice your grammar!")