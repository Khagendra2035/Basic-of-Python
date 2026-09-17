#STRINGS AND CONDITIONAL STATEMENTS
# str1="Hello, World!\n I'm new in this world of programming"
# str2='Python is fun. \t Kidding!!!'
# str3="""Python is a programming language that lets you work quickly and integrate systems more effectively."""
# str4='''Python is a programming language that lets you work quickly and integrate systems more effectively.'''
# print(str1)
# print(str2)
# print(str3)
# print(str4)

#BASIC OPERATIONS
#CONCATENATION
# str="hello"
# str1="world"
# str2=str+str1
# print(str2)

#LENGTH OF STRINGS
# str="hello"
# str1="how are you"
# str2=str+"  "+str1
# print(len(str2))
# print(len(str1))
# print(len(str)) 

#INDEXING AND SLICING
str="PCPS COLLEGE"
# Ind=str[0]
# Ind1=str[5]                   #in indexing we can only excess not access the value of string
# print(Ind)
# print(Ind1)

#SLICING
# str="I'm learning at PCPS COLLEGE"
# print(str[4:20])                   #slicing is used to access the value of string
# print(str[:len(str)])           
# print(str[:20])
# print(str[5:len(str)])
# #negative indexing
# print(str[-10:-1])
# print(str[-10:len(str)])


# #STRING FUNCTIONS
str="I'm learning programming."
# print(str.endswith("programming."))  #check if string ends with given value
# print(str.startswith("I'm"))  #check if string starts with given value  
# print(str.count("a"))  #count the number of occurences of given value in string
# print(str.find("programming"))  #find the index of given value in string
# print(str.replace("programming","Python"))  #replace the given value in string with new value
# print(str.upper())  #convert string to uppercase.
# print(str.lower())  #convert string to lowercase.
# print(str.capitalize())  #convert first character of string to uppercase.
# print(str.title())  #convert first character of each word in string to uppercase.


##PRACTISE QUESTIONS##
#WAP to input user's name and print its length.
# a = input("Enter your full name=")
# print("your name length is:",len(a))

#WAP to find the occurrence of'$' in a String.
# str="the $ is the currency of USA where $ means $ is dollar."
# print(str.count("$"))

#CONDITONAL STATEMENTS
# age= 18                    #voting eligibility
# if (age>18):
#     print("You are eligible to vote.")
# elif (age==18):
#     print("You are eligible to vote but you have to wait for your birthday.")
# else:
#     print("You are not eligible to vote.")
# print("Thank you for using our service.")

#TRAFFIC LIGHT PROGRAM
# light=input("Enter the color of the traffic light=")
# if(light=="green"):
#  print("you can go")
# elif(light=="red"):
#  print("stop! stop! stop!")       #spcae before print is called indentation 
# else:
#  print("wait look and go carefully")
#print("Thank you for using our service.")

# age= int(input("Enter your age: "))
# if (age>18):
#     print("you can try for driving license")
# elif (age==18):
#     print("you can try for driving license but you have to wait for your birthday.")
# else:
#     print("you are not eligible for driving license.")
# print("end of code......")



#CONDITIONAL STATEMENTS
# marks=int(input("enter your marks: "))
# if (marks>=90):
#     print("you got 'A' grade")
# elif (marks>=80 and marks<90):
#     print("you got 'B' grade")
# elif(marks>=70 and marks<80):
#     print("you got 'C' grade")
# else:
#     print("you got 'D' grade")
# print("!!best of luck and keep working hard for better results.!!")

#NESTING CONDITIONAL STATEMENTS
# age=int(input("Eneter your age: "))
# if (age>=18):
#     if(age>18):
#         print("you can marry")
#     else:
#         print("you can marry but you have to wait for your birthday.")
# else:
#     print("you are not eligible for marriage.")

# print("!!!end of code......!!!")

###PRACTISE QUESTIONS####
#WAP to check if a number enered by the user is odd or even.
# a=int(input("enter a number="))
# if(a%2==0):
#  print("this is an even number")
# else:
#  print("this is an odd number.")
# print("'''''END'''''")

#WAP to find the greatest of 3 numbers entered by the user.
# a=int(input("Enter your first nnumber="))
# b=int(input("Enter your second nnumber="))
# c=int(input("Enter your third nnumber="))
# if(a>b and a>c):
#     print(a," is the greatest number.")
# elif(b>a and b>c):
#     print(b," is the greatest number.")
# else:
#     print(c,"is the greatest number.")
# print("??DO you find your greatest number???")

#WAP to check if a number is a multiple of 7 or not.
a=int(input("Enter your number="))
if(a%7==0):
    print("This is the multiple of 7.")
else:
    print("This is not the multiple of 7.")

