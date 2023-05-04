def demo():
  print("hello")
  print("*******")
  demo()

#passing arguments
def demo(name):#/name-parameter
  print("hello"+ name)
demo("shalini")#/ARGUMENT
print("#######")
demo("saranya")

#using fname,lname(positional arguments)
def demo(fname,lname):
  print("hello"+fname+""+lname)
demo("shalini","alagumurugan")
print("#######")
demo("saranya","kandhasamy")

#KEYWORD ARGUMENTS
def demo(lname,fname):
  print("hello"+fname+""+lname)
demo(lname="shalini",fname="alagumurugan")
print("#######")
demo("saranya","kandhasamy")

#CALENDAR 
import calendar  
# ask of month and year  
year = int(input("Enter year: "))  
month = int(input("Enter month: "))  
# display the calendar  
print(calendar.month(year,month))  


