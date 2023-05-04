#to print current date and time
import datetime
a=datetime.datetime.today()
print(a)
#tomorrow
import datetime
b=datetime.date.today()+datetime.timedelta(days=1)
print(b)
#YESTEDAY
import datetime
b=datetime.date.today()-datetime.timedelta(days=1)
print(b)            
#to print day and year

import datetime
a=datetime.datetime.now()
print(a.year)
print (a.strftime("%a"))