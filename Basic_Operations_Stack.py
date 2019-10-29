class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def Display_Stack(self):
        my_list = self.items
        for i in range(len(my_list)):
            print(my_list[i])
    def Seek(self):
        if not self.Empty():
            return self.items[-1]
    def Empty(self):
        return self.items == []
my_stack = Stack()
ele = int(input("Enter the How many Element to be Entered:"))
for i in range(ele):
    value = input("Enter the Values:")
    my_stack.push(value)
    #value = int(input("Enter the How many Element to be Entered:"))
my_stack.Display_Stack()
#my_stack.push('B')
#my_stack.push('C')5
#my_stack.push('E')
#print(my_stack.Display_Stack())
#my_stack.pop()
#print(my_stack.Display_Stack())

#my_stack.push('D')
#print(my_stack.Display_Stack())
#my_stack.pop()
#print(my_stack.Display_Stack())
#my_stack.pop()
#print(my_stack.Display_Stack())
#my_stack.pop()
#print(my_stack.Display_Stack())

