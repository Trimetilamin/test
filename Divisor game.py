import os


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




player_round_counter = 1
x = []
divisors_list = []
non_picked_divisor_list = []



cls = lambda: os.system('cls')      #képernyőtörlésekhez majd csak még nem raktam sehova hogy lásd a historyt


def player_namer_function():
    global player_1
    player_1 = input(first_player)
    global player_2
    player_2 = input(second_player)


def number_chooser_function():
    while True:
        try:
            original_number = input(choose_a_number)
            original_number = int(original_number)
            if original_number < 1:
                continue
            else:
                return original_number
        except ValueError:
            continue


def divisor_maker_function(original_number):
    for i in range(1,(original_number+1)):
        if original_number%i == 0:
            divisors_list.append(i)
        else: pass
    print(the_divisors_message)
    print(divisors_list)
    global non_picked_divisor_list
    non_picked_divisor_list = divisors_list
    print(the_non_picked_divisors_message)
    print(non_picked_divisor_list)
    non_picked_divisor_list.append(1)
    return non_picked_divisor_list


def give_a_number_function(player_1: str, player_2: str, non_picked_divisor_list, pick_a_number:str, dont_give_up_message: str, give_a_number_messageage: str):
    player_round_counter = non_picked_divisor_list[-1]
    del non_picked_divisor_list[-1]
    while True:
        if player_round_counter%2 == 1:                                          
            number = input(player_1 + " : " + pick_a_number)
        elif player_round_counter%2 == 0:
            number = input(player_2 + " : " + pick_a_number)
        try:
            number = int(number)
            if (non_picked_divisor_list.count(number) == 0):              
                print(give_a_divisor_number_messagesorNumber)
                print(non_picked_divisor_list)
                continue         
            if (non_picked_divisor_list.count(number) == 1):              
                if number == non_picked_divisor_list[-1]:
                    print(dont_give_up_message)
                    print(non_picked_divisor_list)
                    continue
                else:
                    player_round_counter = player_round_counter + 1
                    non_picked_divisor_list.append(player_round_counter)
                    non_picked_divisor_list.append(number)
                    print(player_round_counter)
                    return non_picked_divisor_list                         
        except ValueError:
            print(give_a_number_messageage)
            continue


def divisor_cutter_function(non_picked_divisor_list):
    number = non_picked_divisor_list[-1]
    del non_picked_divisor_list[-1]
    player_round_counter = non_picked_divisor_list[-1]
    del non_picked_divisor_list[-1]
    non_picked_divisor_help_list = []
    for i in non_picked_divisor_list:
        if i <= number:
            non_picked_divisor_help_list.append(i)
    for i in non_picked_divisor_help_list:
        if number%i==0:
            non_picked_divisor_list.remove(i)
    non_picked_divisor_help_list.clear()
    print(non_picked_divisor_list)
    non_picked_divisor_list.append(player_round_counter)
    return non_picked_divisor_list
   
def the_winner_is_function():
    if player_round_counter%2 == 0:
        print(game_over_messageMessage)
        print(player_1 + winner_messagessage)
    else:
        print(game_over_messageMessage)
        print(player_2 + winner_messagessage)




player_namer_function()
divisor_maker_function(number_chooser_function())

if len(non_picked_divisor_list) > 3:
    while True:
        give_a_number_function(player_1, player_2, non_picked_divisor_list, pick_a_number, dont_give_up_message, give_a_number_messageage)
        divisor_cutter_function(non_picked_divisor_list)
        if len(non_picked_divisor_list) < 3:
            the_winner_is_function()
            break
else:
    the_winner_is_function()











