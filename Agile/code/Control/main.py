#THE COMMIT HAS WORKED
#second trial worked
import os
import sys

sys.path.append(os.path.join('D:/', 'Projects', 'Agile','Agile','code','Model','login'))
from tableClass import logintable

def checkloginControl(type , usertuple):
    queryobj=logintable(type)
    result = queryobj.getloginquery()
    isacceptable=False
    for row in result:
        if (usertuple == row):
            isacceptable = True
            return isacceptable
    return isacceptable






