#Oops Concepts

#Class and Objects

# class sipna:
#     a=10
#     b=20
#     def demo(self,a,b):
#         print(a,b)
# obj=sipna()
# print(obj.a)
# print(obj.b)
# obj.demo(50,60)


# class sipna:
#     a=10
#     b=20
#     def demo(self,a,b):
#         self.a=a
#         self.b=b

# obj=sipna()
# obj1=sipna()
# obj.demo(50,60)
# print(obj.a)
# print(obj.b)
# print(obj1.a)
# print(obj1.b)

#Construtor

# class sipna:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def demo(self):
#         print(self.a,self.b)

# obj=sipna(50,100)
# obj1=sipna(200,500)
# obj.demo()
# print(obj.a)
# print(obj.b)
# print(obj1.a)
# print(obj1.b)

# Inheritance

# class demo:
#     def add(self,a,b):
#         return a+b
    
# class Calculations(demo):
#     def sub(self,a,b):
#         return a-b
    
# obj=demo()
# cal=Calculations()
# print(cal.add(50,100))
# print(cal.sub(100,200))

#Mutliple Inheritance

# class demo:
#     def add(self,a,b):
#         return a+b
    
# class demo1:
#     def mul(self,a,b):
#         return a*b
    
# class Calculations(demo,demo1):
#     def sub(self,a,b):
#         return a-b
    
# obj=demo()
# cal=Calculations()
# print(cal.add(50,100))
# print(cal.sub(100,200))
# print(cal.mul(25,25))

#Mutli Level Inheritance 

# class demo:
#     def add(self,a,b):
#         return a+b
    
# class demo1(demo):
#     def mul(self,a,b):
#         return a*b
    
# class Calculations(demo1):
#     def sub(self,a,b):
#         return a-b
    
# obj=demo()
# obj1=demo1()
# cal=Calculations()
# print(cal.add(50,100))
# print(cal.sub(100,200))
# print(cal.mul(25,25))
# print(obj1.add(10,50))

#Hierarchical Inheritance
#Hybrid Inheritance



#Encaplystion

# class sipna:
#     a=10
#     def demo(self):
#         __b=50
#         print(__b)

# obj=sipna()
# print(obj.a)
# obj.demo()


#polyorism

# class sipna:
#     def add(self,a,b):
#         return a+b
# class sipna1:
#     def add(self,a,b,c):
#         return a+b+c 
    
# obj=sipna()
# obj1=sipna1()
# print(obj.add(10,20))
# print(obj1.add(10,20,30))


# class sipna:
#     def add(self):
#         print("sipna")
# class sipna1(sipna):
#     def add(self):
#         print("sipna1")
# class sipna2(sipna1):
#     def add(self):
#         print("sipna2")
# obj=sipna()
# obj1=sipna1()
# obj2=sipna2()
# for i in obj,obj1,obj2:
#     i.add()


#problem
# class intadd:
#     def add(self,a,b):
#         return a+b
                                                #error and string in missing
# class listadd:
#     def addlist(self):
#         list1=[]
#         size=int(input("Enter the size of list"))                     
#         for i in range(0,size):
#             list1.append(int(input()))
#         list2=[]
#         size=int(input("Enter the size of list"))                     
#         for i in range(0,size):
#             list2.append(int(input()))
#         return list1.extend(list2)
    
# obj=intadd()
# obj1=listadd()
# print(obj.add(50,200))
# obj1.listadd()


# class integer():
#     def add(self,a,b):
#         return a+b
    
# class string(integer):
#     def add(self,a,b):
#         return a+b
    
# class list(string):
#     def add(self,a,b):
#         c=[]
#         if len(a)!=len(b):
#             return 0
#         else:
#             for i in range(len(a)):
#                 c.append(a[i]+b[i])
#                 print(c)

# obj=integer()
# obj1=string()
# obj2=list()

# print(obj.add(10,20))
# print(obj1.add("vedant","solanke"))
# obj2.add([10,20,50,60],[60,20,40,80])

#Bubble Sort  TC=Big O (n^2)

# def bubble(arr,size):
#     for j in range(size):
#         print(f'pass {j}:')
#         for i in range(0,size-1):
#             print(f'IT {i}:',end="")
#             print(arr)
#             if(arr[i+1]<arr[i]):
#                 temp=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=temp
#     return arr

# size=int(input("Enter a size"))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(bubble(arr,size))

#Bubble Sort Optimzation

# def bubble(arr,size):
#     for j in range(size):
#         flag=False
#         print(f'pass {j}:')
#         for i in range(0,size-1):
#             print(f'IT {i}:',end="")
#             print(arr)
#             if(arr[i+1]<arr[i]):
#                 flag=True
#                 temp=arr[i]
#                 arr[i]=arr[i+1]
#                 arr[i+1]=temp
#         if flag==False:
#             break
#     return arr

# size=int(input("Enter a size"))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(bubble(arr,size))

#Selection Sort   TC=Big O (n^2)

# def selection(arr,size):
#     for j in range(0,size-1):
#         min=j
#         for i in range(j+1,size):
#             if(arr[min]>arr[i]):
#                 min=i
#         #swapping
#         temp=arr[j]
#         arr[j]=arr[min]
#         arr[min]=temp

#     return arr

# size=int(input("Enter a size"))
# arr=[]
# for i in range(0,size):
#     arr.append(int(input()))
# print(selection(arr,size))


