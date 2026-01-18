class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

class emp(Person):
    def __init__(self,name,age,salary,post):
        self.salary = salary
        self.post = post
        Person.__init__(self,name,age)

e1=emp("Raj",23 ,2500,"Intern")
e1.display()
print("Salary:",e1.salary)
print("Post:",e1.post)


e2=emp("marco",45,25000,"Intern")
e2.display()
print("Salary:",e2.salary)
print("Post:",e2.post)