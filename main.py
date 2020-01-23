# https://www.programiz.com/python-programming/json
# https://gitpython.readthedocs.io/en/stable/
# https://www.youtube.com/watch?v=2q--gA97caM
# __author__ in javascript: Akshay Saini
# __author__ in python: Victor Manhani

import json
import git
import os
import random
import pytz
import datetime

# initialize the git class
repo = git.Git()
# get the files in the current repository
files = [arquivo for arquivo in os.listdir('.')]
# file name
FILE_PATH = 'data.json'

# n is the quantity of the commits
def make_commit(n):
    # recursive resolve
    if n == 0:
        return repo.push()
    # days to be subtracted
    days = datetime.timedelta(days = 364)
    # x is the week to be add between the 0 and 49 week.
    x = datetime.timedelta(weeks = random.randint(0,49))
    # y is the day of the week to be add between 0 and 6.
    y = datetime.timedelta(days = random.randint(0,6))
    # get the now time 
    today = datetime.datetime.now(pytz.utc)
    # sum and parser to string the date
    DATE = str(today - days + x + y)
    # create a dict for save in json file
    data = {"date": DATE}
    print(data)
    # write the changes in json file
    with open(FILE_PATH, 'w') as json_file:
        json.dump(data, json_file)
    # add files in directory to stage area
    repo.add(files)
    # commit the staged files
    repo.commit(m = DATE, date = DATE)
    # increment minus 1 in the counter 
    n -= 1
    # recursive call with the n decreased
    make_commit(n)

# call the function with the n times it will be called
make_commit(1)