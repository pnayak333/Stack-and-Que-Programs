class Animal_Shelter:
    def __init__(self):
        self.Entry_Dog = []
        self.Exit_Dog = []
        self.Entry_Cat = []
        self.Exit_Cat = []
    def Enque_Dog(self,Name_Dog):
        self.Entry_Dog.append(Name_Dog)
    def Enque_Cat(self,Name_Cat):
        self.Entry_Cat.append(Name_Cat)
    def Deque_Dog(self):
        if len(self.Exit_Dog)== 0:
            if len(self.Entry_Dog) == 0:
                raise NameError("No Dogs are Avialable")
            while len(self.Entry_Dog) > 0:
                Add_Dog_To_Shelter = self.Entry_Dog.pop()
                self.Exit_Dog.append(Add_Dog_To_Shelter)
        return self.Exit_Dog.pop()
    def Deque_Cat(self):
        if len(self.Exit_Dog)== 0:
            if len(self.Entry_Cat) == 0:
                raise NameError("No Dogs are Avialable")
            while len(self.Entry_Cat) > 0:
                Add_Dog_To_Shelter = self.Entry_Cat.pop()
                self.Exit_Cat.append(Add_Dog_To_Shelter)
        return self.Exit_Cat.pop()
    def Disply_Exit_Dogs(self):
        my_list = self.Exit_Dog
        for i in range(len(my_list)):
            print(my_list[i])
    def Disply_Entered_Dogs(self):
            my_list = self.Entry_Dog
            for i in range(len(my_list)):
                print("Dogs:",my_list[i])

    def Disply_Exit_Cats(self):
        my_list = self.Exit_Cat
        for i in range(len(my_list)):
            print("Cats:",my_list[i])

    def Disply_Entered_Cats(self):
        my_list = self.Entry_Cat
        for i in range(len(my_list)):
            print("Cats:",my_list[i])


my_Obj = Animal_Shelter()

Animal = int(input("Enter the size of the Animal:"))
#Choice = input("Enter the Animal : 1:Cat/2:Dog")

for i in range(0,Animal):
    Choice = input("Enter the Animal : 1:Cat/2:Dog")
    if Choice == '1':
        Dog = input("Enter the Animal : ")
        my_Obj.Enque_Cat(Dog)
    elif Choice == '2':
        Cat = input("Enter the Animal : ")
        my_Obj.Enque_Dog(Cat)

my_Obj.Disply_Entered_Dogs()
my_Obj.Disply_Entered_Cats()

#print(my_Obj.Deque_Dog())
#print(my_Obj.Deque_Dog())
#my_Obj.Disply_Exit_Dogs()