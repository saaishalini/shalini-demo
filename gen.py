def data():
    yield "dog"
    yield "cat"
    yield "goat"
for animals in data():
      print(animals)

#even numbers

def even(num):
    # num=int((input("enter a number")))
    if num%2==0:
        yield num
        num=num+1
    else:
        print("odd")
print(even())


# age=int(input("enter your age")) 
# def vote():
#       if age>=18:
#           yield "eligible"
#       else:
#           print("not eligible")
         
# vote()

######
######
def addgenerator():
    a=8
    b=2
    c=a+b
    yield c
    yield b
var1=addgenerator()
print(next(var1))
print(next(var1))

 
