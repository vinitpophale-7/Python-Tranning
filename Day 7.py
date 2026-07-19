# # LinkList

# class node:
#     def __init__(self):
#         self.data=self.head
#         self.next=None

# class LinkedList:
#     head=None
#     def InstertAtBeg(self,data):
#         newNode =node(data)
#         if(self.head==None):
#             self.head=newNode
#             newNode.next=None
#         else:
#             newNode.next=self.head
#             self.head=newNode
#     def display(self):
#         if(self.head==None):
#             print("Empty !!")
#         else:
#             temp=self.head
#             while temp!=None:
#                 print(temp.data,end="->")
#                 temp=temp.next
#             print()
#     def InstertAtEnd(self,data):
#         if(self.head==None):
            



# choice=1
# ll=LinkedList()
# while choice!=0:
#     print("1. Insert at beg")
#     print("2. Insert at end")
#     print("3. Display")
#     choice=int(input("Enter your choice : "))
#     if(choice==1):
#         data=int(input("Enter your choice : "))
#         ll.InstertAtBeg(data)
#     elif(choice==2):
#         data=int(input("Enter your choice : "))
#         ll.InstertAtEnd()
#     elif(choice==3):
#         ll.display()



# LinkList

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     head=None
#     def InstertAtBeg(self,data):
#         newNode =node(data)
#         if(self.head==None):
#             self.head=newNode
#             newNode.next=None
#         else:
#             newNode.next=self.head
#             self.head=newNode
#     def display(self):
#         if(self.head==None):
#             print("Empty !!")
#         else:
#             temp=self.head
#             while temp!=None:
#                 print(temp.data,end="->")
#                 temp=temp.next
#             print()
#     # def InstertAtEnd(self,data):
#     #     if(self.head==None):


#     def InstertAtGivPos(self,pos,data):
#         newNode=node(data)
#         if(pos==1):
#             self.InstertAtBeg(data)
#         else:
#             if(self.head==None):
#                 print("List is Empty!!")
#             else:
#                 temp=self.head
#                 i=1
#                 while i<pos-1:
#                     if temp!=None:
#                         temp=temp.next
#                         i+=1
#                     else:
#                         print("Invalid pos !!")
#                         break
#             newNode.next=temp.next
#             temp.next=newNode

#     def DeleteGivenPos(self,pos):
#         if(pos==1):
#             self.DeleteAtBeg()
#         else:
#             if(self.head==None):
#                 print("List is Empty !!")
#             else:
#                 temp=self.head
#                 i=1
#                 while i<pos-1:
#                     if temp!=None:
#                         temp=temp.next
#                         i+=1
#                     else:
#                         print("Invalid pos !!")
#                         return
#                 temp.next=temp.next.next

            



# choice=1
# ll=LinkedList()
# while choice!=0:
#     print("1. Insert at beg")
#     print("2. Insert at end")
#     print("3. Display")
#     print("4. Insert at Given Position")
#     choice=int(input("Enter your choice : "))
#     if(choice==1):
#         data=int(input("Enter your choice : "))
#         ll.InstertAtBeg(data)
#     elif(choice==2):
#         data=int(input("Enter your choice : "))
#         ll.InstertAtEnd()
#     elif(choice==3):
#         ll.display()
#     elif(choice==4):
#         pos=int(input("Enter the position : "))
#         data=int(input("Enter data : "))
#         ll.InstertAtGivPos(pos,data)
#     elif(choice==5):
#         ll.DeleteAtBeg()
#     elif(choice==6):
#         ll.DeleteAtEnd()
#     elif(choice==7):
#         ll.DeleteAtGivenPos()
        


####################All of the obove are the error code ##########################







#Stack  First In Last Out // Last In First Out   defaut empty stack top value is -1   push is add and pop is remove

class stac:
    size=5
    top=-1
    stack=[]

    def overFLow(self):
        if(self.top==self.size-1):
            return True
        return False

    def underFlow(self):
        if(self.top==-1):
            return True
        return False

    def push(self,data):
        if(self.overFLow()):
            print("OverFlow")
        else:
            self.top+=1
            self.stack[self.top]=data

    def pop(self):
        if(self.underFlow()):
            print.stack[self.top]=data
        else:
            self.top-=1

    def display(self):
        for i in range(self,self.top ,-1,-1):
            print(self.stack[i])

s=stac()
choice=1
while choice!=0:
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    choice=int(input("Enter the choice"))
    if(choice==1):
        data=int(input("Enter data to push"))
        s.push(data)
    elif(choice==2):
        s.pop()
    elif(choice==3):
        s.display()







