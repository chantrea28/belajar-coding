class person:
    def __init__(self,name,age,haircolor):
        self.name = name
        self.age = age
        self.haircolor = haircolor
    def eat(self):
        msg = str(self.name)+ "can also eat"

        return(msg)

class student(person):
    pass 


object1 = student("ahmad","14","white")
print(object1.name)
print(object1.age)
print(object1.haircolor)
print(object1.eat())