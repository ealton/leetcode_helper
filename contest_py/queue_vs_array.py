import collections
import datetime

def queueVsArray():
    q = collections.deque()
    arr = []
    tValue = 100000000

    ts0 = datetime.datetime.now().timestamp()
    for i in range(tValue):
        q.append(i)
    ts1 = datetime.datetime.now().timestamp()
    print(f'check 1: {ts1 - ts0}')

    for i in range(tValue):
        arr.append(i)
    ts2 = datetime.datetime.now().timestamp()
    print(f'check 2: {ts2 - ts1}')

    for i in range(tValue):
        q.pop()
    ts3 = datetime.datetime.now().timestamp()
    print(f'check 3: {ts3 - ts2}')

    for i in range(tValue):
        arr.pop()
    ts4 = datetime.datetime.now().timestamp()
    print(f'check 4: {ts4 - ts3}')





queueVsArray()
