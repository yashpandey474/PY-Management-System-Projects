import pdb
import pickle
import random
import string
import os
import sys
import math


#LIST database
y1 = ['yes', 'yeah', 'yup', 'affirmative', 'y', 'i think', 'YES', 'Yes']
n = ['no', 'not at all', 'nope', 'not yet', 'n', 'NO', 'NOPE', 'never', 'maybe', 'maybe not', 'No']
g = ['male', 'female', 'other', 'not specified']

#HOTEL database

users = {}
backpack = {}
executives = {}

#USE OF PICKLE:
if os.path.exists('save17.p'):
    with open('save17.p', 'rb') as f:
        executives = pickle.load(f)


if os.path.exists('save14.p'):
    with open('save14.p', 'rb') as f:
        backpack = pickle.load(f)


if os.path.exists('save12.p'):
    with open('save12.p', 'rb') as f:
        users = pickle.load(f)




pickle.dump(users, open("save21.p", "wb"))
pickle.dump(backpack, open("save13.p", "wb"))
pickle.dump(executives, open("save15.p", "wb"))




print(users, backpack)


      
