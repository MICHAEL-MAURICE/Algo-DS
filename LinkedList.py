class Node:
    def __init__(self,data):
        self.value=data
        self.Next=None 


class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def insertfront(self,data):
        self.size=self.size+1
        newnode= Node(data) 
        if self.head==None:
            self.head=newnode
        else:
            newnode.Next=self.head
            self.head=newnode
    def insertEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            cur=self.head
            while cur.Next is not None:
                cur=cur.Next

            cur.Next =newNode

    def remove(self,data):
        if self.head is None:
            return

       
        curent=self.head
        prev=None

        while curent is not None and  curent.value !=data:
            prev=curent
            curent=curent.Next

        if prev is None:
            self.head=curent.Next
            self.size=self.size-1
        elif prev is not None and curent is not None :
            prev.Next=curent.Next 
            self.size=self.size-1   
        else:
            print("This Value Not Found")   

            



    def GetLength(self):
        return self.size
    
    def size2(self):
        size=0
        cur=self.head
        while cur is not None:
            size=size+1

        return size
    
    def print(self):
         cur=self.head
         while cur is not None:
             print(cur.value)
             cur=cur.Next






head=LinkedList()
head.insertfront(1)
head.insertEnd(2)
head.insertEnd(3)
head.insertEnd(4)
head.insertEnd(5)
head.remove(3)
head.print()
print(head.GetLength())

           
                            