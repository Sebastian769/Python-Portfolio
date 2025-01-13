#PokemonEvolution
#Sebastian
#Init
pokemon_level=0
pokemon_name="charmander"
day = 1
import random

def charmander():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠉⠀⠀⠀⠀⠀⠈⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⣠⣄⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⡸⢛⣷⡀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⢰⣷⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⢏⡏⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠁⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⣦⡀⠐⠂⠠⠴⠀⠀⠀⠀⠀⠀⠀⣀⡴⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢀⠀⠀⠀
⠀⢰⠦⣄⠈⢿⣶⡶⠤⠤⠤⠔⠒⠒⣶⠒⡫⢋⡄⠀⢸⠀⠀⠀⠀⢀⣀⠤⣤⠀⠀⠀⠀⠀⢀⡞⠉⠛⢆⠀⠀
⢰⡟⢷⠂⠉⠚⠿⣿⣄⣀⣀⣀⣠⣴⣛⣯⠔⠋⠀⠠⠼⠦⠔⠒⠊⠁⠠⡶⢧⡄⠀⠀⠀⠀⠸⣧⠀⡀⠈⣿⠀
⠀⠙⢮⡀⠀⠀⠀⠈⠉⡖⠛⠋⠉⠉⠁⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣥⠞⠁⠀⠀⠀⠀⠀⡏⠿⢧⢀⠈⡆
⠀⠀⠀⠙⢄⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠸⣯⠀⡿
⠀⠀⠀⠀⠀⠓⢄⣠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠐⠒⢖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠉⣶⡇
⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣴⢦⠞⠁
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⢀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠚⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠤⠤⢤⣸⠓⠢⠄⢀⠀⠤⠔⠊⠁⠀⠀⡼⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⢀⡜⠉⠉⠛⢧⠀⠀⠀⠀⠀⠀⣸⠥⣄⣀⣀⣀⠠⠖⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢸⠇⠀⠀⠀⢀⣴⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣷⣦⣀⣀⣀⡀⠤⠤⠤⠚⠁⠀⠀⠀⢸⡤⢤⡤⢤⡴⢤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠾⡷⠞⠿⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")

def charmeleon():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠠⠂⢁⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠊⠁⠀⠀⡀⠙⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢳⠄⠸⣰⣮⡁⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠃⡀⠀⠀⠀⡀⢀⠎⠀⠀⠀⠀⠀⠀⠰⢠⠀⠀⠀
⠀⠀⠀⠀⠀⠐⠢⢥⣬⠄⠀⢸⡀⠀⠀⠀⠀⠀⠀⡞⠻⣰⣄⠀
⠀⠀⠀⢀⠄⠀⠐⠊⡤⠄⡀⠀⠀⠁⠤⢀⡀⠀⠀⣱⠀⠀⣼⡀
⠀⢀⠔⠁⢀⠤⠐⡎⠀⠀⠐⠀⠀⢲⠄⠀⠈⢄⢸⠛⠀⠀⠀⢸
⣰⢅⣔⡶⠁⠀⢸⠀⠀⠀⠀⠃⠀⠀⢂⡇⠀⠘⡄⠑⣄⣤⢠⠁
⠙⠺⠋⠀⠀⠀⣈⠀⠀⠀⠀⢸⡀⠀⠈⣧⡠⢤⡅⠀⡘⢸⠅⠀
⠀⠀⠀⠀⢀⠊⠘⠄⠀⠀⠀⡘⠀⠀⠀⠙⡿⠎⠥⠊⣠⠎⠀⠀
⠀⠀⠀⠀⡧⠀⠀⠈⢂⡄⣀⣃⠀⠀⠀⢀⠧⠄⢐⠨⠊⠀⠀⠀
⠀⠀⠀⢀⡜⠀⠀⢀⡇⠀⠀⠈⣢⠈⣄⠈⡅⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⠮⠓⠂⠁⠀⠀⠀⠀⠷⡎⡢⣗⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
def charizard():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠰⣾⣿⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⣶⣶⣿⠁⠀⠙⠿⣿⣿⣿⡟⠶⠀⠀⠀⠀⠀⢲⣄⠀⠀⠀⠀⠀
⠀⢀⣶⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⢻⣿⣧⠀⠀⠀⠀⠀⢀⣾⣿⣿⣦⡀⠀⠀
⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⢸⣿⣿⡄⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣦⠀
⣿⡟⠉⠀⠀⠈⢻⣿⣿⠿⢿⣿⣿⣷⣾⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⡿⢿⣿⣿⣇
⢻⠁⠀⠀⠀⠀⠀⠉⣠⣶⡟⠛⣿⣿⣿⣿⣿⣿⣿⠟⠛⣿⣿⣿⠋⠀⣾⣟⢻⣿
⠀⠀⠀⠀⠀⠀⠀⠈⠻⠙⢇⣼⣿⣿⣿⣿⣿⣿⣿⡆⠀⠟⠻⠟⠀⠀⣾⣿⠈⡟
⠀⠀⠀⠀⠀⣀⣤⣴⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⢸⣿⡿⠇⠀
⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⢀⣀⡤⠊⠀⠀⠀
⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠛⠻⠿⠿⢿⣿⣿⣿⠛⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠀⠀⠀⠀⠀⠀⠀""")

def train():
    global pokemon_level
    print("You pokemon is now level " + str(pokemon_level+ 1))
    pokemon_level = pokemon_level + 1
def gym_battle():
    global pokemon_level
    print("Welcome to Gym Battle, you will now fight")
    outcome = random.randint(1,2)
    if outcome == 1:
        print("You won!!! You Pokemon is now level " + str(pokemon_level + 2) )
        pokemon_level = pokemon_level + 2
    if outcome == 2:
        print("You lost, better luck next time")
def rest():
    if pokemon_level < 5:
        print(" Charmander is level: " + str(pokemon_level))
        charmander()
    if pokemon_level >= 5 and pokemon_level < 15:
        print(" Charmeleon is level: " + str(pokemon_level))
        charmeleon()
    if pokemon_level > 14:
        print(" Charizard is level: " + str(pokemon_level))
        charizard()




def evolution_2():
    global pokemon_name
    print("Charmander has now evolved into Charmeleon")
    pokemon_name == "charmeleon"
    charmeleon()

def evolution_3():
    global pokemon_name
    print("Charmeleon has now evolved into Charizard")
    pokemon_name == "charizard"
    charizard()


def pokemon_evolution():
    global day
    global pokemon_level
    print("Welcome to pokemon evolution")
    while True:
        print("Choose an activity for day " + str(day))
        print("""1.Train your pokemon(level up by 1)
2.Gym battle(win = +2, loss = 0)
3.Display Pokemon info
4.Exit game""")
        day = day + 1
        activity= int(input("Activity for the day: "))
        if activity == 1:
            train()
        if activity == 2:
            gym_battle()
        if activity == 3:
            rest()
        if activity == 4:
            break
        if pokemon_level == 5:
            evolution_2()
        if pokemon_level == 15:
            evolution_3()



#main
pokemon_evolution()
