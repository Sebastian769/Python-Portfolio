#Seb astian Munoz
#10/23/24


#imp



#Function
def bottles_song():
    milk=99
    for i in range(99):
        if milk>2 :
            print(str(milk) + " bottles of milk on the wall " + str(milk) + " bottles of milk, take one down pass it around")
            milk= milk-1
            print("take one down, pass it around "  + str(milk) + " bottles of milk on the wall")
        elif milk == 2:
            print(str(milk) + " bottles of milk on the wall " + str(milk) + " bottles of milk, take one down pass it around")
            milk= milk-1
            print("take one down, pass it around "  + str(milk) + " bottle of milk on the wall")
        elif milk== 1:
            print(str(milk) +  " bottle of milk on the wall " + str(milk) + " bottle of milk, take one down pass it around")
            milk= milk-1
            print("take one down, pass it around, no more botles of milk on the wall")

#Main
bottles_song()
