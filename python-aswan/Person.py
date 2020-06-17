class Person:
    name = '' # instance var
    count = 0 # class var
    def __init__(self, name):
        self.name = name # initaliaze
        # Person.count +=1
        # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.count)

    @classmethod
    def increase(cls):
        cls.count += 1

p = Person('A')

Person.increase()
print(p.name, p.count)
print(Person.count)

q = Person('q')

print(q.name, q.count)
print(p.name, p.count)
print(Person.count)
print(Person.name)
Person.name = "V"
print(Person.name)
print(q.name, q.count)
print(p.name, p.count)
print(p.description())