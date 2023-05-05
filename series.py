import pandas as pd

role = ["Doctor","Engineer","Teacher"]
aim = pd.Series(role)

print(aim)

################
import pandas as pd

role = ["Doctor","Engineer","Teacher"]


aim = pd.Series(role, index = ["a", "b", "c"])

print(aim)