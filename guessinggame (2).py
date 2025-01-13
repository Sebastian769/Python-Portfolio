#Sebastian 
#11/12/24
#init
import random
secret=random.randint(1,10)#integer
secret2=random.randint(1,25)
#function
def guessing_game():
    print("Welcome to the guessing game, pick a number 1-10 and test your luck")
    guess=int(input("Enter Guess"))#integer
    if guess == secret:
        print("Congrats you won!!!")
        play_again= input("Play again?(yes or no)")
        if play_again == "yes":
            guessing_game()
        if play_again== "no":
            print("Someone is lameeee")


    else:
        if guess > secret:
             print("too high, try again")
             guess=int(input("Enter Guess"))#integer
             if guess == secret:
                play_again= input("Play again?(yes or no)")
                if play_again == "yes":
                    guessing_game()
                if play_again== "no":
                    print("oh well :( )")

             else:
                print("You lost, the secret number was " + str(secret))
                play_again= input("Play again?(yes or no)")
                if play_again == "yes":
                    guessing_game()
                if play_again== "no":
                    print("giving up so easily?")


        if guess < secret:
            print("too low, try again")
            guess=int(input("Enter Guess"))#integer
            if guess == secret:
                play_again= input("Play again?(yes or no)")
                if play_again == "yes":
                    guessing_game()
                if play_again== "no":
                    print("oh well :( )")
            else:
                print("You lost the secret number was " + str(secret))
                play_again= input("Play again?(yes or no)")
                if play_again == "yes":
                    guessing_game()
                if play_again== "no":
                    print("giving up so easily?")

        if guess == secret:
            print("Congrats you won")
            play_again= input("Play again?(yes or no)")
            if play_again == "yes":
                guessing_game()
            if play_again== "no":
                print("oh well :( ")









#Main
guessing_game()

