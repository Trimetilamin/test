import os


FirstPlayer = "Az első játékos neve:"
SecondPlayer ="A második játékos neve:"
ChooseANumber = "1-nél nagyobb, egész számot adjon meg!"
PickANumber = "Válassz egy számot!"
LooserMessage = "Vesztettél!"
DontGiveUpMessage = "Még van lehetőség mást választani!"
GiveANumber = "Kérem számot adjon meg!"
GiveADivisorNumber = "Ez a szám nincs az osztók között!"
GameOverMessage = "Vége a játéknak"
WinnerMessage = " nyert!"




playerRound = 1
x = []
divisors = []
nonPickedDivisors = []
PickedDivisors = []


cls = lambda: os.system('cls')      #képernyőtörlésekhez majd csak még nem raktam sehova hogy lásd a historyt


def playerNamer():
    global Player_1
    Player_1 = input(FirstPlayer)
    global Player_2
    Player_2 = input(SecondPlayer)


def numberchooser():
    while True:
        try:
            origNumber = input(ChooseANumber)
            origNumber = int(origNumber)
            if origNumber < 1:
                continue
            else:
                return origNumber
        except ValueError:
            continue


def divisorMaker(origNumber):
    for i in range(1,(origNumber+1)):
        if origNumber%i == 0:
            divisors.append(i)
        else: pass
    print("Ezek az osztók:")
    print(divisors)
    global nonPickedDivisors
    nonPickedDivisors = divisors
    print("Ezek a még nem kiejtett osztók:")
    print(nonPickedDivisors)
    nonPickedDivisors.append(1)                 #1. playerround jön
    return nonPickedDivisors


def giveANumber(Player_1: str, Player_2: str, nonPickedDivisors, PickANumber:str, DontGiveUpMessage: str, GiveANumber: str):
    playerRound = nonPickedDivisors[-1]
    del nonPickedDivisors[-1]
    while True:
        if playerRound%2 == 1:                                          
            numb = input(Player_1 + " : " + PickANumber)
        elif playerRound%2 == 0:
            numb = input(Player_2 + " : " + PickANumber)




        try:
            numb = int(numb)
            if (nonPickedDivisors.count(numb) == 0):              
                print(GiveADivisorNumber)
                print(nonPickedDivisors)
                continue
                           
            if (nonPickedDivisors.count(numb) == 1):              
                if numb == nonPickedDivisors[-1]:
                    print(DontGiveUpMessage)
                    print(nonPickedDivisors)
                    continue
                else:
                    playerRound = playerRound + 1
                    nonPickedDivisors.append(playerRound)
                    nonPickedDivisors.append(numb)
                    print(playerRound)
                    return nonPickedDivisors
                               
        except ValueError:
            print(GiveANumber)
            continue


def divisorCutter(nonPickedDivisors):
    numb = nonPickedDivisors[-1]
    del nonPickedDivisors[-1]
    playerRound = nonPickedDivisors[-1]
    del nonPickedDivisors[-1]
    nonPickedDivisorsHelp = []
    for i in nonPickedDivisors:
        if i <= numb:
            nonPickedDivisorsHelp.append(i)
    for i in nonPickedDivisorsHelp:
        if numb%i==0:
            nonPickedDivisors.remove(i)
    nonPickedDivisorsHelp.clear()
    print(nonPickedDivisors)
    nonPickedDivisors.append(playerRound)
    return nonPickedDivisors
   
def theWinneris():
    if playerRound%2 == 1:
        print(GameOverMessage)
        print(Player_1 + WinnerMessage)
    else:
        print(GameOverMessage)
        print(Player_2 + WinnerMessage)




playerNamer()
divisorMaker(numberchooser())

if len(nonPickedDivisors) > 3:
    while True:
        giveANumber(Player_1, Player_2, nonPickedDivisors, PickANumber, DontGiveUpMessage, GiveANumber)
        divisorCutter(nonPickedDivisors)
        if len(nonPickedDivisors) < 3:
            theWinneris()
            break
else:
    theWinneris()












