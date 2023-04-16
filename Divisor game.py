import os

class Messages:
    first_player = "Az első játékos neve:"
    second_player ="A második játékos neve:"
    the_divisors_message = "Ezek az osztók:"
    the_non_picked_divisors_message = "Ezek a még nem kiejtett osztók:"
    choose_a_number = "1-nél nagyobb, egész számot adjon meg!"
    pick_a_number = "Válassz egy számot!"
    looser_message = "Vesztettél!"
    dont_give_up_message = "Még van lehetőség mást választani!"
    give_a_number_messageage = "Kérem számot adjon meg!"
    give_a_divisor_number_messagesorNumber = "Ez a szám nincs az osztók között!"
    game_over_messageMessage = "Vége a játéknak"
    winner_messagessage = " nyert!"

class Props:
    original_number = int
    player_round_counter = 0
    x = []
    divisors_list = []
    non_picked_divisor_list = []

class Players:

    player_1 = input(Messages.first_player)
    player_2 = input(Messages.second_player)
    pass

#cls = lambda: os.system('cls')


def player_namer_function():
    Players


def number_chooser_function():
    while True:
        try:
            ask_number = input(Messages.choose_a_number)
            original_number = int(ask_number)
            if original_number < 1:
                continue
            else:
                original_number = Props.original_number
        except ValueError:
            continue


def divisor_maker_function():
    for potential_divisors in range(1,(Props.original_number+1)):
        if Props.original_number%potential_divisors == 0:
            Props.divisors_list.append(potential_divisors)
        else:
            pass
    print(Messages.the_divisors_message)
    print(Props.divisors_list)
    Props.non_picked_divisor_list = Props.divisors_list
    print(Messages.the_non_picked_divisors_message)
    print(Props.non_picked_divisor_list)


def give_a_number_function():
    Props.player_round_counter = Props.player_round_counter + 1
    while True:
        if Props.player_round_counter%2 == 1:                                          
            number = input(Players.player_1 + " : " + Messages.pick_a_number)
        elif Props.player_round_counter%2 == 0:
            number = input(Players.player_2 + " : " + Messages.pick_a_number)
        try:
            number = int(number)
            if (Props.non_picked_divisor_list.count(number) == 0):              
                print(Messages.give_a_divisor_number_messagesorNumber)
                print(Props.non_picked_divisor_list)
                continue         
            if (Props.non_picked_divisor_list.count(number) == 1):              
                if number == Props.non_picked_divisor_list[-1]:
                    print(Messages.dont_give_up_message)
                    print(Props.non_picked_divisor_list)
                    continue
                else:
                    Props.player_round_counter = Props.player_round_counter + 1
                    print(Props.player_round_counter)
                    return Props.non_picked_divisor_list                         
        except ValueError:
            print(Messages.give_a_number_messageage)
            continue

player_namer_function()
divisor_maker_function(number_chooser_function())
