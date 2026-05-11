# a=int(inut("enter your first NUmber"))
# b=int(input("enter your second Number"))

# a,b=map(int,input("enter your Number ").split(","))
# c=a+b
# print(c)

# print("value is ", a,b, sep=":",end="\n")

# d= a*b
# print("multiplication of Two Number " ,d)

# print("Addition of %d and %d is %d" %(a,b,c))
# print("value of %d is " %a)


# Roll_no = 55
# Name ="Nikhil Kumar"
# age= 20
# # str="Roll No. is {}\n Name is {}\n and Age is {}"
# # print(str.format(Roll_no, Name, age))
# str="Name is {}\n Roll No.is {}\n Age is {}"
# print(str.format(Name, Roll_no, age))

a=str(input("enter your Name "))
b=input("enter your Roll No ")
c= int(input("enter your age "))
# c= input("enter your age")
d= c>18

str="welcome buddy\n your name is {}\n your Roll No is {}\n Your age is {}\n you are become adult {}"
print(str.format( a, b, c, d,)) 
