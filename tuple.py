#tuple
#tuples cannot be changable but can convert thr tuple into list and covert back into tuplse

x=("car","bike","cycle")
y=list(x)
#y[2]="bus"
y = x[:2] + ("bus")
print(y)
#joining two tuple
a=("animals","birds"
,"humans")
b=(1,2,3,4,5,6,7,)
c=a+b
print(c)

#tuple methods
newtuple = (1,2,3,4,5,6)
x = newtuple.count(5)
print(x)