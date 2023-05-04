#num=int(input("enter numerator"))
#den=int(input("enter denominator"))
#result=num/den
#print(result)
#print("bye")

#exception handling
try:
    num=int(input("enter numerator"))
    den=int(input("enter denominator"))
    result=num/den
    print(result)
except Exception:
    print("some error occured")
print("bye")

# ZERO DIVISION ERROr
try:
    num=int(input("enter numerator"))
    den=int(input("enter denominator"))
    result=num/den
    print(result)
except ZeroDivisionError:
    print("YOU CANNOT DIVIDE BY ZERO")
    print("bye")

# VALUE ERROR
try:
    num=int(input("enter numerator"))
    den=int(input("enter denominator"))
    result=num/den
    print(result)
except ValueError:
    print("ENTER NUMBERS ONLY")
    print("bye")
#no error occurs

try:
    num=int(input("enter numerator"))
    den=int(input("enter denominator"))
    result=num/den
except ZeroDivisionError:
    print("YOU CANNOT DIVIDE BY ZERO")
except ValueError:
    print("ENTER NUMBERS ONLY")
except Exception:
    print("some error occured")
else:
    print(result)
finally:
    # print ("this always executes")
    # print("bye")
    n=10
    d=0
    c=n/d
    print(c)
