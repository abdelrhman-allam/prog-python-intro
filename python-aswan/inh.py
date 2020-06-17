class Person():
    
    def __init__(self, name, age):
        print(self)
        self.__name = name
        self.age = age

    def talk(self, message = "hello"):
        print(message, "my name is " , self.__name , " and I am "+ str(self.age) + " year old")    
     
    def set_name(self, name):
        name = name.upper()

        self.__name = name
    def get_name(self):
        return self.__name

class Employee(Person):
    def __init__(self, name, job, salary, age):
        super().__init__(name, age)       
        self.job = job
        self.salary = salary
    

    # def talk(self, message = 'text', _today = "someday"):
    #     print(message, 'my job is ', self.job, ' today is ' , _today)

class Student(Person):
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def talk(self, message = "good day"):
        print(message, "I am ", self.name)


    
obj = Employee("Zakria", "Pilot", 30, 35)
obj.talk()
obj.set_name("Ahmed")
print(obj.get_name())
obj.talk()
# objStudent = Student("Ayman", 9)
# objStudent.talk()

