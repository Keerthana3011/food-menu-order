class parent1:
    def num(self,a,b):
        print(a+b)


class child1(parent1):
    def num1(self):
        print("child1")

class child2(parent1):
    def num2(self):
        print("child2")


a=child1()
b=child2()
a.num1()
b.num2()
a.num(5,6)
