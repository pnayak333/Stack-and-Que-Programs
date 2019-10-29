class Stack_Paltes:
    def __init__(self,capacity):
        self.stacks = []
        if capacity < 1:
            raise NameError("Not Possible")
        else:
            self.capacity = capacity

    def push(self,item):
        if self.stacks == []:
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) == self.capacity:
                self.stacks.append([item])
            else:
                self.stacks.append([item])
    def pop(self):
        if self.stacks == []:
            raise NameError("Empty Stack")
        else:
            ele = self.stacks[-1][-1]
            print("Pop:",ele)
            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                self.stacks[-1][-1].pop()
        return ele

    def Display(self):
        for item in range(len(self.stacks)):
            print(self.stacks[item])
    def Top(self):
        return self.stacks[-1][-1]
        #return self.stacks
my_obj = Stack_Paltes(1)

my_obj.push(10)
my_obj.push(20)
my_obj.push(30)
my_obj.push(40)
my_obj.push(50)
#print(my_obj.pop())
my_obj.Display()
my_obj.push(60)
my_obj.push(70)
my_obj.push(80)
my_obj.push(90)
my_obj.push(811)
my_obj.push(901)
my_obj.push(90)
my_obj.push(8111)
my_obj.push(9011)
#print(my_obj.Top())
#print(my_obj.pop())
my_obj.Display()




