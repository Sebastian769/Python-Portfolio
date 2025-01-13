#Sebastian 
#1/9
#Init
import random
#Functions
def quiz():
    print("Welcome to the multiplication quiz, answer these questions correctly. Good luck")
    grade=0
    for i in range(5):
        num1= random.randint(0,10)
        num2= random.randint(0,10)
        total = num1*num2
        answer=int(input("What is " + str(num1) + " multiplied by "+  str(num2)+ "?"))
        if answer == total:
            print("correct")
            grade= grade+1
        else:
            print("wrong")
    print("Your score is " + str(grade)+"/5")
#Main
quiz()
