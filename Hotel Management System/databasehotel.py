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
if os.path.exists('save20.p'):
    with open('save20.p', 'rb') as f:
        executives = pickle.load(f)


if os.path.exists('save8.p'):
    with open('save18.p', 'rb') as f:
        backpack = pickle.load(f)


if os.path.exists('save15.p'):
    with open('save15.p', 'rb') as f:
        users = pickle.load(f)

#USE OF pickle'

pickle.dump(users, open("save16.p", "wb"))
pickle.dump(backpack, open("save17.p", "wb"))
pickle.dump(executives, open("save19.p", "wb"))
