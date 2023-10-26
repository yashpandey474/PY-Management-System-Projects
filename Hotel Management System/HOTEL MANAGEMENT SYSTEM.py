#MODULES
import pdb
import databasehotel
import answerlists
import math
import random
import string
import json
import pickle
import os
import sys
backpack = pickle.load( open("save18.p", "rb"))
executives = pickle.load( open("save20.p", "rb"))
users = pickle.load( open("save15.p", "rb"))
from databasehotel import y1
from databasehotel import n
status = ''


#INITIALISATION


print("                     HOTEL BOOKING SYSTEM(HBSBY)                ", end = '\n \n \n \n \n \n')
print("MADE BY:   YASH PANDEY", end = '\n')
print("FROM: APJ SCHOOL SS", end = '\n \n \n \n')

print("================================================================================")


print("Welcome to HMSBY!")
print("We are a multipurpose platform that allows different types of users.",
      "For a customer, we provide a list of hotels in the area they want,",
      "and we show them he respective costs based on their period of journey.",
      "They can then choose the hotel of their choice and we instantle make changes in rooms, accordingly.",
      "For a hotel manager, they can register their hotel and specify multiple feature for users to consider.",
      "they have seperate access through executive logins and can edit hotels with their ids only shown to the owner.",
      "While editing, they can change rooms availaible, prices per room and even the name, but have the same id forever.",
      sep = '\n')

print("\n \n \nLet\'s move on to the main part of our application, now")
print("\nWe will need you to login or signup before going into the booking process: ")




#FUNCTIONS

def start():

    userdetails()

    st = str(input("Do you want to start with hotel booking process?"))


    if st in y1:

        pass
    elif st in n:

        print("Oh. Well, this is a hotel booking system, so farewell!")
        quit()
    else:
        while st not in y1 and st not in n:

            print("Invalid input")

            st = str(input("Do you want to start with hotel booking process?: "))

            if st in y1:

                start()
            elif st in n:

                print('Well, we call that non-, invalid input')
                quit()

            else:

                while st not in y1 and st not in n:


                    print("Invalid input")
                    st = str(input("Do you want to start with hotel booking process?: "))
    ar = str(input("Enter the area to find hotels in: "))
    room = int(input("Enter no of rooms required: "))
    time = int(input("Enter no of days to stay: "))
    ctrl = 0
    x = 1
    for f in backpack:
        m = backpack[f]
        for i in m:
            if ctrl == 0:
                if i != ar:
                    break
                else:
                    pass
            elif ctrl == 1:
                if i<room:
                    break
            elif ctrl == 2:
                price = i*room*time
            elif ctrl == 3:
                name = i
            elif ctrl == 4:
                address = i
                print(x,'.', name, 'in', address)
                print("Total cost: ", price, 'rupees')
            elif ctrl == 5:
                print("With features:", end = '\n \n')
                for f in i:
                    print(f)
                print()

            ctrl += 1


        ctrl = 0

    print()

    x += 1




    bok = str(input("Enter the full name of the hotel to book  (case sensitive): "))
    for f in backpack:

        if bok == f[3]:
            f[1] -= room

        price = f[2]*room*time
        name = f[3]




    print("Okay! Hotel successfully booked", end ='\n \n \n')


    print("          REPORT:          ", end = '\n \n \n')
    print(room, 'booked')
    print("in", name)
    print("for", time)





    restart()



def Signup():

    user = str(input("\nAre you a customer or a hotel executive?: "))

    if  'executive' in user or 'hotel' in user:

        user = 'hotel'





    if 'customer' in user:
        user = 'customer'

    username = input("Enter a username: ")

    if username in users and user == 'customer':
        print("\nUsername already exists ")
        Signup()

    elif user == 'customer' and username not in users:

        password = input("Enter a password for your account: ")
        users[username] = password
        print("Alright! You're all ready to go!")
        start()

    elif user == 'hotel' and username in executives:
        print("\n Username already exists ")
        Signup()

    elif user == 'hotel' and username not in executives:
        password = input("Enter a password for your account: ")
        executives[username] = password
        print("Alright! You're all ready to go!")
        starthotel()


def Login():
    user = str(input("\nAre you a customer or a hotel executive?: "))

    if  'executive' in user or 'hotel' in user:
        user = 'hotel'





    if 'customer' in user:
        user = 'customer'



    username = str(input("Enter your username correctly: "))
    password = str(input("Enter your account password: "))

    if user == 'customer':

        if  users[username] == password:

            print("Welcome back", username, "Let's continue")
            start()
        elif   users[username] != password:


            print("Invalid username or password")
            Login()

        elif username  not in users and username  in executives:
            print("This is a Executive login, not a customer one")
            trya = str(input("Do you want to switch to a executive login?: "))
            if trya in y1:
                user = 'hotel'
                login()
            else:
                login()

        elif username not in users and username not in executives:
            print("Invalid username entered. Neither a valid customer username")
            trya = str(int("Do you want to try again?: "))
            if trya in y1:
                 login()

            elif trya in n:
                print("Okay. Farewell")
                quit()

            else:
                print("Invalid input")
                trya = str(int("Do you want to try again?: "))


    elif user  == 'hotel':


        if executives[username] == password:

            print("Welcome back", username, "Let's continue")


        elif executives[username] != password:
            print("Incorrect password entered")
            trya = str(int("Do you want to try again?: "))
            if trya in y1:
                 login()

            elif trya in n:
                print("Okay. Farewell")
                quit()

            else:
                print("Invalid input")
                trya = str(int("Do you want to try again?: "))


        elif username in users and username not in executives:
            print("This is a customer login, not a executive one")
            trya = str(input("Do you want to switch to a customer login?: "))
            if trya in y1:
                user = 'customer'
                login()
            else:
                login()

        elif username not in users and username not in executives:
            print("Invalid username entered. Neither a valid customer username")
            trya = str(int("Do you want to try again?: "))
            if trya in y1:
                 login()

            elif trya in n:
                print("Okay. Farewell")
                quit()

            else:
                print("Invalid input")
                trya = str(int("Do you want to try again?: "))




def askuser():
    status = input("Have you registered yet? Press q to quit: ")
    if status == "q" or status == "Q":
        quit()

    elif status in y1:
        Login()

    elif status in n:
        Signup()

    else:
        print("And that, we call as non-, *cough* invalid input")
        status = input("Have you registered yet? Press q to quit: ")









def userdetails():
    nameuser = str(input("\n Kindly enter your name: "))
    adduser = str(input("\n Kindly enter your detailed home address: "))
    phno = int(input("\n Kindly enter your personal contact number: "))
    chckin = int(input("\n Kindly enter your checkin date in datemonthyearformat: (for e.g. 7120) "))
    chckout = int(input("\n Kindly enter your checkout date in datemonthyear format: "))


def registerhotel():


    a = []
    c = randomString()
    print("Hello and welcome to HMSY's registration process!", 'We will need the following asked details about your hotel:', sep = '\n')
    state = str(input("Enter the state in which your hotel is: "))
    name = str(input("Enter the unique name of your hotel: "))
    address = str(input("Enter detailed address: "))
    roo = int(input("Enter no of rooms availaible: "))
    price = int(input('Enter price per night for one room: '))
    features = []
    n = int(input('How many extra features would you like to mention?: '))
    for i in range (n):
        feature = str(input("Enter feature: "))
        features.append(feature)


    a.append(state)
    a.append(roo)
    a.append(price)
    a.append(name)
    a.append(address)
    a.append(feature)
    backpack[c] = a
    print("For future editing purposes, your hotel id is: ", c, sep ='')
    print("Hotel successfully registered")
    restart()





def  edithotel():
    id1 = str(input("\nEnter your Hotel's ID: "))

    while id1 not in backpack:
        print("\ninvalid ID no")
        id1 = str(input("\nEnter your Hotel's ID: "))
    else:
        print('\nAs Provided before, your Hotel\'s details are as follows: ')
        m = backpack[id1]
        ctrl = 0
        x = 0
        for i in m:
            if ctrl == 0:
                x = 'State'
            elif ctrl == 1:
                x = 'Rooms availaible'
            elif ctrl == 4:
                x = 'Detailed address'
            elif ctrl == 2:
                x = 'Price per room'
            elif ctrl == 3:
                x = 'Name of hotel'

            print(x, ": ", i, sep = '')
            print()
            ctrl += 1
    print("\nPlease confirm the details: ")
    x = str(input("\nAre there any changes required? : "))
    if x in n:
        print("\nOkay, we are good to move on")

    elif x in y1:

        mg = str(input("Are there multiple mistakes?: "))
        while mg not in y1 and mg not in n:
            print("invalid input")
            mg = str(input("Are there multiple mistakes?: "))

        if mg in n:


            op = str(input("\nIn which detail is the change needed? (Name/Rooms availaible/address/Price per room/): "))
            ent = input("\nEnter corrected value of credential: ")
            if op == 'state':
                i = 0

            elif op == 'rooms availaible':
                i = 1

            elif op == 'address':
                i = 4

            elif op == 'price per room':
                i = 2

            elif op == 'name':

                i = 3

            m[i] = ent

        elif mg in y1:
            n = str(input("Is there a mistake in the state?: "))
            a = str(input("Is there a mistake in the rooms availaible?: "))
            ad = str(input("Is there a mistake in the address?: "))
            ge = str(input("Is there a mistake in the price? : "))
            me =  str(input('Is there a mistake in the name?: '))
            if n in y1:
                z = input("Enter correct state: ")
                m[0] = z
            elif a in y1:
                z = input("Enter correct rooms: ")
                m[1] = z

            elif ad in y1:
                z = input("Enter correct address: ")
                m[2] = z

            elif ge in y1:
                z = input("Enter correct price: ")
                m[3] = z

            elif me in y1:
                z = input("Enter correct name: ")
                m[4] = z

        print("Corrected details: ")


        ctrl = 0
        x = 0
        for i in m:
            if ctrl == 0:
                x = 'State'
            elif ctrl == 1:
                x = 'Rooms availaible'
            elif ctrl == 2:
                x = 'Price per room'
            elif ctrl == 3:
                x == 'Name of hotel'

            elif ctrl == 4:
                x == 'Detailed address of hotel'
            print(x, ": ", i, sep = '')
            print()
            ctrl += 1



    restart()






def starthotel():
    print("Hello and welcome")
    status = str(input("Do you want to edit or register a hotel?: "))
    if 'register' in status:
                 registerhotel()

    elif 'edit' in status:
                 edithotel()






def restart():
    end = str(input("Do you want to edit, register or test out the hotel booking process?: "))

    if 'register' in end:
        registerhotel2()


    elif 'edit' in end:
        edithotel2()


    elif 'test' in end or 'book' in end:
        pickle.dump( users, open("save6.p", "wb"))
        pickle.dump(backpack, open("save8.p", "wb"))
        databasehotel
        start()


    else:
        q = str(input("Do you want to quit?: "))
        if q in y1:
            quit()

        else:
            restart()




def randomString(stringLength=10):

    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))








#EXECUTION






askuser()








#EXIT
pickle.dump( users, open("save16.p", "wb"))
pickle.dump(backpack, open("save17.p", "wb"))
pickle.dump(executives, open("save19.p", "wb"))

databasehotel
