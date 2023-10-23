#!/usr/bin/python3
"""returns information about his/her TODO list progress. """
import sys
import requests

EMPLOYID = int(sys.argv[1])
TODOURL = f"https://jsonplaceholder.typicode.com/todos?userId={EMPLOYID}"
USER = f"https://jsonplaceholder.typicode.com/users/{EMPLOYID}"
response = requests.get(USER)

if response.status_code == 200:
    DATA = response.json()
    TASKS = requests.get(TODOURL).json()
    com = 0
    unfinished = 0
    for task in TASKS:
        if task['completed']:
            com += 1
        else:
            unfinished += 1
    totale = com + unfinished
    print(f"Employee {DATA['name']} is done with tasks ({com}/{totale}):")
    for task in TASKS:
        if task['completed']:
            print(f"\t {task['title']}")
else:
    print(f"Request failed with status code: {response.status_code}")
