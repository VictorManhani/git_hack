# https://www.programiz.com/python-programming/json

import json
import git
import os
import random
import pytz
import datetime

repo = git.Git()

# n is the quantity of the commits
def make_commit(n):
    if n == 0:
        return repo.push()

    # x is the week and y is the day.
    x = random.randint(0,49)
    y = random.randint(0,6)
    days = datetime.timedelta(days = 364)
    x = datetime.timedelta(weeks = x)
    y = datetime.timedelta(days = y)
    today = datetime.datetime.now(pytz.utc)
    DATE = str(today - days + x + y)
    FILE_PATH = 'data.json'

    data = {"date": str(DATE)}
    print(data['date'])
    
    with open(FILE_PATH, 'w') as json_file:
        json.dump(data, json_file)

    print([arquivo for arquivo in os.listdir('.')])
    repo.add([arquivo for arquivo in os.listdir('.')])
    repo.commit(m = DATE, date = DATE)
    n -= 1
    make_commit(n)

make_commit(1)