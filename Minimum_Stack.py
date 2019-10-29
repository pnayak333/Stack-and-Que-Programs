class MinStack:
    def __init__(self):
        self.items = []
        self.Minitems = []
    def push(self,x):

        self.items.append(x)
        if len(self.Minitems) == 0 or x <= self.Minitems[-1]:
            self.Minitems.append(x)
    def pop(self):
        if len(self.items) == 0:
            return None
        if self.items[-1] == self.Minitems[-1]:
            self.Minitems.pop()
        return self.items.pop()
    def top(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]
    def getmin(self):
        if len(self.Minitems) == 0:
            return None
        else:
            return self.Minitems[-1]
    def Display(self):
        if len(self.items) == 0:
            return None
        else:
            print(self.items)

my_obj = MinStack()
my_obj.push(10)
my_obj.push(20)
my_obj.push(30)
#my_obj.push(40)
#my_obj.push(50)
#my_obj.push(5)
my_obj.Display()
print(my_obj.top())
print(my_obj.getmin())
#print(my_obj.pop())
#my_obj.Display()