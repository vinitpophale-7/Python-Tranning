#Check the voteing Elig
# age=int(input("Enter your age : "))
# if(age>=18):
#     print("Your are Eligable")
# else:
#     print("Your are not eligable")

#three int comparison
# num1=int(input("Enter the first Number"))
# num2=int(input("Enter the second Number"))
# num3=int(input("Enter the third Number"))
# if(num1>num2):                  #logical error         #num1>num2 and num1>num3
#     print("Num 1 is greater")
# elif (num2>num3):                #logical error       #num2>num1 and num2>num3
#     print("Num 2 is greater")
# else:
#     print("Num 3 is greater")


#loops

# list = [10,20,30,'vinit',40,50,5+6j]
# for i in list:
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(1,10,3):
#     print(i) 

#evencount and oddcount

# list=[10,52,50,548,28,43,47,70,7,15,25]
# evenCount=oddCount=0
# for i in list:
#     if i%2==0:
#         evenCount+=1
#     else:
#         oddCount+=1

# print("Even : ",{evenCount},"Odd : ",{oddCount})


# num=int(input("Enter your Number")) #str
# print(num[::-1])

#Reverse the input number  @Important@

# num=int(input("Enter the Number : "))
# rev=0
# while num!=0:
#     rev=rev*10+num%10
#     num=num//10  #num//=10
# print(rev)

#palindrome

# num=int(input("Enter the Number : "))
# temp=num
# rev=0
# while num!=0:
#     rev=rev*10+num%10
#     num=num//10  #num//=10
# if temp==rev:
#     print("It is palindrome number")
# else:
#     print("It is not palindrome number")

#Digit Sum

# num=int(input("Enter the number"))
# sum=0
# while num!=0:
#     sum=sum+num%10
#     num=num//10  
# print(sum)

#Factroial 

# num=int(input("Enter the number"))
# fact=1
# for i in range(2,num+1):
#     fact*=i #fact=fact*i
# print(fact)

#Fibonacci series @Important@

# num=int(input("Enter the num"))
# a=0
# b=1
# print(a,b,end=",")
# for i in range(2,num):
#     c=a+b
#     print(c,end=",")
#     a=b
#     b=c

#AmStrong Number

# num=int(input("Enter Number : "))
# temp=num
# count=len(str(num))
# sum=0
# while num!=0:
#     sum+=(num%10)**count
#     num//=10
# if temp==sum:
#     print("A")
# else:
#     print("NA")











