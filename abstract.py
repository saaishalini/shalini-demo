from abc import ABC,abstractmethod

class Colleges(ABC):
    @abstractmethod
    def types (self):
        pass
class Mcollege(Colleges):
        def types(self):
            print("i am a medical college")
class Ecollege(Colleges):
        def types(self):
            print("i am a Engineering college")
class AScollege(Colleges):
        def types(self):
            print("i am a Arts and Science college")
m=Mcollege()
m.types()
e=Ecollege()
e.types()
AS=AScollege()
AS.types()


