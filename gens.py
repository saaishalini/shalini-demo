def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30
gen = mygenerator() 
val = next(gen) #First item
print(val) #10

val = next(gen) #Second item
print(val) #20

val = next(gen) #Last item
print(val) #30

val = next(gen) #error 