# wap to deal with real world situation where the stack ds is widely used in evaluation of expression:
# stacks are used to evaluate the expression, especially in  language that use postfix or prefix notation

user=input("enter the expression:")

stack=[]

users =user.split()

for i in users:    
    print(f"step by step in stack:{stack}")
    if i=="+" or i=="-" or i=="*" or i=="/":
        a=stack.pop()
        b=stack.pop()
        if i=="+":
            stack.append(b+a)
        elif i=="-":
            stack.append(b-a)
        elif i=="*":
            stack.append(b*a)
        elif i=="/":
                stack.append(b/a)
    else:
        stack.append(int(i))

print(f"stack is:{stack}")
