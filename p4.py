# wap to design a circular queue(size) which should implement the below functions
# a.Enqueue 
# b.Dequeue
# c.Front
# d.Rear

class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1

    def enqueue(self,data):
        if self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        elif (self.rear+1)%self.size==self.front:
            print("queue is full")
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data

    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
        elif self.front==self.rear:
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp

    def Front(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
        else:
            return self.queue[self.front]    

    def Rear(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
        else:
            return self.queue[self.rear]
    
    def printQueue(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
        else:
            print(self.queue)
        

cq=CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)  
cq.enqueue(40)
cq.enqueue(50)
cq.printQueue()
print(cq.dequeue())
print(cq.Front())
print(cq.Rear())