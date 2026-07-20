# s = input("Enter a string: ")

# hashes = ""
# chars = ""

# for ch in s:
#     if ch == "#":
#         hashes += ch
#     else:
#         chars += ch

# result = hashes + chars

# print("Output:", result)

#Back Tracking

# arr=[1,2,3]
# def subset(index,result):
#     if index==len(arr):
#         print(result)
#         return
#     subset(index+1,result+ [arr[index]])

#     subset(index+1,result)

# subset(0,[])


# #Call of above program

# subset(0,[]) # Include
# s(1,[1])    # Include
# s(2,[1,2])  # Include
# s(3,[1,2,3])    # Include
# s(1,[])    # Exclude 

# s(2,[1])    # Include
# s(3,[1,2])  # Include


# Greedy Algorithm example


# coins=[10,5,2,1]
# amount=20
# result=[]
# for i in coins:
#     while amount>=i:
#         result.append(i)
#         amount-=i

# print(result)
# print(len(result))


# Mini Project 

data={}

def Register():
    rollno=int(input("Enter roll no for register:"))
    name=input("Enter Name :")
    age=int(input("Enter Age :"))
    marks=0

    if rollno not in data:
        data[rollno]=[name,age,marks]
    else:
        print("Roll no already there use another one !!")

def Serach():
    rollno=int(input("Enter roll no to serach"))
    if rollno not in data:
        print("Student is not in Database")
    else:
        print("Student is in Database")

def Update():
    rollno=int(input("Enter roll no to update :"))
    marks=int(input("Enter marks to update :"))
    if not data[rollno]:
        print("Student data not exit")
    data[rollno][2]=marks
    print("Marks Updated Successfully")

def Marks():
    rollno=int(input("Enter roll no to enter marks :"))
    marks=data[rollno][2]
    print(f"Marks of this student is {marks}")

def Display():
    rollno=int(input("Enter roll no to display:"))
    if rollno in data:
        print(f'Name->{data[rollno][0]}')
        print(f'age->{data[rollno][1]}')
        print(f'marks->{data[rollno][2]}')
    else:
        print("Student not Exit !!")

choice=1
while choice!=0:
    print("_________________________________Student Management System_____________________________________")
    print("1. Register new Student")
    print("2. Display Data of Student")
    print("3. Search Student")
    print("4. Enter Mark for Student")
    print("5. Update Student Data")
    choice=int(input("Enter the choice :"))

    if choice==1:
        Register()
    elif choice==2:
        Display()
    elif choice==3:
        Serach()
    elif choice==4:
        Marks()
    elif choice==5:
        Update()






