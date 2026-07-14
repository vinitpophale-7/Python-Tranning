#Dictonary

# di={101:"vinit",102:"sipna"}
# print(di)
# print(di.values())
# print(di.keys())

# print(di.get(101))
# # di.clear()
# print(di)
# di1=di.copy()
# print(di1)
# di1.update({103:"Kartik"})
# print(di1)
# di1.pop(103)
# print(di1)
# di1.popitem()
# print(di1)

# keys=['a','b']
# values=["vinit","pophale"]
# di2=dict.fromkeys(keys,values)
# print(di2)

#Pattern program

#opposite right angle triangle
# row=int(input("Enter the rows"))
# for i in range(1,row+1):
#     for j in range(1,i+1) :
#         print("*",end=" ")
#     print()

#opposite right angle triangle
# row=int(input("Enter Rows"))
# for i in range(1,row+1):
#     for j in range(i,row+1) :
#         print("*",end=" ")
#     print()

#square
# row=int(input("enter rows"))
# for l in range(1,row+1):
#     for m in range(1,row+1):
#         print("*",end=" ")
#     print()

#half diamond
# row=int(input("enter rows"))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for l in range(1,row+1):
#     for m in range(l,row+1):
#         print("*",end=" ")
#     print()

#triangle
# row=int(input("enter rows"))
# for i in range(1,row+1):
#     for k in range(row,i-1,-1):
#         print(" ",end='')
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()

#kite

#diamond
# row=int(input("enter rows"))
# for i in range(1,row+1):
#     for k in range(row,i,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(1,row+1):
#     for k in range(1,i+1,1):
#         print(" ",end="")
#     for j in range(row,i,-1):
#         print("*",end=" ")
#     print()


#Questions  give the range input and in between range which no is divible by 3 give addition and not is divible by 3 give addition and both differnce give 

# def rang(start,end):
#     sumdivby3=0
#     sumnotdivby3=0
#     for i in range(start,end+1):
#         print(i)
#     if(i%3==0):
#         print(i)

# rang(10,20)



# def diff(start,end,num):
#     divsum=0
#     nondivsum=0
#     for i in range(start,end+1):
#         if i%num==0:
#             divsum+=i
#         else:
#             nondivsum+=i
#     diff=abs(divsum-nondivsum)
#     return diff
# start=int(input("start: "))
# end=int(input("end: "))
# num=int(input("num: "))
# print(diff(start,end,num))


#Questions String aaaabbbbccdddzzzdv=a4b4c2d4z3v1  Capgemini 

# def string(str1):
#     str2=""
#     for i in str1 :
#         if i not in str2:
#             if str1.count(i)>1:
#                 str2+=i
#                 str2+=str(str1.count(i))
#             else:
#                 str2+=i
#     print(str2)

# str1=input("enter : ")
# string(str1)


#functions
def demo(*args):
    c=0
    for i in range():
        c+=i
    print(c)

demo(10,20)


# def demo(*kwargs):
#     print(kwargs)

# demo("vinit","start","sipna","hello")



