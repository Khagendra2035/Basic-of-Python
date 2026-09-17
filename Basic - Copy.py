#how to print
# print("hello there!")

# VARIABLES
# name= "khagendra"
# rollno=7
# weight=52.6
# print("Your name is=",name,"Your roll no is=",rollno,"you are",weight,"kg")

#PRINT SUM
# a= 12
# b = 11
# c = a +b
# sum = c
# print(sum)

#TYPES OF OPERATORS
#operational operators
# a = 24
# b = 2
# print(a+b)
# print(a-b)
# print(a * b)
# print(a/b) 
# print(a%b) #remainder
# print(a**b)  #power operator b^a

#relational operators
# a= 23
# b= 34
# print(a==b) #if a is equal to b
# print(a!=b) #if a is not equal to b
# print(a>b) #a is greater than b
# print(a<b) #a is less than b
# print(a>=b) #a is greater than or equal to b
# print(a<=b) #a is less than or equal to b

#assignment operators
# num= 10
# # num += 5  # equivalent to num = num + 5
# num -= 3  # equivalent to num = num - 3
# # num *= 2  # equivalent to num = num * 2
# # num /= 4  # equivalent to num = num / 4
# # num %= 3  # equivalent to num = num % 3
# # num **= 2  # equivalent to num = num ** 2
# # num //= 2  # equivalent to num = num // 2
# print("num =", num)

#LOGICAL OPERRATORS(nor,and,or)
# print(not True) #not operator
# a = 10
# b = 20
# print(not (a > b)) #not operator

# val1 = True
# val2 = True
# val3 = False
# print("and operator:", val1 and val2) #and operator
# print("and operator:", val1 and val3) #and operator
# #both value must be true for and operator to return true

# val1 = True
# val2 = True
# val3 = False
# a=24
# b=34
# print("or operator:", val1 or val2) #or operator
# print("or operator:", val1 or val3) #or operator
# print("or operator:", a < b or a == b) #or operator
# #atleast one value must be true for or operator to return true

#TYPE CONVERSION
#type coversion(automatic) and type casting(manually converting one data type to another)
# #type conversion
# a=2
# b=3.5
# sum = a + b
# print(sum)
# #type casting
# x = "5" #a string
# y = 2.5
# z = int(x) + y #string is converted to integer and then added to float
# print(z)


#INPUT FUNCTION
# a= input("Enter your name: ") #input converts everything into string 
# print("Your name is:", a)
# #example of type casting with input function
# name = input("Enter your name: ")
# age = int(input("Enter your age: ")) #converting input to integer
# marks = float(input("Enter your marks: ")) #converting input to float
# print("Your name is:", name)
# print("Your age is:", age)
# print("Your marks are:", marks)

# #WRITE A PROGRAM TO INPUT 2 NUMBERES AND PRINT THEIR SUM
# a = int(input("Enter first number: "))
# b= int(input("Enter second number: "))
# sum= a + b

# print("the sum of a and b is",sum)

# #WAP TO INPUT SIDES OF SQUARE AND PRINT AREA
# a = input("enter the value of one side of square:" )
# b = input("enter the value of another side of that square=")
# L=int (a)**2
# print("area of square is=",L)

#WAP TO INPUT LENGTH AND BREADTH OF RECTANGLE AND PRINT AREA
# L=int(input("Enter the length of the rectangle="))
# B=int (input("Enter the breadth of the rectangle="))
# area =2*(L+B)
# print("the area of rectangle is =",area)

# #WAP TO INPUT 2 FLOAT NUMBERS AND PRINT THEIR AVERAGE
# a= input("enter the first float number=")
# b= input("enter the second float number=")
# c=float(float(a)+float(b))/2
# print("the average of two float numbers is=",c)

#WAP TO INPUT 2 NUMBERS AND PRINT THEIR PRODUCT
a = int(input("enter your first number="))
b=int(input("enter your second number="))
c=int(a)*int(b)
print("the product of your numbers is =",c)

#PRINT IF A NUMBER IS GREATER THAN B. IF NOT THEN PRINT B IS GREATER THAN A.
# a = int(input("enter your first number="))
# b = int(input("enter your second number="))
# if a > b:
#     print(a, "is greater than B", b)
# else:
#     print(b, "is greater than ",a)