class Queue_Two_Stacks():

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, item):
        self.stack_1.append(item)
        #print(self.stack_1)

    def Add_Stack1_to_Stack2(self):
        if len(self.stack_2) == 0:
            # If stack_1 is empty, raise an error
            if len(self.stack_1) == 0:
                raise IndexError("Can't dequeue from empty queue!")

            # while stack_1 is not empty,
            # move items from stack_1 to stack_2, reversing order
            while len(self.stack_1) > 0:
                last_stack_1_item = self.stack_1.pop()
                self.stack_2.append(last_stack_1_item)
                print(self.stack_2)
        # return the last item in stack_2, which is the first
        # item that entered stack_1 (FIFO!)
        return self.stack_2

    def Display_Stack(self):
        my_list = self.stack_1
        for i in range(len(my_list)):
            print(my_list[i])
    def deque(self):

        if len(self.stack_2) == 0:
            raise IndexError("Stack 2 is Empty")
        else:
            n = len(self.stack_2)
           # print(n)
            while n >= 1:
                pop_val = self.stack_2.pop()
                n = n-1
                print(":",pop_val)
my_obj = Queue_Two_Stacks()
size = int(input("Enter The Size of the  Stack_1:"))

for i in range(0,size):
    val = int(input("Enter The value to the Stack_1:"))
    my_obj.enqueue(val)
my_obj.Display_Stack()
print(my_obj.Add_Stack1_to_Stack2())
print('-----------------------------------------------------------')
print(my_obj.deque())
#my_obj.Display_Stack()