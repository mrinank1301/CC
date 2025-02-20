#programe to merge 2 linked lists

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.head=self

    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=newNode
    
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data, end="->")
            temp=temp.next
            
    def Sort(self):
        temp=self.head
        while temp is not None:
            next=temp.next
            while next is not None:
                if temp.data>next.data:
                    temp.data,next.data=next.data,temp.data
                next=next.next
            temp=temp.next

class Merge:
    def merge(self,l1,l2):
        temp=l1.head
        while temp.next is not None:
            temp=temp.next
        temp.next=l2.head

class MergePoint:
    def mergePoint(self,l1,l2):
        temp1=l1.head
        temp2=l2.head
        while temp1 is not None and temp2 is not None:
            temp1=temp1.next
            temp2=temp2.next
        return temp1

class RemoveDuplicate:
    def removeDuplicate(self,l1):
        temp=l1.head
        while temp.next is not None:
            if temp.data==temp.next.data:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return l1

if __name__=="__main__":
    l1=Node(60)
    l2=Node(20)
    l1.insertAtEnd(10)
    l1.insertAtEnd(20)
    l1.insertAtEnd(20)
    l1.insertAtEnd(40)
    l1.insertAtEnd(50)
    l1.printList()
    print("\n sorted list is :")
    l1.Sort()
    l1.printList()
    print("\n===================================================")
    l2.insertAtEnd(60)
    l2.insertAtEnd(110)
    l2.insertAtEnd(80)
    l2.insertAtEnd(80)
    l2.insertAtEnd(100)
    l2.printList()
    print("\n sorted list is :")
    l2.Sort()
    l2.printList()
    print("\n===================================================")
    merge = Merge()
    merge.merge(l1,l2)
    print("\n merged list is :")
    l1.printList()
    print("\n===================================================")
    mergePoint=MergePoint()
    print("\n merge point is :")
    print(mergePoint.mergePoint(l1,l2).data)
    print("\n===================================================")
    removeDuplicate=RemoveDuplicate()
    print("\n list after removing duplicates :")
    removeDuplicate.removeDuplicate(l1).printList()
    