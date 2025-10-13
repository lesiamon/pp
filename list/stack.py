#basic operation on stack
'''
push
pop
peek    
is_empty
size
'''
'''
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print('stack:', stack)
#peek
topElement = stack[-1]
print('top element:', topElement)
#pop
poppedElement = stack.pop()
print('pop:', poppedElement)
#stack after pop
print('stack after pop:', stack)
#is_empty   
isEmpty = not bool(stack)
print('is stack empty:', isEmpty)
#size
size = len(stack)       
print('size of stack:', size)
'''

class Person:
    def __init__(self, name,age):
        self.name= name
        self.age= age

    def  greet(self):
        print(f"hello my name is {self.name} and i am {self.age} years old")

p1= Person("lesi", 24)
p1.greet()
p2= Person("lucky", 26)
p2.greet()
p3= Person("linda", 30)
p3.greet()