#Queue
# Type of Queue 1.Linear  2.Circular 3.Priority  4.Double Ended 
# defaut value is front =-1 and rear = -1

# class QueueIm:
#     def __init__(self):
#         self.front=-1
#         self.rear=-1
#         self.size=5
#         self.queue=[0]*self.size
    
#     def Enqueue(self,data):
#         if self.rear==self.size-1:
#             print("OverFlow")
#         elif self.front==-1 and self.rear==-1:
#             self.front+=1
#             self.rear+=1
#             self.queue[self.rear]=data
#         else:
#             self.rear+=1
#             self.queue[self.rear]=data

#     def Dequeue(self):
#         if self.front==self.size:
#             print("UnderFlow")
#         else:
#             print(f'{self.queue[self.front]} item dequeue')
#             self.front+=1

#     def Display(self):
#         for i in range(self.front,self.rear+1):
#             print(self.queue[i],end=",")


# choice=1
# qu=QueueIm()
# while choice!=0:
#     print("1. Enqueue")
#     print("2. Dequeue")
#     print("3. Dispaly")
#     choice=int(input())
#     if choice==1:
#         data=int(input("Enter data"))
#         qu.Enqueue(data)
#     elif choice==2:
#         qu.Dequeue()
#     elif choice==3:
#         qu.Display()


#Searching
#Linear Search  => O(n)          And Binary Search  =>   O(log n)

#Linear Search 

# def linersearch(arr,key):
#     for i in range(0,len(arr)):
#         if arr[i]==key:
#             return i
#     return -1

# li=[8,5,2,1,9,75,15,45,63,20,10,17]
# key=int(input("Enter the key to search"))
# result=linersearch(li,key)
# if(result==-1):
#     print("key not found")
# else:
#     print(f'key is found at {result +1}')

# Binary Search  It only works on sorted array  it is work on  divide and conqure 

# def Binarysearch(arr,key,low,high):
#         if low<=high:
#             mid=(low+high)//2
#             if(arr[mid]<key):
#                 return Binarysearch(arr,key,mid+1,high)
#             elif(arr[mid]>key):
#                 return Binarysearch(arr,key,low,mid-1)
#             else:
#                 return mid
    

# li=[2,3,6,15,20,25,28,42,48,79,88,99,100]
# key=int(input("Enter key value"))
# result=Binarysearch(li,key,0,len(li)-1)
# if(result==None):
#     print("key not found")
# else:
#     print(f'key found at {result+1}')

# Game Number Guessing 

# import random as rd

# num=rd.randint(1,100)
# chances=10
# while chances>0:
#     choice=int(input("Guess the Number Between 1 to 100"))
#     if choice<num:
#         print(f'You guessed low !! you have only {chances} chances available')
#     elif choice>num:
#         print(f'You guessed high !! you have only {chances} chances available')
#     else:
#         print("Congratulations !!!! broooo")
#     chances-=1


# Rock Paper Scissors

# Tree
# Type of Tree  1.Binary 2.Binary Search 3.B 4.B+ 5. Red-Black 6.Avl

#Binary Tree
# Type of Binary Tree 1.Full BT 2.Complete BT 3.Perfect BT 4.Degenerate BT 


# class node:
#     def __int__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None

# class Tree:
#     def __init__(self):
#         self.root=None

#     def createNode(self,data):
#         newNode=node(data)
#         self.insert(self.root,newNode)

#     def insert(self,root,newNode):
#         if(self.root==None):
#             newNode=self.root

#         if(self.root.left==None):
#             self.root.left==newNode
#         else:
#             return self.insert(self.root.left,data)
        
#         if(self.root.right==None):
#             self.root.right==newNode
#         else:
#             return self.insert(self.root.right,data)
        
#     def display(self):
#         self.inorder(self.root)

#     def inorder(self):
#         if root is not None :
#             self.inorder(root.left)
#             print(self.root.data,end=',')
#             self.inorder(root.right)

# t=Tree()
# t.createNode(10)
# t.createNode(20)
# t.createNode(30)
# t.createNode(40)
# t.createNode(50)
# print("Inorder Traversal")
# t.display()
     