#findall
import re
intro= "i am shalini from Tiruchengode"
res = re.findall("i", intro)
print(res)

if (res):
  print("Yes,match success")
else:
  print("No match failure")
  ##### search
  import re
txt = "i am shalini from Tiruchengode"
x = re.search("^i.*tiruchengode$", txt)

if x:
  print("match!")
else:
  print("No match")

  ######
  msg="hiiii shalini"
  x = re.search("shalini", msg)
  print(x)

###split-Split at each white space
msg="welcome to e2infosystems"
x = re.split("\s", msg)
print(x)

######split a particular string
txt = "The rain in Spain"
x = re.split("\s", txt, 2)#split upto 2nd whitespace 
print(x)

########sub()-replace every white space character with number 2
import re
msg="welcome to e2infosystems"
x = re.sub("\s","2" ,msg)
print(x)

########sub()-replace every white space character with letter S
msg="welcome to e2infosystems"
x = re.sub("\s","S" ,msg)
print(x)

########sub()-replace every white space character with SPECIAL SYMBOLS 
msg="welcome to e2infosystems"
x = re.sub("\s","@&" ,msg)
print(x)

###match object

#The search() function returns a Match object:

txt = "welcome to e2systems"
x = re.search("info", txt)
print(x)






