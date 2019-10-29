class Sort_Stack:
    def __init__(self):
        self.data = []
    def push(self,x):
        self.data.append(x)
    def pop(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data.pop()
    def top(self):
        if len(self.data) == 0:
            return None
        else:
            return self.data[-1]
    def display(self):
        if (len(self.data) == 0):
            return None
        else:
            print(self.data)
    def Sort(self):
        for i in range(len(self.data)-1):
            for j in range(len(self.data)-i-1):
                if self.data[j] <= self.data[j+1]:
                    self.data[j],self.data[j+1] = self.data[j+1],self.data[j]
        return self.data


my_obj = Sort_Stack()

my_obj.push(10)
my_obj.push(5)
my_obj.push(30)
my_obj.push(40)
my_obj.display()
print(my_obj.top())
#print("pop:",my_obj.pop())
print(my_obj.Sort())
#my_obj.display()
print(my_obj.top())

