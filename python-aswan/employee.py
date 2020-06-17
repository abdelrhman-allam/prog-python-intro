class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def talk(self):
        print("my name is " , self.name , " and I am "+ self.age + " year old")    
                
emp1 = Employee("ahmed","90", "400")
emp2 = Employee("mohamed","10", "600")
emp3 = Employee("Taha","60", "300")

emp1.talk()
emp2.talk()
emp3.talk()