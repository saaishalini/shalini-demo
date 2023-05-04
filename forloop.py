#forloop to print each data
data = ["name", "age", "clg"]
for x in data:
  print(x)

  #forloop to print letter in a word
  for x in "name":
    print(x)
#for loop using break statement

data = ["name", "age", "year"]
for x in data:
  print(x)
  if x == "year":
    break
  
  #using continue statement
  students = ["shalini", "saranya", "sangeetha"]
for x in students:
  if x == "saranya":
    continue
  print(x)
  #range
  for i in range(0,101):
   print(i)



