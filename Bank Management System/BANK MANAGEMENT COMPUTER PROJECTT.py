##bank management system


import pdb
import databasebank

import math
import random
import string
import json
import pickle
import os
import sys



backpack = pickle.load( open("save13.p", "rb"))
executives = pickle.load( open("save15.p", "rb"))
users = pickle.load( open("save21.p", "rb"))


from databasebank import y1
from databasebank import n
status = ''



#####################################################################################################################
def seperate():

    print('----------------------------------------'*2)
    print('\n\n')





######################################################################################################################
def choice():
    
    cho = int(input("\n\nENTER ANY ONE OF THE FOLLOWING NUMBERS: \n1. CREATE ACCOUMT \n2. WITHDRAW FROM ACCOUNT \n3. ADD FUNDS TO ACCOUNT \n4. TRANSFER TO ANOTHER ACCOUNT  \n5. VIEW STATUS OF ACCOUNT \n(press 0 to exit): \n"))

    seperate()

    if (cho == 1):
        create()


    elif (cho == 2):
        withdraw()

    elif (cho == 3):
        add()

    elif (cho == 4):
        transfer()

    elif (cho == 5):
        view()
        

    elif (cho == 0):
        quit()
    else:
        print("\nInvalid input")
        choice()




def create():
    print("\nWelcome to creation process of BMSBY!")
    username = str(input("\nEnter any valid string for username: "))
    password = str(input("\nEnter any valid string/number for password: "))

    if username in users:
        print("ERROR! USERNAME ALREADY EXISTS, CHOOSE ANOTHER USERNAME")
        e = True
        while e  == True:
            username = str(input("\nEnter any valid string for username: "))
            if username not in users:
                e = False
        seperate()
        print('Account created!\n'+'username =',username, '\npassword =',password)
        backpack[username] = 0
        seperate()
    else:
        users[username] = password
        print('Account created!\n'+'username =',username, '\npassword =',password)
        backpack[username] = 0
        seperate()

            
        ##### TO ADD TRANSFER OR WITHDRAWL OPTION




################################################################################################################################


def withdraw():
    print("\nWelcome to withdrawl process of BMSBY!")
    username = str(input("\nEnter your username:"))
    password = str(input("\nEnter your password: "))


    ##ADD INVALID CLAUSES

    amount = int(input("\nEnter required amount to be withdrawn: "))


    x =int(backpack[username])

    x -= amount
    backpack[username] = x


    seperate()
    print("Transaction complete!")


    print('Withdrawed: ', amount, '\nFrom account: ', username)

    seperate()





########################################################################################################################

def add():

    print("\nWelcome to addition process of BMSBY!")
    username = str(input("\nEnter your username:"))
    password = str(input("\nEnter your password: "))

    ###ADD FINAL AND CURRENT ACCOUNT BALANCE

    amount = int(input("\nEnter amount to be added: "))

    
    if username not in backpack:
        print('Invalid username')
        add()
    elif username in backpack:
        backpack[username] += amount

    else:
        backpack[username] = amount
    
    print('Transaction complete!')
    print("Final account balance: ", backpack[username])
    seperate()
##################################################################################################################################


def transfer():

    print("\nWelcome to transfer process of BMSBY!")
    username = str(input("\nEnter your username: "))
    password = str(input("\nEnter your password:  "))
    
    if username not in backpack:
        print('\nInvalid username')
        transfer()

    username2 = str(input("\nEnter valid username to be transferred to: "))

    if username2 not in backpack:
        print('\nInvalid username2')
        transfer()

    amount = int(input("\nEnter amount to be transfered: "))


    backpack[username] -=amount
    backpack[username2] += amount

    print("\n \nTransaction complete!")


    
    print('Amount of: ' ,amount , '\nTransferred to: ', username2)
    print('Remaining account balance: ', backpack[username])
    seperate()



############################################################################################################
def view():
    print("Welcome to viewing section of BMSBY!:")
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))

    if username not in backpack:
        print("\nAccount does not exist")
        view()

    if users[username] != password:
        print("\nIncorrect password for", username)
        view()

    else:
        print("STATUS: ")
        print('\n')


        print("Account: "+username)
        print("Balance: ", backpack[username])


    seperate()

##############################################################################################################



print("              BANK MANAGEMENT SYSTEM                ", end = '\n \n \n \n')
print("=============================================================================")
print('\nBY: YASH PANDEY', 'OF: APJ SCHOOL SS', sep = '\n', end = '\n')
print('\n\n\n\n=============================================================================')



summary = []


print("CAUTION!!: EXECUTE ONLY IN PYTHON SHELL")
print("CAUTION!:  TO PERFORM ACTIONS WITH AN ACCOUNT CREATED IN CURRENT WINDOW, RENITIALISE PROGRAM")
choice()



########################################################################################




pickle.dump(users,open("save12.p", "wb"))
pickle.dump(backpack,open("save14.p", "wb"))
pickle.dump(executives,open("save16.p", "wb"))

databasebank


backpack = pickle.load( open("save13.p", "rb"))
executives = pickle.load( open("save15.p", "rb"))
users = pickle.load( open("save21.p", "rb"))

choice()




