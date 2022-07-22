# standard i/o,comment,variable

print('Hello World')

# comment

"""
comment
"""

name = 'kan'
age = 18
# format
print('my name is = {}, age {}' .format(name, age))
a = b = 20
print(a, b)

LEGAL_AGE = 20

if age > LEGAL_AGE:
    print("adult")
else:
    print("children")

# format py3.6
print(f'age = {age}')
# format py3.8
print(f'{age=}')

# list
array = [1,2,3,4,5]
print(array)

# list slice
list = [1,2,3,4,5]
list_1 = list[1:2]
print(list_1)

# dictionary
car = {'brand': 'toyota'}
print(car['brand']) # show error
print(car.get("brand")) # don`t` show error
print(car.items()) # key + value
for k, v in car.items():
    print('key = {}, value = {}' .format(k, v))
if 'brand' in car:
    print('{}' .format(car['brand']))


# tuple = immutable
tuple = ('a', 'b', 'c')
print(tuple)

# set = unique key
set_a = {'a', 'b', 'c', 12}
print(set_a)
print('a' in set_a)

s = {'a', 'b', 'c'}
t = {'c', 'd', 'e'}

# s.union(t) - +
u = s | t
print(u)

# s.intersection(t) - the two
u = s & t
print(u)

# s.difference(t) - s and not t
u = s - t
print(u)

# s.symmetric_difference(t) - not s,t duplicate
u = s ^ t
print(u)

# if - False = None,0,false,"",empty list,empty tuple,empty set
var = ''
print('bool result: {}' .format(bool(var)))
if var:
    print('if statement')

# function
def print_hello():
    print('Hello')

def sample(arg1, arg2=100):
    print(arg1, arg2)
sample(200, 300)

def spam(arg1, *arg2): # tuple
    print(f'{arg1=}{arg2=}')
spam(1,2,3,4)

def spam2(arg1, **arg2): # dictionary
    print(f'{arg1=}{arg2=}')
spam2(1, age=2, count=3)

# global variable
global ANIMAL
ANIMAL = 'dog'

# inner function
def outer():
    def inner():
        print('inner function')
    inner()
outer()


# lambda
add_f = lambda x=1, y=1: x + y
print(add_f())
print(add_f(2,2))
