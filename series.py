#series-one dimensional array

#creating a series using list
import pandas as pd
role = ["Doctor","Engineer","Teacher"]
aim = pd.Series(role)
print(aim)

################
import pandas as pd
role = ["Doctor","Engineer","Teacher"]
aim = pd.Series(role, index = ["a", "b", "c"])##### AIM[b]
print(aim)

#########labels
import pandas as pd
role = ["Doctor","Engineer","Teacher"]
aim = pd.Series(role)
print(aim[2])


import pandas as pd
students=["shalini","saranya","sangeetha","priya","nivetha"]
x=pd.Series(students)
print(x)
#####
data=("saran","sachin",1)
y=pd.Series(data)
print(y)