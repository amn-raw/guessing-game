import getpass
import pyautogui as pt
import time
import random
import colorama as clm
 # selecting player as computer or friend


try:
    player_type = input('If you want to play with computer please press C Else if you want to play with Player press P')
except Exception as error:
    print('error', error)
while (player_type == "" or (player_type != 'c' and player_type!='C' and player_type!='p' and player_type!='P' ) ):
    print('Please Enter C/P and then press enter')
    try:
        player_type = input('If you want to play with computer please press C Else if you want to play with Player press P')
    except Exception as error:
        print('error', error)

# Play with Computer
if (player_type == "C" or player_type == "c"):
    try:
        rg_min_str = input('give minimum value of the range in which you want to play the game and then press enter ')
        if (rg_min_str != ''):
            rg_min = int(rg_min_str)
        else:
            rg_min = 0
    except Exception as error:
        print('error', error)
    while (rg_min < 0 or rg_min_str == "" ):
        try:
            rg_min_str = input(
                'give minimum value of the range in which you want to play the game and then press enter ')
            if (rg_min_str != ''):
                rg_min = int(rg_min_str)
            else:
                rg_min = 0
        except Exception as error:
            print('error please Enter a valid number')

    try:
        rg_max_str = input('give maximum value of the range in which you want to play the game and then  press enter ')
        if (rg_max_str != ''):
            rg_max = int(rg_max_str)
        else:
            rg_max = 0
    except Exception as error:
        print('error', error)
    while (rg_max < 0 or rg_max_str == ""):

        try:
            rg_max_str = input(
                'give maximum value of the range in which you want to play the game and then  press enter ')
            if (rg_max_str != ''):
                rg_max = int(rg_max_str)
            else:
                rg_max = 0
        except Exception as error:
            print('please enter a valid number')

    time.sleep(1)

    s1 = ["  ______  _______    _        ________     _______",
          " /      \    |      / \        |       \      |",
          "|            |     /   \       |       |      |",
          " \_____      |    /     \      |______/       |",
          "       \     |   /   -   \     |    \         |",
          "        |    |  /         \    |     \        |",
          " \_____/     | /           \   |      \       |"
          ]
    for i in range(7):
        count = 0
        for ch in s1[i]:
            p = abs(6 - abs(12 - (abs(25 - (abs(50 - count))))))
            time.sleep(0.005)
         #   print(ch, end="")
            print("\033[92m"+ ch +"\033[0m",end="")
            count += 1
        time.sleep(0.1)
        print("")
    time.sleep(1.2)
    flag = 1
    flag1 = 1
    flag2 = 1
    win_1 = 0
    win_2 = 0
    round_num = 1
    while (flag == 1):
        print("Let's start round " + str(round_num) +"with Computer")
        print('First computer will set the number for you to guess')
        p = rg_min
        q = rg_max
        try:
            number = random.randint(p,q);
        except Exception as error:
            print('error', error)
        # time.sleep(4)
        # second person guesses
        print('Player 2 may now start guessing the number')
        guess_no = 1
        try:
            guess_str = input('Enter guess ' + str(guess_no) + ' ')
            guess = int(guess_str)
        except Exception as error:
            print('error', error)

        while (guess != number):
            if (guess_str == ""):
                print("You haven't Entered a valid guess! Please Enter a guess again!!!")
            elif (guess == -1 and guess_no == 1):
                flag = 0
                break
            elif (guess == -1):
                flag1 = 0
                break
            elif (guess < rg_min or guess > rg_max):
                print('please enter number in valid range [' + str(rg_min)+ ','+str(rg_max)+ '] you have lost your one guess')
            elif (guess > number):
                print('Your guess is greater Please try again')
            elif (guess < number):
                print('Your guess is smaller Please try again')
            if (guess_str != ""):
                guess_no += 1
            try:
                guess_str = input('Enter guess ' + str(guess_no) + ' ')
                guess = int(guess_str)
            except Exception as error:
                print('error', error)

        print('You guessed the number correctly in ' + str(guess_no) + ' guesses.')
        a = guess_no

        if (flag == 0):
            break

        if (flag1 == 0):
            print( "\033[92m"+ " You quit the game so Winner of this round is Player 2" +"\033[0m")
            win_2 += 1
            break

        print('Please set a number for  Computer to guess ')
        try:
            number = int(pt.password('Player 2 please enter a number between ' + str(rg_min) + "and " + str(rg_max)))
        except Exception as error:
            print('error', error)
        while (number > rg_max or number < rg_min or number == ''):
            print('Please Enter the number in between ' + str(rg_min) + 'and' + str(rg_max))
            try:
                number = int(
                    pt.password('Player 1 please enter a number between ' + str(rg_min) + "and " + str(rg_max)))
            except Exception as error:
                print('error', error)
        # time.sleep(4)
        # second person guesses
        print('Computer may now start guessing the number')
        guess_no = 1
        try:
            guess = random.randint(p,q)
        except Exception as error:
            print('error', error)

        while (guess != number):
            time.sleep(1);
            print("\033[92m"+"Guess : "+str(guess) + "\033[0m")
            time.sleep(1)
            if(guess > number):
                print( "Cmputer's guess is greater Please try again" )
                q=guess-1
            elif(guess < number):
                print("Computer's guess is smaller Please try again")
                p=guess+1
            guess_no += 1
            try:
                guess = random.randint(p, q)
            except Exception as error:
                print('error', error)
        print("\033[92m"+"Guess : " + str(guess)+"\033[0m")
        print('\033[92m'+ 'Computer guessed the number correctly in ' + str(guess_no) + ' guesses.' + '\033[0m')
        b = guess_no
        if (a > b):
            print('winner of round ' + str(round_num) + ' is Computer')
            win_2 += 1
        elif (b > a):
            print('winner of round ' + str(round_num) + ' is you ')
            win_1 += 1
        else:
            print('This match Draws')
        round_num += 1
        try:
            next_match = input('If you want to play one more game please press Y + enter otherwise press N + Enter')
        except Exception as error:
            print('error', error)
        while (next_match == ""):
            print('Please Enter Y/N and then press enter')
            try:
                next_match = input('If you want to play one more game please press Y + enter otherwise press N + Enter')
            except Exception as error:
                print('error', error)
        if (next_match == "N" or next_match == "n"):
            flag = 0
        elif (next_match == "Y" or next_match == "y"):
            continue

    if (win_1 > win_2):
        print('Player 1 is Overall winner')
    elif (win_2 > win_1):
        print('Player 2 is Overall winner')
    else:
        print('DRAW')
    exit()



# Play with friend:
elif (player_type == "p" or player_type == "P"):
    try:
        rg_min_str = input('give minimum value of the range in which you want to play the game and then press enter ')
        if (rg_min_str != ''):
            rg_min = int(rg_min_str)
        else:
            rg_min = 0
    except Exception as error:
        print('error', error)
    while (rg_min < 0 or rg_min_str==""):
        try:
            rg_min_str = input(
                'give minimum value of the range in which you want to play the game and then press enter ')
            if (rg_min_str != ''):
                rg_min = int(rg_min_str)
            else:
                rg_min = 0
        except Exception as error:
            print('error please Enter a valid number')

    try:
        rg_max_str = input('give maximum value of the range in which you want to play the game and then  press enter ')
        if (rg_max_str != ''):
            rg_max = int(rg_max_str)
        else:
            rg_max = 0
    except Exception as error:
        print('error', error)
    while (rg_max < 0 or rg_max_str == ""):

        try:
            rg_max_str = input(
                'give maximum value of the range in which you want to play the game and then  press enter ')
            if (rg_max_str != ''):
                rg_max = int(rg_max_str)
            else:
                rg_max = 0
        except Exception as error:
            print('please enter a valid number')

    time.sleep(1)

    s1 = ["  ______  _______    _        ________     _______",
          " /      \    |      / \        |       \      |",
          "|            |     /   \       |       |      |",
          " \_____      |    /     \      |______/       |",
          "       \     |   /   -   \     |    \         |",
          "        |    |  /         \    |     \        |",
          " \_____/     | /           \   |      \       |"
          ]
    for i in range(7):
        count = 0
        for ch in s1[i]:
            p = abs(6 - abs(12 - (abs(25 - (abs(50 - count))))))
            time.sleep(0.01)
            print(ch, end="")
            count += 1
        # time.sleep(0.2)
        print("")
    time.sleep(1.5)
    flag = 1
    flag1 = 1
    flag2 = 1
    win_1 = 0
    win_2 = 0
    round_num = 1
    while (flag == 1):
        print("Let's start round " + str(round_num))
        print('Player 1 please Enter a number')
        try:
            number = int(pt.password('Player 1 please enter a number between ' + str(rg_min) + "and " + str(rg_max)))
        except Exception as error:
            print('error', error)

        while (number > rg_max or number < rg_min or number == ''):
            print('Please Enter the number in between ' + str(rg_min) + 'and' + str(rg_max))
            try:
                number = int(
                    pt.password('Player 1 please enter a number between ' + str(rg_min) + "and " + str(rg_max)))
            except Exception as error:
                print('error', error)
        # time.sleep(4)
        # second person guesses
        print('You may now start guessing the number')
        guess_no = 1
        try:
            guess_str = input('Enter guess ' + str(guess_no) + ' ')
            guess = int(guess_str)
        except Exception as error:
            print('Please Enter Valid Guess', error)

        while (guess != number):
            if (guess_str == ""):
                print("You haven't Entered a valid guess! Please Enter a guess again!!!")
            elif (guess == -1 and guess_no == 1):
                flag = 0
                break
            elif (guess == -1):
                flag1 = 0
                break
            elif (guess < rg_min or guess > rg_max):
                print('please enter number in valid range [' + str(rg_min)+ ','+str(rg_max)+ ']  you have lost your one guess')
            elif (guess > number):
                print('Your guess is greater Please try again')
            elif (guess < number):
                print('Your guess is smaller Please try again')
            if (guess_str != ""):
                guess_no += 1
            try:
                guess_str = input('Enter guess ' + str(guess_no) + ' ')
                guess = int(guess_str)
            except Exception as error:
                print('error', error)

        print('You guessed the number correctly in ' + str(guess_no) + ' guesses.')
        a = guess_no

        if (flag == 0):
            break

        if (flag1 == 0):
            print(' You quit the game so Winner of this round is Player 2')
            win_2 += 1
            break

        print('Player 2 please Enter your number')
        try:
            number = int(pt.password('Player 2 please enter a number between ' + str(rg_min) + "and " + str(rg_max)))
        except Exception as error:
            print('error', error)
        while (number > rg_max or number < rg_min or number == ''):
            print('Please Enter the number in between ' + str(rg_min) + 'and' + str(rg_max))
            try:
                number = int(
                    pt.password('Player 1 please enter a number between ' + str(rg_min) + "and " + str(rg_max)))
            except Exception as error:
                print('error', error)
        # time.sleep(4)
        # second person guesses
        print('player1 may now start guessing the number')
        guess_no = 1
        try:
            guess_str = input('Enter guess : ' + str(guess_no))
            guess = int(guess_str)
        except Exception as error:
            print('error', error)

        while (guess != number):
            if (guess_str == ""):
                print("You haven't Entered a valid guess! Please Enter a guess again!!!")
            elif (guess == -1):
                flag2 = 0
                break
            elif (guess < rg_min or guess > rg_max):
                print('please enter number in valid range  [' + str(rg_min)+ ','+str(rg_max)+ '] you have lost your one guess')
            elif (guess > number):
                print('Your guess is greater Please try again')
            elif (guess < number):
                print('Your guess is smaller Please try again')
            if (guess_str != ""):
                guess_no += 1
            try:
                guess_str = input('Enter guess : ' + str(guess_no))
                guess = int(guess_str)
            except Exception as error:
                print('error', error)

        if (flag2 == 0):
            print('You quit the game So Winner of this round is Player 1')
            win_1 += 1
            break

        print('You guessed the number correctly in ' + str(guess_no) + ' guesses.')
        b = guess_no
        if (a > b):
            print('winner of round ' + str(round_num) + ' is Player 1')
            win_2 += 1
        elif (b > a):
            print('winner of round ' + str(round_num) + ' is Player 2')
            win_1 += 1
        else:
            print('This match Draw')
        round_num += 1
        try:
            next_match = input('If you want to play one more game please press Y + enter otherwise press N + Enter')
        except Exception as error:
            print('error', error)
        while (next_match == ""):
            print('Please Enter Y/N and then press enter')
            try:
                next_match = input('If you want to play one more game please press Y + enter otherwise press N + Enter')
            except Exception as error:
                print('error', error)
        if (next_match == "N" or next_match == "n"):
            flag = 0
        elif (next_match == "Y" or next_match == "y"):
            continue

    if (win_1 > win_2):
        print('Player 1 is Overall winner')
    elif (win_2 > win_1):
        print('Player 2 is Overall winner')
    else:
        print('DRAW')
    exit()





