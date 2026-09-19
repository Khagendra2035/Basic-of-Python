##LOOPS IN PYTHON
# count=1                    #initial number
# while count<=10:           #stopping condition
#     print("hello")         #printing words
#     count+=1               #every step decrease or increase process
#     # print(count)

# a=1
# while a <=150:
#     print("hey")
#     a+=1
#     print(a)

#print natural numbers
# a=1
# while a<=9:
#     print("number=",a)
#     a+=1
# print("loop ended...")

##QUESTIONS  QUESTIONS
#print numbers from 1 to 100.
# a=1
# while a<=100:
#     print('number,',a)
#     a+=1
#print numbers feom 100 to 1.
# b=100
# while b>=1:
#     print("number is,",b)
#     b-=1

#print multiplication table of a number n.
# n=int(input("enter your number=")) #int after n is compulsory
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# n=int(input("enter number="))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1


#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
# num=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(num):
#     print(num[idx])
#     idx+=1

#search for a number x in this tuple using loop:
# [1,4,9,16,25,36,49,64,81,100]
# num=(1,4,9,16,25,36,49,64,81,100)
# n=int(input("enter the number="))
# i=0
# while i< len(num):
#     if (num[i]==n):
#         print("found at index=",i)
#         break
#     else:
#         print("finding...")
#     i+=1


##BREAK AND CONTINUE
# i=1
# while i<=10:
#     print(i)
#     if(i==6):
#         break
#     i+=1
# print("end of code...")

# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue #skip
#     print(i)
#     i+=1

# i=1
# while i<=10:
#     if(i%2 !=0 ):
#         i+=1
#         continue #skip
#     print(i)
#     i+=1

##FOR LOOP
# num=[1,2,3,4,5]
# for val in num:
#     print(val)

# fruits=["mango","banana","apple","pineapple","dragonfruit"]
# for val in fruits:
#     print(val)

# tup=(1,2,3,4,5,6)
# for num in tup:
#     print(num)

# str="khagendra"
# for chr in str:
#     print(chr)
# else:   #to print in the end
#     print("end")

# str="khagendra"
# for chr in str:
#     if(chr=="r"):
#         print("found..")
#         break
#     print(chr)
# else:   #to print in the end
#     print("not found")


##PRACTISE QUESTIONS
# using for
# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

# search for a number x in this tuple using loop:
#  [1,4,9,16,25,36,49,64,81,100]

##RANGE()
# num=range(7)
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# print(num[6])

# num=range(8)
# for i in num:
#     print(i)

# for i in range(8):  #range(stop)
#     print(i)

# for i in range(2,8):  #range(start,stop)
#     print(i)

# for i in range(2,50,2):  #range(start,stop,step)
#     print(i)

##PRACTISE  PRACTISE

#print numbers from 1 to 100.
#print numbers from 100 to 1.
#print the multiplication table of a number n.


#PASS STATEMENT
for i in range(1,50,2):
    pass
print("some useful works")
