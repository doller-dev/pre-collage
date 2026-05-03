# writing a code for single line input in int/float format.

print('enter your two number with common such as 3,4  65,34 ') 
a,b = map(int,input("Enter Two number ").split(","))
c=a+b
print("additon of Two No. is " ,c)

# for float value change int to float like that
#  a,b = map(float,input("Enter two number ").split(","))

d=a-b
print("substraction of Two No." ,d)

print(type(c))
print(type(d))
