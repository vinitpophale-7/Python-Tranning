#Why python is called as dynamically typed language  * dynamic natural decide in run time enviromment by python interpeter *
# =>
# math = 50
# chem = 60
# phy = 70
# pi = 3.14
# name = "prahant jha "
# print(type(math))   # python interpeter (pvm) is decide which data type is given 
# print(type(chem))
# print(type(phy))
# print(type(pi))
# print(type(name))    #Ctrl+/   

# How to check the address of any variable ? ans = id() 
# =>
# #id function is use to return the adddress of variable 

# math = 50
# chem = 60
# phy = 70
# pi = 3.14
# name = "prahant jha "
# print(id(math)) 
# print(id(chem))
# print(id(phy))
# print(id(pi))
# print(id(name))

#Wap to accept three paper marks and calculate total marks, percentage and display 
#=>
# math = 50
# chem = 60
# phy = 70
# total = phy + chem + math
# percentage = total / 3.0
# print("Total Markes = ", total)
# print("Percentage =", percentage)

#What is type casting
#=>
#convert from one data type to another data type is called type casting

# print(2+2)
# print("2"+"2") # concatenation

# val1 = input("Enter first value:")   # input function by defaut is only accept the string value 
# val2 = input("Enter second value:")
# print(val1+val2)

# val3 = int(input("Enter second value:"))
# val4 = int(input("Enter second value:"))
# print(val3+val4)

#Int Type Casting
# print(int(3.14))
# #print(int(10+5j))  #error
# print(int(True)) #=1
# print(int(False)) #=0
# #print(int("4.22")) #error
# print(int("4"))
# #print(int("name")) #error

#Float Type Casting 
# print(float(3.14))
# #print(float(10+5j))  #error
# print(float(True)) #=1.0
# print(float(False)) #=0.0
# print(float("4.22")) 
# print(float("4"))
# #print(float("name")) #error

#Complex Type Casting 
# print(complex(3.14))
# print(complex(10+5j))  
# print(complex(True)) 
# print(complex(False)) 
# print(complex("4.22")) 
# print(complex("4"))
# #print(complex("name")) #error
# print(complex(5,-3))
# print(complex(True,False))

#Bool Type casting
# print(bool(0)) #False
# print(bool(15)) #True
# print(bool(3.14)) #True
# print(bool(0.0)) #false
# print(bool(1+2j)) #True
# print(bool(0+0j)) #false
# print(bool(-1)) #True
# print(bool(False)) #False
# print(bool(True)) #True
# print(bool()) #False
# print(bool("name")) #True

#Swapping number using third variable 
# val1=int(input("Enter the First Number"))
# val2=int(input("Enter the Second Number"))
# temp=val1
# val1=val2
# val2=temp
# print("first number :",val1,"second number :",val2)

#Swapping without using third variable
# val1=int(input("Enter the First Number"))
# val2=int(input("Enter the Second Number"))
# val1=val1+val2
# val2=val1-val2
# val1=val1-val2
# print("first number :",val1,"second number :",val2)

#Simple Interest
# principal = int(input("Enter principal amount :"))
# rate_of_interest = float(input("Enter ROI :"))
# time = float(input("Enter the Duration of laon amount :"))
# simple_interest = principal*rate_of_interest*time/100
# print(simple_interest)

#Compound Interest
# principal = int(input("Enter principal amount :"))
# rate_of_interest = float(input("Enter ROI :"))
# time = float(input("Enter the Duration of laon amount :"))
# compound_interest = (principal*(1+(rate_of_interest/time)))^time
# print(compound_interest)

# #Area of Circle
# pi=3.14
# radius = float(input("Enter Radius of Circle : "))
# Area=pi*radius*radius
# print(Area)

#Circumference of Circle
# pi=3.14
# radius = float(input("Enter Radius of Circle : "))
# Circumference=2*pi*radius
# print(Circumference)

#Convert Height Feet To Inch and Centimeter
# h=float(input("Enter the Height in feet :"))
# inch = h*12
# cm = inch * 2.54
# print(inch)
# print(cm)

#Reverse Number  //=> floor division  %=> Modulo Division
# num = 123
# a=num%10 # a=3
# num = num // 10 #num=12
# b = num%10 #b=2
# c = num // 10 #c=1 
# reverse = a*100+b*10+c
# print(reverse)

# Reverse num = 1234567
# num = 1234567
# a = num %10
# num = num // 10
# b = num % 10 
# num = num // 10
# c = num % 10 
# num = num // 10
# d = num % 10 
# num = num // 10
# e = num % 10 
# num = num // 10
# f = num % 10 
# g=num //10
# rev = a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g
# print(rev)

# Centigrade to Fahreheit
# c = float(input("Enter the Tempeature in Centigrade : "))
# f = 1.8*c+32
# print("Fahreheit : ",f)


# address comparison the we go for identity operators  two types of identity operators 1} Is 2} Is not

# memory management
# math = 50
# chem = 50
# eng = 80
# phy = 50
# print(id(math))
# print(id(chem))
# print(id(phy))
# print(id(eng))

#identity operators 
# x=10
# y=10
# z = 20
# print(x is y)
# print(x is not y)
# print(x is z)
# print(x is not z)

#MemberShip Operators
# by using this we check object is present or not in collection of data structure (list,tuple,set,dict,string)
#Types of Membership Operators
#in 
#not in

# name ="help4code"
# print('p' in name)
# print("4" not in name)
# print('z' in name)
# print("5" not in name)

#Slicing String

# name = "vinitpophale"
# print(name[0])
# print(name[1])
# print(name[-1])
# #print(name[15]) #error out of range
# print(name[0:5]) #end-1
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[1:10:3])
# print(name[::-1]) #*IT IS USE OF REVERSE THE STRING*

#Find
# s = "help4code is a best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))

#Join
# s="vinit","yadhnesh","vedant"
# m='$'.join(s)
# print(m)

#lower,upper,swapcase,title,capitalize
# s="Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

#format
# print('Subject Marks :')
# phy=50
# chem=60
# math=70
# print("physics ={} chemistry ={} Math ={} ".format(phy,chem,math))
# print("physics ={0} chemistry ={1} Math ={2} ".format(phy,chem,math))
# print("physics ={x} chemistry ={y} Math ={z} ".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total Marks",f"{total}")
# print("Roll No=","7".zfill(4))


#1. rstrip()===>To remove spaces at right hand side
#2. 1strip()===>To remove spaces at left hand side
#3. strip() ==>To remove spaces both sides

# programming=input("Enter your programming Name:")
# p_name=programming.rstrip()
# if p_name=='Python':
#     print(p_name)
# elif p_name=='Java':
#     print(p_name)
# elif p_name=="Cpp":
#     print(p_name)
# else:
#     print("Wrong programming name")



# print('prashantjha777'.isalnum()) #True
# print('prashantjha'.isalpha()) #True
# print('777f'.isdigit())
# print('sdsdsdsd'.islower())
# print(''.islower())
# print('PRASHANTJ'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(''.isspace)
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))