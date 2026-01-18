'''
def fun_name():---> FUNCTION DEFINATION--> PARAMETERIZED AND NON PARAMETERIZED
BODY

fun_name()--->FUNCTION CALL
'''

'''
def fun():
    print("hello world0")

fun()'''
'''
def sum(a,b):
    print(a+b)
x=int(input())
y=int(input())
sum(x,y)
'''
'''

def sum(a,b):
    print(a+b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print (a/b)   
def sub(a,b):
    print(a-b)

x=int(input("enter : ")) 
y=int(input("enter : "))     
op=str(input("enter : "))   
if op=="+":
    sum(x,y)
elif op=="-":
    sub(x,y)
elif op=="*" :
    mul(x,y)
elif op=="/":
    div(x,y)
else:
    print("not valid")
'''

# parameter and arguement
'''
def fun_name(a,b):--> formal parameter
BODY

fun_name(x,y) actual arguement
'''

#types
# positional arguement
'''
def sub(a,b):
    print(a-b)
x=int(input())
y=int(input())
sub(x,y)'''

# default arguement
'''
def greet(name="diya"):
    print("hello"+ name)

greet()
greet("abc")
hellodiya
helloabc'''

#keyword arguement
'''
def greet(name, msg):

    print(msg, name)

greet(msg="hello", name="diya")
greet(name="diya", msg="hello")
hello diya
hello diya'''

'''
def fun():
    x=10#---> local--> valid only in function
    print(x)
x=20#--> global #-->> valid in the whole document
print(x)
fun()
def fen2():
    print(x)
fen2()
print(x)'''


# wap to input a string and count the no. of upper and lower cases:
# oocurance count
# remove the duplicate value from the list:
# count the vowel in the string:
# sum of digit:
# check if the given key exists in the dictionary:
# odd or even in the tuple:
# factorial:
# delete an element:
# wap to multiple all the no. from the list:
# find HCF of two no.:
