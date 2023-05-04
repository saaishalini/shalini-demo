class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def introduce(self):
        print(f"My name is {self.name} and I am a {self.major} major.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"My name is {self.name} and I teach {self.subject}.")

person1 = Person("Alice", 30)
person1.introduce()    # outputs: "My name is Alice and I am 30 years old."

student1 = Student("Bob", 20, "Computer Science")
student1.introduce()   # outputs: "My name is Bob and I am a Computer Science major."

teacher1 = Teacher("Charlie", 45, "History")
teacher1.introduce()   # outputs: "My name is Charlie and I teach History."
