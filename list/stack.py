#basic operation on stack
'''
push
pop
peek    
is_empty
size
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
