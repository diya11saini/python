#basically mapping is use to reduce the complexity
'''def multiple(a):
    b=a*2
    return b
l=[1,2,3,4]
a1=map(multiple,l)
print(list(a1))

# output
[2, 4, 6, 8]

'''


'''
def sum(a):
    b=a+10
    return b
l=[1,2,3,4]
c=map(sum,l)
print(list(c))
#output
[11, 12, 13, 14]
'''
'''
from functools import reduce
l=[2,4,6,8]
product=reduce(lambda x,y:x*y,l)
print(product)
#output
384
'''

'''
def even(a):
    b=a%2==0
    return b
l=[1,2,3,4,5,6,7,8]
c=filter(even,l)
print(list(c))
#output
[2, 4, 6, 8]
'''


# Use filter to get all positive numbers from [-5, 3, -2, 9, 0, -1].

# Use filter to get all strings longer than 3 characters from ['hi', 'hello', 'cat', 'python'].

# Use filter to get all numbers divisible by 3 from [3, 7, 9, 10, 12, 14].

# Use map to add 5 to each number in [10, 20, 30, 40].

# Use map to get the length of each string in ['hi', 'hello', 'python'].

# Use map to square each number in [2, 4, 6, 8].

# Use reduce to find the product of [1, 2, 3, 4].

# Use reduce to find the maximum number in [5, 12, 7, 18, 3].

# Use reduce to concatenate all strings in ['Hi', ' ', 'there', '!'].

# Use reduce to find the factorial of 5 using [1, 2, 3, 4, 5].


'''
def positive(n):
    a=n>=0
    return a

l=[-5, 3, -2, 9, 0, -1]
b=filter(positive,l)
print(list(b))    '''

def string():
    n=input()
    a=n>3
    return a
l=['hi', 'hello', 'cat', 'python']
b=filter(string,l)
print(list(b))