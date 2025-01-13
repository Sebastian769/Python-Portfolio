#sebastian 
#10/18/24
#Name generator

#Input

#Functions
def animal_gen():
    print("Welcome to your wild animal")
    print("Answer questions to find out your wild animal")
    ans=input("Jungle(j) or Desert(d)?")
    if ans == "j":
        ans = input("flies(fly) or stays on ground(sog)" )
        if ans == "fly":
            ans= input("colorful(c) or not colorful(nc)")
            if ans == "c":
                print("You are a tucan")
            else:
                print("You are a grey parrot")

        if ans == "sog":
            ans= input("climbs(c) or can't climb(cc)")
            if ans == "c":
                print("You are a monkey")
            else:
                print("You are a capybara")

    if ans == "d":
            ans = input("bird(b) or mammal(m)")
            if ans == "m":
                ans = input("underground(ug) above ground(ag)")
                if ans == "ug":
                    print("You are a ferret")
                else:
                    print("You are coyote")

            if ans == "b":
                ans = input("flies(f) or stays on ground(sog)" )
                if ans == "f":
                    print("You are a Hawk (2 uh)")
                else:
                    print("You are an ostrich")



#Main
animal_gen()
