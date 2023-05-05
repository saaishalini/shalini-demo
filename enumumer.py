from enum import Enum

class birds(Enum):
    parrot=101
    crow=201
    peacock=301

print(birds.parrot)
print(birds.crow)
print(birds.peacock)

 #accessing values
print(birds.parrot.value)
print(birds.crow.value)
print(birds.peacock.value)
for birds in birds:
    print(birds)


