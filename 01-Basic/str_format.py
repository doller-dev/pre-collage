# Write a code using Str.format with varible input value.
# Auther :- (Code Name: "Doller")                                            Date:- 06/05/2026

Name=input("Enter your Name ")
Roll_no= input("Enter your Roll No. ")
Age = int(input("Enter your age "))

Adult= Age>18

str="WELCOME TO THE SMALL CODE OF WORLD \n Your Name is {}\n Your current Roll No. is {}\n Ypur current age is {}\n Your are become adult {}"
print(str.format(Name, Roll_no, Age, Adult))

