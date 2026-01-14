'''
age=int(input("enter the number"))
if age>=18:
    print("eligible")
else:
    print("not eligible")
'''

'''
n=int(input("enter the number : "))
if n>0:
    print("positive")
elif n==0:
     print("n is zero")
else:
    print("negative")     
'''

'''
a=int(input("enter the number : "))
b=int(input("enter the number : "))
if a%b==0:
    print("divisble")
    print(int(a/b))
elif b%a==0:    
    print("divisble")
    print(int(b/a))
else:
    print("not divisble")
'''
'''
a=eval(input("no.1 : "))
b=eval(input("no.2 : "))
c=eval(input("no.3 : "))
d=eval(input("no.4 : "))
e=eval(input("no.5 : "))
sum=a+b+c+d+e
total=500
per=(sum/total)*100
print(per)
if per>=90 and per <=100:
    print ("A")
elif per >=80 and per<=89:
    print("B")
'''

'''            

# sorting of 3 number using if else

a=int(input("enter the rnumber : "))
b=int(input("enter the number : "))
c=int(input("enter the number : ")) 
if a>b and a>c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b>a and b>c:
    if c>a:
        print(b,c,a)
    else:    
         print(b,a,c)

elif c>a and c>b:
    if b>a:
        print(c,b,a)
    else:    
         print(c,a,b)
else:
    print("all are equal")   
'''         


# #take 2 numbers from user also input operate and perform operation...
# # take an alphabet from user and tell wehther it is a vowel or consonent....
# Given an integer, determine whether it is even or odd.

# Login Authentication
# Given a username and password:
# If both are correct → "Login Successful"
# If username is correct but password is wrong → "Incorrect Password"
# Otherwise → "Invalid Username"

# Electricity Bill Calculation
# Units consumed:
# First 100 units → ₹1/unit
# Next 100 units → ₹2/unit
# Above 200 units → ₹3/unit
# Calculate and print the total bill.

# Triangle Type Identifier
# Given three sides of a triangle:
# Check if it is a valid triangle
# If valid, determine whether it is Equilateral, Isosceles, or Scalene


# Weekday or Weekend
# Given a day number (1–7), print whether it is a weekday or weekend.

# Temperature Description
# Given temperature:
# < 0 → Freezing
# 0–15 → Cold
# 16–30 → Warm
# 30 → Hot

# ATM Withdrawal
# Check if withdrawal is possible:
# Balance must be sufficient
# Amount must be a multiple of 100

# Number of Days in a Month
# Given a month number and year, print the number of days in that month (handle leap year).

'''
a=int(input("enter : "))
b=int(input("enter : "))
oper=str(input("enter : "))
if oper=="+":
    print(a+b)
elif oper=="-":
    if a>b:
        print(a-b)
    elif b>a:
        print((a-b))
    else:
        print("both are equal")
elif oper=="*":
    print(a*b)
elif oper=="/":
    if a>b:
        print(a/b)
    elif b>a:
        print(b/a)
    else:
        print("1")
else:
    print("operator is not valid")                                
'''


a=str(input("enter : "))
if a=="a" and a=="e" and a=="i" and a=="o" and a=="u":
    print("vowels")
else:
    print("consonent")