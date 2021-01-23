import pandas as pd
import random

# read excel file
readFile = pd.read_excel(
    r'/mnt/c/Users/girlj/Dropbox/My PC (DESKTOP-P7PHLGB)/Documents/Java Projects/Random_Question_Generator/100_Getting_to_know_you_Questions.xlsx')
# print(readFile.head())

# store the data into the list
questions = readFile['100 Questions'].tolist()
questionNum = readFile['#'].tolist()

# welcome message
print("Enter your name: ", end='')
name = input()
print("Hello,", name, " <Enter>", end='')
input()
print()
print("We have", len(questions), "questions to get to know you")
print("Please enter to get a question: <ENTER> ", end='')
input()

QnA = {}
exitOrNot = "" 
# LOOP GENERATING QUESTIONS:
while exitOrNot != "0" and len(questions) > 0:
    # Generate random number for the question.
    # and remove the number and its question from the lists
    randomNum = random.randint(0, len(questions)-1)
    # print(randomNum)
    questionNum.remove(randomNum)
    questions.remove(questions[randomNum])

    # Show the random questions:
    print()
    print("<<", questions[randomNum], ">>")
    print()
    print("Please type your answer: ", end="")
    answer = input()
    print()

    # store the answers per the question
    QnA[questions[randomNum]] = answer
    # print(QnA)

    print("     <Enter> if you want more questions, otherwise '0' to exit: ", end='')
    exitOrNot = input()
    if exitOrNot=="0":
        print()
        i = 1
        for x in QnA:
            print(i,")", x, ":", QnA[x])
            i+=1
        print()
        print("Thank yourself for having time to get to know yourself! Bye!")
        break

    


# FOR TESTING: showing the left questions
#print("The left number of questions are:",len(questions))
# i = 0
# for x in range(len(questions)):
#     print(questionNum[i], questions[i])
#     i+=1
