mentors = {'french': 'Paige, 7783839103, Paigeiscool@gmail.com'
,'tagalog': 'Kristen Tan, 778-900-2718, Sheila543@gmail.com'
,'mandarin': 'Jerry, 604-728-9302, Jerry!!!!!@gmail.com'
,'thai': 'Benny Chinvanich, 778-920-4719, bennyjetts@gmail.com'
,'cantonese': 'Cameron Leong, 778-420-1234, burner@gmail.com'
}

def ell():
    word = input("What is your native language? ")
    counter = 0
    for x in mentors:
        counter += 1
        if word == x:
            
            print("Cool! Here's your new mentor's contact info! \n" + mentors.get(x))
            break
        elif counter == len(mentors):
            print("Sorry! We don't have any " + answer + " speakers available to mentor you.")
            break

answer = input("What language are you trying to learn? ")
if answer == "English" or answer == "english":
    ell()
else:
    counter = 0
    for x in mentors:
        counter += 1
        if answer == x:
            print("Cool! Here's your new mentor's contact info! \n" + mentors.get(x))
            break
        elif counter == len(mentors):
            print("Sorry! We don't have any " + answer + " speakers available to mentor you.")
            break
        
           




