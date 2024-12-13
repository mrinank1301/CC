#finding minimum element in stack
stack=[]

stack.append(20)
stack.append(30)
stack.append(10)
stack.append(50)

min=stack[0]
for i in range(len(stack)):
    if min>stack[i]:
        min=stack[i]

print(min)