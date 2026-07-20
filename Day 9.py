# # Tree 

# In Order

# from collections import deque

# class node:
#     def __init__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None

# class Tree:
#     def __init__(self):
#         self.root=None

#     def insert(self,data):    
#         newNode=node(data)

#         if(self.root==None):
#             self.root=newNode
#             return
        
#         q=deque([self.root])

#         while q:
#             temp=q.popleft()

#             if(temp.left==None):
#                 temp.left=newNode
#                 return
#             else:
#                 q.append(temp.left)
        
#             if(temp.right==None):
#                 temp.right=newNode
#                 return
#             else:
#                 q.append(temp.right)
        
#     def display(self):
#         self.inorder(self.root)

#     def bfs(self):
#         if self.root==None:
#             print("Empty")
#             return
        
#         q=deque([self.root])

#         while q:
#             temp=q.popleft()
#             print(temp.data,end=",")
#             if temp.left!=None:
#                 q.append(temp.left)
#             if temp.right!=None:
#                 q.append(temp.right)

#     def inorder(self,root):
#         if root != None :
#             self.inorder(root.left)
#             print(root.data,end=',')
#             self.inorder(root.right)
#         return


# t=Tree()
# t.insert(10)
# t.insert(20)
# t.insert(50)
# t.insert(30)
# t.insert(40)
# t.insert(60)
# # t.display()
#print("In Order")
# t.inorder(t.root)
# # t.bfs()

# Pre Order 

# from collections import deque

# class node:
#     def __init__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None

# class Tree:
#     def __init__(self):
#         self.root=None

#     def insert(self,data):    
#         newNode=node(data)

#         if(self.root==None):
#             self.root=newNode
#             return
        
#         q=deque([self.root])

#         while q:
#             temp=q.popleft()

#             if(temp.left==None):
#                 temp.left=newNode
#                 return
#             else:
#                 q.append(temp.left)
        
#             if(temp.right==None):
#                 temp.right=newNode
#                 return
#             else:
#                 q.append(temp.right)
        
#     def display(self):
#         self.inorder(self.root)

#     def bfs(self):
#         if self.root==None:
#             print("Empty")
#             return
        
#         q=deque([self.root])

#         while q:
#             temp=q.popleft()
#             print(temp.data,end=",")
#             if temp.left!=None:
#                 q.append(temp.left)
#             if temp.right!=None:
#                 q.append(temp.right)

#     def preorder(self,root):
#         if root != None :
#             print(root.data,end=',')
#             self.preorder(root.left)
#             self.preorder(root.right)
#         return


# t=Tree()
# t.insert(10)
# t.insert(20)
# t.insert(50)
# t.insert(30)
# t.insert(40)
# t.insert(60)
# # t.display()
#print("Pre Order")
# t.preorder(t.root)
# # t.bfs()

# Post Order 

# from collections import deque

# class node:
#     def __init__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None

# class Tree:
#     def __init__(self):
#         self.root=None

#     def insert(self,data):    
#         newNode=node(data)

#         if(self.root==None):
#             self.root=newNode
#             return
        
#         q=deque([self.root])

#         while q:
#             temp=q.popleft()

#             if(temp.left==None):
#                 temp.left=newNode
#                 return
#             else:
#                 q.append(temp.left)
        
#             if(temp.right==None):
#                 temp.right=newNode
#                 return
#             else:
#                 q.append(temp.right)
        
#     def display(self):
#         self.inorder(self.root)

#     def bfs(self):
#         if self.root==None:
#             print("Empty")
#             return
        
#         q=deque([self.root])

#         while q:
#             temp=q.popleft()
#             print(temp.data,end=",")
#             if temp.left!=None:
#                 q.append(temp.left)
#             if temp.right!=None:
#                 q.append(temp.right)

#     def postorder(self,root):
#         if root != None :
#             self.postorder(root.left)
#             self.postorder(root.right)
#             print(root.data,end=',')
#         return


# t=Tree()
# t.insert(10)
# t.insert(20)
# t.insert(50)
# t.insert(30)
# t.insert(40)
# t.insert(60)
# # t.display()
# print("Post Order")
# t.postorder(t.root)
# # t.bfs()

# DFS

# from collections import deque

# class node:
#     def __init__(self,data):
#         self.left=None
#         self.data=data
#         self.right=None

# class Tree:
#     def __init__(self):
#         self.root=None

#     def insert(self,data):    
#         newNode=node(data)

#         if(self.root==None):
#             self.root=newNode
#             return
        
#         q=deque([self.root])

#         while q:
#             temp=q.popleft()

#             if(temp.left==None):
#                 temp.left=newNode
#                 return
#             else:
#                 q.append(temp.left)
        
#             if(temp.right==None):
#                 temp.right=newNode
#                 return
#             else:
#                 q.append(temp.right)
        
#     def display(self):
#         self.inorder(self.root)

#     def dfs(self):
#         if self.root==None:
#             print("Empty")
#             return
        
#         s=[self.root]

#         while s:
#             temp=s.pop()
#             print(temp.data,end=",")
#             if temp.right!=None:
#                 s.append(temp.right)
#             if temp.left!=None:
#                 s.append(temp.left)

#     def postorder(self,root):
#         if root != None :
#             self.postorder(root.left)
#             self.postorder(root.right)
#             print(root.data,end=',')
#         return


# t=Tree()
# t.insert(10)
# t.insert(20)
# t.insert(50)
# t.insert(30)
# t.insert(40)
# t.insert(60)
# # t.display()
# # t.postorder(t.root)
# t.dfs()


# HashMapping

# dict={}

# string=input()
# for char in string:
#     if char in dict:
#         dict[char]+=1
#     else:
#         dict[char]=1

# print(dict)

# arr=[]
# for key in dict.keys():
#     arr.append(key)
# arr.sort()
# for keys in arr:
#     print(keys,end=":")
#     print(dict.get(keys))

# Factroial By recurion

# def cal(num):
#     if num==1:
#         return num
#     return num*cal(num-1)
# num=int(input("Enter the number : "))
# print(cal(num))


# Rock Paper Sicssors

import random as rd
cmpchoice=rd.randint(1,4)
arr=["Rock","Paper","Sicssors"]
choice=1
while choice!=0:
    print("1. Rock")
    print("2. Paper")
    print("3. Sicssors")
    choice=int(input("Enter your choice"))
    
    if cmpchoice==1 and choice==3 or cmpchoice==2 and choice==1 or cmpchoice==3 and choice==1 :
        print(f'Computer Wins it chosen {cmpchoice} !!') 
    elif cmpchoice==1 and choice==2 or cmpchoice==1 and choice==3 or  












