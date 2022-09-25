my_dict = {'slay': 'to finish a task with ease and confidence'
,'riz': 'ability to attract a mate' 
,'lit': 'When something is cool or awesome'
,'valid': 'Something that is exciting, cool, or of a high standard'
,'cap': 'Synonym of lie'
,'copium': 'lying to yourself in order to cope with something'
,'based': 'A word used when you agree with something, usually about a controversial or unpopular opinion'}

word = input("Enter a word: ")
for x in my_dict:
    if word == x:
        print(my_dict.get(x))
        break


    