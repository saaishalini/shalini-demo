#pandas 


#dataframe-

import pandas as role
Project={
"Team":["Project manager","Design","Developer","Testing","Marketing"],
 "Salary":["50,000","30,000","30,000","20,000","25,000"]
}
x=role.DataFrame(Project)
print(x)

###########
x=role.DataFrame(Project)
print(x.loc[2])
###########

import pandas as pd

data = {
  "students": ["shalini","sai" ,"saisha" ],
  "marks": [50, 40, 45]
}
score = pd.DataFrame(data)

print(score) 

###
x=(1,"shalini",3)
print(pd.DataFrame(x))

