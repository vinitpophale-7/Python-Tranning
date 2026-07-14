#List and Their Functions

# list=[10,20,30,'sipna','vinit',40,50,5,1,15,35]
# print(list)

# for i in list:
#     print(i)

# for i in list:
#     print(i,end=' ')

# list.append("vinit")
# print(list)

# list.remove(50)
# print(list)

# list.clear()
# print(list)

# list.append(10)
# print(list.count(10))
# print(list)

# list.reverse()
# print(list)

# list1=list.copy()
# print(list1)

# list1=[10,20,50,30,40,1,2,5,15,100,35]
# print(list1)
# list1.sort()
# print(list1)

# list1.pop(5)
# print(list1)

# list1.extend("sipna")
# print(list1)
# list1.extend("250")
# print(list1)
# list1.extend([10,56,25])
# print(list1)

# newlist=[[10,20,30],[40,50,60]]
# print(newlist)
# for i in newlist:
#     for j in i:
#         print(j)

# for i in newlist :
#     print(i)


#remove dupicate elements form a list 
#take list by user

# list=[]
# size=int(input("Enter the size of list"))                     
# for i in range(0,size):
#     list.append(int(input()))
# print(list)
# for i in list:
#     while list.count(i)!=1:                           
#         list.remove(i)
# print(list)


#tuple

# tu=(10,20,30,40)
# print(tu)
# print(tu[2])
# print(tu.count(10))
# print(tu.index(30))


#second largerest element for even and second smallest element form odd and tip is 0 consider as a even place

# org=[]
# size=int(input("enter size of array"))
# for i in range(0,size):
#     org.append(int(input()))
# print(org)
# even=[]
# odd=[]
# even.append(org[0])
# for i in range(1,size):
#     if i%2==0:
#         even.append(org[i])
#     else:
#         odd.append(org[i])
# even.sort()
# odd.sort()
# print(f'Second largest element={even[len(even)-2]}')
# print(f'Second smallest element={odd[1]}')


#set
# s={10,45}
# s1=[10,45,89,56,23]
# s.add(88)
# s.clear()
# s.union(s1)
# s1.issuperset(s)
# s3=s1.copy()
# print(s3)
# print(s3[2])

#Swapping
#using third variable
# temp=a
# a=b
# b=temp
# #use arthimetic and without using third variable
# a=a+b
# b=a-b
# a=a-b
# #not using arthimetic operator # using XOR operators
# a=a^b
# b=a^b
# a=a^b
# # by multilpe * and divide /
# a=a*b
# b=a/b
# a=a/b



rows = int(input("Enter number of rows: "))
start = 1
for i in range(1, rows + 1):
    curr = start
    digsum = 0

    print(" "*(rows-i) , end="")
    for j in range(i):
        print(curr, end=" ")

        temp = curr
        while temp !=0:
            digsum = digsum + temp % 10
            temp //= 10

        curr += 1

    print("\n")
    start = digsum