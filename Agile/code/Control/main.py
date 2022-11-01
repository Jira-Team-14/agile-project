#THE COMMIT HAS WORKED
#second trial worked
import os
import sys

sys.path.append(os.path.join('D:/', 'Projects', 'Agile','Agile','code','Model','login'))
from tableClass import logintable


queryobj=logintable(2)
queryobj.getloginquery()



