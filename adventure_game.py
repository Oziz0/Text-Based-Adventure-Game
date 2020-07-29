import random
import time
# List of items and the use of random in items
# a list of items to pick randomly
Item = items = ['lockpick kit', 'gun', 'keycard', 'granade', 'shady bottle']
randChoice = random.choice(items)
# A function delaying the text


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)
# Start of the game


def start():
    print_pause('You woke up in a white room,')
    print_pause('''You see a large thick glass window and a table.''')
    print_pause('1-look at table.\n 2-look at glass window.')
    option1 = input("Enter 1 or 2: ")
    Check = True
    while Check:
        if '1' == option1:
            Check = False
            choice1()
        elif '2' == option1:
            Check = False
            choice2()
        else:
            print('invalid input, Try again')
            option1 = input("Enter 1 or 2: ")
# Printing for choice1
# This is the route for choice1


def choice1():
    print_pause('You saw a note at the table written on it ')
    print_pause('''"you have one hour before i discharge a deadly chemical,
    find your way out of this small room before i do so."''')
    story()


# The completion of the story and the use of the random items and the results


def story():
    print_pause('''You looked around and there's a
    door with a card slot with a tiny screen that said 'INSERT',''')
    print_pause('You looked further into the room,')
    print_pause('And you see a hidden lever ')
    print_pause('You try to pull the level')
    print_pause('You pull it then a hatch opened from the ceiling')
    print_pause('And a '+randChoice+' dropped from the hatch')
    if 'keycard' in randChoice:
        print_pause('''you've tried to open the door with the keycard and''')
        print_pause('You Won')
        Restart()
    if 'gun' in randChoice:
        print_pause('You shoot the glass window and escaped')
        print_pause('You Won')
        Restart()
    if 'granade' in randChoice:
        print_pause('''You tried to throw at the door to blow it but it
        hits door and came back at you and
        \n You died from the explosion ''')
        Restart()
    if 'lockpick kit' in randChoice:
        print_pause('''You tried to open the door with a lockpick kit then,
        you escaped the room''')
        print_pause('You Won')
        Restart()
    if 'shady bottle' in randChoice:
        print_pause('You Drinked the shady bottle')
        print_pause('You Died')
        Restart()
# Printing for choice1
# This is the route for choice1


def choice2():
    print_pause('''You looked at the window and you
    saw a man behind the glass and he said''')
    print_pause('''"you have one hour before i discharge a deadly chemical,
    find your way out of this small room before i do so."''')
    story()
# A function for restarting the game


def Restart():
    replay = input('Want to play again \n [Yes] [No] ').lower()
    CheckReplay = True
    while CheckReplay:
        if 'yes' == replay:
            print_pause('Enjoy...')
            start()
        elif 'no' == replay:
            print_pause('Good bye...')
            CheckReplay = False
        else:
            print('invalid input, Try again')
            replay = input('Want to play again \n [Yes] [No] ').lower()

# Function call


start()
