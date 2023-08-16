# def profile(fname, lname, password, age):
#     print( 'my name is ' + fname, lname, ', I am ' + str(age), 'and my password is: ' + str(password))
# profile('JOHN', 'james', 1234, 21)
# class Animal:
#     def __init__(self, name) -> None:
#         self.name = name
#     def fname(self):
#         print(f"the name of my dog is {self}")
#     def sound(self):
#         print(f'my dog sounds Bark! Bark! so i named it {self}')
# dog = Animal
# dog.fname('bingo')
# dog.sound('Barker')


# class Sound:
#     def __init__(self, sound) -> None:
#          self.sound = sound
#     def fsound (sound):
#         print(f"The sound my dog makes is {sound}")
# Sound.fsound('woof, woof')

class Person():
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def display(self):
        print(f'My name is  {self.name}')
    # def disploy(self):
    #     (f'and my number is  {self.number}')

class Employee(Person):
    def __init__(self, name, number, age):
        super().__init__(name, number)
        self.name = name
        self.number= number
        self.age = age
    def details(self):
        print(f'my name is {self.name}')

Joshua = Person('Joshua', 4567890)
# Joshua.display()

mgt = Employee('John', 234543234, 21)
# mgt.details()
mgt.display()

