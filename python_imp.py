#----------------------my projects---------------------------------
'''1.book market website:
	this is a dynamic website which is based on the database CRUD operations.
	use: you can book a book or any stationary products from local book stores.
		you can compare the prices from different stores. if the products you want is not available,then you can request in request box. this box is seen to the customers and sellers.
		sellers are also replies on that request.
		login is requred for book any book.
		seller is registered and varified by admin.
		SDLC = spiral model(best for risk analysis and prototype based development)
		database = sqlite3
		framework = django
		technologies = python, js, css, html5, Bootstrap, templates
'''

# what is python language ?
'''--> python is general purpose, interpreted, scripting, object oriented, high level programming language.'''

# why you choose python language ?
'''--> if you are begginer, then python is a right choice. python language is easy to code and understand. It is dynamically typed. so you do not need to give the type of variables. the bulk of libraries are made python more powerful and fully featured language that is used in almost all Major filds like sofwere development, machine learning, artificial intelligence,Data science, big data, web scraping, web development, IOT, etc. so that's why i choose python .'''

'''
python vs java

1. python is interpreted language and java is compiled language.
means the python interpreter interpretes the code line by line and execute line by line.
and java compiler compiles the whole block of code and then executes the code.

2. python is dynamically typed language. java is statically typed language.

3. java is used for large scale sofwere development, web application development, android development. where the python is used in machine learning, data science, big data, web scraping,
artificial intelligence, etc.

4.
'''
# What are the key features of Python?
'''1.Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.
2.Python is dynamically typed, this means that you don’t need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without error
3.Python is well suited to object orientated programming in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++’s public, private).
4.In Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects
5.Writing Python code is quick but running it is often slower than compiled languages. Fortunately，Python allows the inclusion of C-based extensions so bottlenecks can be optimized away and often are. The numpy package is a good example of this, it’s really quite quick because a lot of the number-crunching it does isn’t actually done by Python
6.Python finds use in many spheres – web applications, automation, scientific modeling, big data applications and many more. It’s also often used as “glue” code to get other languages and components to play nice.
'''

#How is memory managed in Python?
'''Ans: Memory is managed in Python in the following ways:

Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
The allocation of heap space for Python objects is done by Python’s memory manager. The core API gives access to some tools for the programmer to code.
Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.
'''

#what is namespace in python?
'''A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries.
Examples of namespaces are: the set of built-in names,the global names in a module; and the local names in a function invocation.
In a sense the set of attributes of an object also form a namespace. The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; 
for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.for example, in the expression z.real, real is an attribute of the object z. 
Strictly speaking, references to names in modules are attribute references: in the expression modname.funcname, modname is a module object and funcname is an attribute of it.
'''

#what are generators in python?
'''Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). An example shows that generators can be trivially easy to create:

#generator example
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
	print(char)

#output
f
l
o
g
'''
#What are the decorators in python?
'''Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.

In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
Syntax for Decorator:
@gfg_decorator
def hello_decorator(): 
	print("Gfg") 
Above code is equivalent to - 

def hello_decorator(): 
	print("Gfg") 
	
hello_decorator = gfg_decorator(hello_decorator)


Decorator can modify the behavior:

# defining a decorator 
def hello_decorator(func): 

	# inner1 is a Wrapper function in 
	# which the argument is called 
	
	# inner function can access the outer local 
	# functions like in this case "func" 
	def inner1(): 
		print("Hello, this is before function execution") 

		# calling the actual function now 
		# inside the wrapper function. 
		func() 

		print("This is after function execution") 
		
	return inner1 


# defining a function, to be called inside wrapper 
def function_to_be_used(): 
	print("This is inside the function !!") 


# passing 'function_to_be_used' inside the 
# decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 


# calling the function 
function_to_be_used() 

Output:

Hello, this is before function execution
This is inside the function !!
This is after function execution
'''

#Deep copy and Shallow copy in python
'''#Deepcopy:
Deep copy is a process in which the copying process occurs recursively. It means first constructing a new collection object and then recursively populating it with copies of the child objects found in the original. 
In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object. In python, this is implemented using “deepcopy()” function.


#shallow copy:
A shallow copy means constructing a new collection object and then populating it with references to the child objects found in the original. The copying process does not recurse and therefore won’t create copies of the child objects themselves. 
In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object. In python, this is implemented using “copy()” function.
'''

#The self and __init__ method in python
'''
#The self
Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it.
If we have a method that takes no arguments, then we still have to have one argument.
This is similar to this pointer in C++ and this reference in Java.
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.
 

__init__ method
The __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
'''


#Constructor in Python
'''Constructors are generally used for instantiating an object.The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.In Python the __init__() method is called the constructor and is always called when an object is created.

Syntax of constructor declaration :

def __init__(self):
    # body of the constructor
Types of constructors :

default constructor : The default constructor is simple constructor which doesn’t accept any arguments.It’s definition has only one argument which is a reference to the instance being constructed.
parameterized constructor : constructor with parameters is known as parameterized constructor.The parameterized constructor take its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.


# Mangling and how it works in python
The technique of making a variable or method private is called 'data mangling'.

In Python, there is something called name mangling, which means that there is a limited support for a valid use-case for class-private members basically to avoid name clashes of names with names defined by subclasses. Any identifier of the form __geek (at least two leading underscores or at most one trailing underscore) is replaced with _classname__geek, where classname is the current class name with a leading underscore(s) stripped. As long as it occurs within the definition of the class, this mangling is done. This is helpful for letting subclasses override methods without breaking intraclass method calls. 
Let’s look at this example and try to find out how this underscore works: 
'''
'''
#magic methods in python
There’s another case of double leading and trailing underscores. We follow this while using special variables or methods (called “magic method”) such as__len__, __init__. These methods provide special syntactic features to the names. For example, __file__ indicates the location of the Python file, __eq__ is executed when a == b expression is executed. 



#-----------------------string methods------------------------------

Method	Description
capitalize()	Converts the first character to upper case
casefold()		Converts string into lower case
center()		Returns a centered string
count()			Returns the number of times a specified value occurs in a string
encode()		Returns an encoded version of the string
endswith()		Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()			Searches the string for a specified value and returns the position of where it was 				found
format()		Formats specified values in a string
format_map()	Formats specified values in a string
index()			Searches the string for a specified value and returns the position of where it was 				found
isalnum()		Returns True if all characters in the string are alphanumeric
isalpha()		Returns True if all characters in the string are in the alphabet
isdecimal()		Returns True if all characters in the string are decimals
isdigit()		Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()		Returns True if all characters in the string are lower case
isnumeric()		Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()		Returns True if all characters in the string are whitespaces
istitle()		Returns True if the string follows the rules of a title
isupper()		Returns True if all characters in the string are upper case
join()			Joins the elements of an iterable to the end of the string
ljust()			Returns a left justified version of the string
lower()			Converts a string into lower case
lstrip()		Returns a left trim version of the string
maketrans()		Returns a translation table to be used in translations
partition()		Returns a tuple where the string is parted into three parts
replace()		Returns a string where a specified value is replaced with a specified value
rfind()			Searches the string for a specified value and returns the last position of where it 			was found
rindex()		Searches the string for a specified value and returns the last position of where it 			was found
rjust()			Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()		Splits the string at the specified separator, and returns a list
rstrip()		Returns a right trim version of the string
split()			Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()			Returns a trimmed version of the string
swapcase()		Swaps cases, lower case becomes upper case and vice versa
title()			Converts the first character of each word to upper case
translate()		Returns a translated string
upper()			Converts a string into upper case
zfill()			Fills the string with a specified number of 0 values at the beginning

#------------------------ list methods-------------------------------
#how the list is stored in memory
#list memory management
#The list object consists of two internal parts; one object header, and one separately allocated array of object references. The latter is reallocated as necessary.the empty list takes 72bytes.an empty string takes 37 bytes.
#empty tuple takes 56 bytes. 
#the empty list takes 72bytes.


#list1=['a','b','c','d','e']
#print(list1[4]) # returns value at index '4' of list1
#print(list1[2:4]) #returns list with values of index range of 2 to 4(exclude).
#print(list1[2:]) # returns list with values of index start from 2 to end.
#print(list1[:4]) # returns list with values of index start from 0 to 4.
#print(list1[::-1]) # returns reverse list of list1.  
#print(list1[1:4:2]) # returns list with values of index 1,3.
'''
'''
append()	Adds an element at the end of the list
clear() 	Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list(changes the main list)
reversed()  returns a reversed iterator object(don't change the main list).
sort()	    Sorts the list(changes main list)
sorted()	create a new list containing a sorted version of the list.(don't changes main list)
'''

#add values in list
'''
list1.append('f') #adds given value at the end of list

print(list1)
list1.insert(4,'g') # adds given value at given index
print(list1)
list1[4]='i' #update the value at given index. 
print(list1)
'''

#------------------- list Based logical Programs--------------------
# 1. make the list with the elements stress,supress,compress and the output will be:s,s,c


# 2. string 'hello world'. and output will be the max count of char. o/p: l is max no of occrence char in string
''' 
s='hello world'
l=[]
print(l.index(max(l))

for i in range(len(s)):
    count1=s.count(s[i])
    l.append(count1)
print(l)
    
j=l.index(max(l))
print('max count of {} is {}'.format(s[j],j))

'''
 
# 3. L1 = [10,20,30,40,50] o/p : [10,30,60,100,150]
'''
L1 = [10,20,30,40,50]
l2 = []
sum = 0
for i in L1:
    sum=sum+i
    l2.append(sum)
print(l2)
'''
#------------------------tuple methods--------------------------------
#how tuple is stored in memory?
#-->tuple is stored as a contiguous block of memory.whole tuple is stored in one memory block.
#while we access the tuple object, it returns the reference object of that block of memory. 

'''
len() returns the length of any iterable object(string,list,tuple,set,dict)
copy() makes the new iterable object with as copy of any iterable obj(list,tuple,set,dict).
tuple() makes any iterable object as tuple
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''

#------------------------ Dictionary Methods---------------------------
# dictionary memory management
# Python dictionaries are stored as a contiguous block of memory. That means each array cell would start at dict_start + array_cell_index * cell_size. First, then, we need to decide which index value to look up.


#alpha = {'a':'apple', 'b':'ball', 'c':'cat', 'd':'dog'}
#print(alpha['a'])

 #Update value
#alpha['b']='bat' #change value of key 'b'
#print(alpha)

#alpha['e']='eyes' #change value of key 'e' if not available key then add key-value pair
#print(alpha)

 #remove items
#alpha.pop('e')  # remove key-value pair of given key 'e' 
#print(alpha)

#alpha.popitem() # remove key-value pair at the end of dict
#print(alpha)

#print(alpha.keys()) # returns list of all keys of alpha dict
#print(alpha.values()) # returns list of all values of alpha dict
#print(alpha.items())  # returns a new object of the dict items in (key,value) format.
#print(alpha.setdefault('g',default)) # returns value of key 'g'. if key not found returns 'default' if default not given returns 'none'.
#print(alpha.get('c')) # returns value of key 'c'. if key not found gives error.

#alpha1={'e':'eyes','f':'fish'}
#alpha.update(alpha1) # add another dict at the end of current dict
#print(alpha) 



#a=alpha.copy() # makes copy of dict alpha 
#print(a)

#print(dict(alpha)) # make dictionary of any sequetial data

#alpha.clear()   # remove all elements of dict but empty dict stay there 
#print(alpha)

#del alpha       # delete the dictionary with all elements

#key=[1,2,3,4,5]
#values='number'
#d=dict.fromkeys(key(seq),value) # dict.fromkeys returns new dictionaries with given sequences as key and other as values
#print(d)

#-------------------set methods-----------------------------
'''
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns 'true' if two sets have a intersection or else 'false'
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an random element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets(a union b - a intersection b)
symmetric_difference_update()	inserts the symmetric differences from this set and another(a union b - a intersection b)
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
set() make any iterable as set
'''


# armstrong number
'''n=int(input("enter number: "))
t=n
a=0
while(n>0):
    m=n%10
    a=a+m**3
    n=n//10
if t==a:
    print(t," is armstrong number")
else:
    print(t, " is not armstrong number")
'''

# fibonacci series
'''
n=int(input("enter length of series you want: "))
a,b=0,1
for i in range(n):
    a,b=b,a+b
    print(a,end=" ")
'''

# prime number
'''
n=int(input("enter number: "))
a=0
for i in range(1,n+1):
    if n%i==0:
        a+=1
if a<=2:
    print(n," is prime number")
else:
    print(n," is not prime number")
'''

# palindrom string
'''
s=input("enter string: ")
if s==s[::-1]: print(s," is palindrome")
else: print(s," is not palindrome")
'''

# patterns using for loop:
'''
for i in range(4):
    for j in range(4):
        print('*',end=' ')
    print()
'''
#output :
'''
 * * * *
 * * * *
 * * * *
 * * * *
 '''
'''
for i in range(4):
    for j in range(4):
        print(i,end=' ')
    print()
'''
#output
'''
0 0 0 0
1 1 1 1
2 2 2 2
3 3 3 3  
'''
'''
for i in range(4):
    for j in range(4):
        print(j,end=' ')
    print()
'''
#output
'''
0 1 2 3
0 1 2 3
0 1 2 3
0 1 2 3
'''
'''
for i in range(4):
    for j in range(4):
        print(chr(65+i),end=' ')
    print()
'''
#output
'''
A A A A
B B B B
C C C C
D D D D
'''
'''
for i in range(4):
    for j in range(4):
        print(chr(65+j),end=' ')
    print()
'''
#output    
'''
A B C D
A B C D
A B C D
A B C D
'''
'''
for i in range(4,0,-1):
    for j in range(4,0,-1):
        print(i,end=' ')
    print()
'''    
#output
'''
4 4 4 4
3 3 3 3
2 2 2 2
1 1 1 1
'''
'''
for i in range(4,0,-1):
    for j in range(4,0,-1):
        print(j,end=' ')
    print()
'''
#output
'''
4 3 2 1
4 3 2 1
4 3 2 1
4 3 2 1
'''
'''
for i in range(4,0,-1):
    for j in range(4,0,-1):
        print(chr(64+j),end=' ')
    print()
'''
#output
'''    
D C B A
D C B A
D C B A
D C B A
'''
'''
for i in range(4,0,-1):
    for j in range(4,0,-1):
        print(chr(64+i),end=' ')
    print()
'''
#output
'''
D D D D
C C C C
B B B B
A A A A
'''
'''
for i in range(5):
    for j in range(i):
        print(i,end=' ')
    print()
'''    
#output
'''
1
2 2
3 3 3
4 4 4 4
'''
'''
for i in range(5):
    for j in range(i):
        print(j+1,end=' ')
    print()
'''
#output
'''
1
1 2
1 2 3
1 2 3 4
'''
'''
for i in range(4,0,-1):
    for j in range(i):
        print(j+1,end=' ')
    print()
'''
#output
'''
1 2 3 4
1 2 3
1 2
1
'''
'''
for i in range(4,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()
'''
#Output
'''
4 4 4 4
3 3 3
2 2
1
'''
'''
for i in range(4,0,-1):
    for j in range(i):
        print(chr(64+i),end=' ')
    print()
'''
#output
'''
D D D D
C C C
B B
A
'''
'''
for i in range(4,0,-1):
    for j in range(i):
        print(chr(65+j),end=' ')
    print()
'''
#output
'''
A B C D
A B C
A B
A
'''
'''
for i in range(1,5):
    for j in range(4,i,-1):
        print(' ',end=' ')
    for j in range(i):
        print(j+1,end=' ')
    print()
'''
#output
'''
      1
    1 2
  1 2 3
1 2 3 4
'''
'''
for i in range(4,0,-1):
    for j in range(i,5):
        print(' ',end=' ')
    for j in range(0,i):
        print(j+1,end=' ')
    print()
'''
#output
'''
1 2 3 4
  1 2 3
    1 2
      1
'''
'''
for i in range(1,8,2):
    for j in range(6,i,-2):
        print(' ',end=' ')
    for j in range(0,i):
        print('*',end=' ')
    print()
'''
#output
'''    
      *
    * * *
  * * * * *
* * * * * * *
'''
'''
for i in range(7,0,-2):
    for j in range(6,i,-2):
        print(' ',end=' ')
    for j in range(0,i):
        print('*',end=' ')
    print()
'''
#output
'''
* * * * * * *
  * * * * *
    * * *
      *
'''
'''
for i in range(3,-4,-1):
    for j in range(0,abs(i)):
        print(' ',end='')
    for j in range(5,abs(i)+1,-1):
        print('* ',end='')
    print()
'''
#output
'''
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
'''

# Greatest Common Divisor
'''
n1=int(input("enter 1st number:"))
n2=int(input("enter 2nd number:"))
d1=[]
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        d1.append(i)
print("n1: {}, n2: {}, GCD: {}".format(n1,n2,max(d1)))
'''

#least common multiplier
'''
n1=int(input("enter 1st number:"))
n2=int(input("enter 2nd number:"))

for i in range(1,(n1*n2)+1):
    m1=n1*i
    for j in range(1,(n1*n2)+1):
        m2=n2*j
        if m1==m2:
            print("\n n1:{},n2:{}, LCM:{}".format(n1,n2,m1))
            exit()
'''                 
#prime Number
'''
n=int(input("enter number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c<=2:
    print(n,"is prime.")
else:
    print(n,"is not prime.") 
'''

#fibbo2
'''
a,b=0,1
n = int(input('enter lenght Of series: '))
for i in range(n):
	print(a,end=' ')
	a,b = b,a+b
'''


#-----------------------------------pymysql-----------------------------------------    

#-----------------------MySQL queries---------------------------------

#create database


#use database


#Interview Questions for Python: (Practical round)
'''
1)	Create database name emplyee in that create table name emplyee_details add field (email,password,phone,city,address) insert ,update , delete data in it.(using pymysql module)

---> What is PyMySQL ?
PyMySQL is an interface for connecting to a MySQL database server from Python program. 
It implements the Python Database API v2.0 and contains a pure-Python MySQL client library. The goal of PyMySQL is to be a drop-in replacement for MySQLdb.
'''
'''
import pymysql
def createConn():
    return pymysql.connect(host='localhost', database='emp', user='root', password='', port=3306)

def CreateTable():
    conn=createConn()
    cursor=conn.cursor()
    cursor.execute('create table emptable(name varchar(50), address varchar(50), city varchar(50))')
    conn.commit()
    print('table created')
    conn.close()

def insertdata(name,address,city):
    conn=createConn()
    cursor=conn.cursor()
    args = (name,address,city)
    query = ('insert into emptable(name,address,city)values(%s,%s,%s)')
    cursor.execute(query,args)
    conn.commit()
    print("data inserted")
    conn.close()

def getall():
    conn = createConn()
    cursor = conn.cursor()
    cursor.execute('select * from emptable')
    res= cursor.fetchall()
    for i in res:
        print(i)

def UpdateData(address,city,name):
    conn = createConn()
    cursor= conn.cursor()
    args = (address,city,name)
    query = ('update emptable set address=%s,city=%s where name=%s')
    cursor.execute(query,args)
    conn.commit()
    print("data updated")
    conn.close()

def deletedata(name):
    conn = createConn()
    cursor = conn.cursor()
    args = (name)
    query = 'delete from emptable where name=%s'
    cursor.execute(query,name)
    conn.commit()
    print("data deleted")
    conn.close()


#deletedata('kartavya')
#insertdata('ajay','limdi','dahod')
getall()
deletedata('ajay')
'''

'''
2. 2) create calculator (use function for it)-user have to enter numbers

3. 3) Give factorial number (user have to enter numbers)

-->#---------------------------------factorial-------------------------------------
# Python program to find the factorial of a number provided by the user.

# change the value for a different result

num = int(input("enter number: "))

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)




4. create list ,tuple,set,dictory – insert data in all collections – delete data in all collections – update data in all collections – find unique number from list
'''
#unique num from list
'''
l=[1,2,2,3,1,1]
for i in l:
    if l.count(i)==1:
        print("{} is unique".format(i))
'''
'''
5. read and write file operations
 -->
 
 #file write
with open('testfile.txt','a+') as f:
    f.write('this is test file\n that is made by me ')
    print(f.read())
    f.close()

6. given link of web page and have to give specified data from that web page ( web scarping ) using scrapy module of python

Technical Round Questions:
1. explain project: my project name is book market. it is basically a website that is made using django. the main use of this website is that you can book the book from local stores which are registered in this website. 1st you have to register then you can login. three different types of login: admin,seller,customer. seller is varified by admin. compare prices from different shops for same product. 

2. what is python
-->Python is general purpose, interpreted, scripting, and high level programming language based on oops.
    Scripting language : A scripting or script language is a programming language for a special 
                        run-time environment that automates the execution of tasks.
                         the tasks could alternatively be executed one-by-one by a human operator. 
                        Scripting languages are often interpreted, rather than compiled.

    Scripting language vs programming language :
    -->The primary difference between a scripting language and a programming language is in their execution – programming languages use a compiler to convert the high-level programming languages into machine language, on the other hand, scripting languages use an interpreter.

3. what is django
-->Django is a Python-based free and open-source web framework that follows the model-template-views (MTV) architectural pattern

4. what is javascript
-->JavaScript is a lightweight, interpreted programming language. It is designed for creating network-centric applications.

5.what is css
-->Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML.CSS describes how HTML elements are to be displayed on screen, paper, or in other media.

All CSS Simple Selectors
Selector	      	Example	           		Example description
#id	              #firstname	           Selects the element with id="firstname"
.class	          .intro	               Selects all elements with class="intro"
element.class	  p.intro                  Selects only <p> elements with class="intro"
*	              *	                       Selects all elements
element			  p					       Selects all <p> elements
element,element..  div, p	               Selects all <div> elements and all <p> elements


6. what is html
-->Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser.

7.what is Bootstrap?
-->Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and (optionally) JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.

7. how to get data from database
8. what is template
9. how to get css file in html
10. oops concepts
11. default data base (list , tuple , set , dictionary)

1) find length of list element
2) different between list and tuple
3) find length of list element using map function
4) reverse string
5) what is web scraping
6) MYSQL query
7) numpy and pandas

-->pandas: Pandas is defined as an open-source library that provides high-performance data manipulation in Python. It is built on top of the NumPy package, which means Numpy is required for operating the Pandas. 

    numpy: NumPy is mostly written in C language, and it is an extension module of Python. It is defined as a Python package used for performing the various numerical computations and processing of the multidimensional and single-dimensional array elements. The calculations using Numpy arrays are faster than the normal Python array.


8) what is web crawling
-->Basically, web crawling creates a copy of what's there
 web scraping extracts specific data for analysis, or to create something new.

9) what is ORM
-->Object-relational mapping is a programming technique for converting data between incompatible type systems using object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language.
'''



###----------------------------------------------DJANGO--------------------------------------------###
'''
#Explain Django.
--> Django is a free and open source web application framework, written in Python. It is a server-side web framework that provides rapid development of secure and maintainable websites.

#Explain Django architecture.
Django follows MVT (Model View Template) pattern. It is slightly different from MVC.

Model: It is the data access layer. It contains everything about the data, i.e., how to access it, how to validate it, its behaviors and the relationships between the data.

View: It is the business logic layer. This layer contains the logic that accesses the model and defers to the appropriate template. It is like a bridge between the model and the template.

Template: It is a presentation layer. This layer contains presentation-related decisions, i.e., how something should be displayed on a Web page or other type of document.To configure the template system, we have to provide some entries in settings.py file.

#How does Django work?
--> Django can be broken into many components:

Models.py file: This file defines your data model by extending your single line of code into full database tables and add a pre-built administration section to manage content.

Urls.py file: It uses a regular expression to capture URL patterns for processing.

Views.py file: It is the main part of Django. The actual processing happens in view.

When a visitor lands on Django page, first Django checks the URLs pattern you have created and used the information to retrieve the view. After that view processes the request, querying your database if necessary, and passes the requested information to a template.

After that, the template renders the data in a layout you have created and displayed the page.

# What are the features available in Django web framework?
Features available in Django web framework are:

Admin Interface (CRUD)
Templating
Form handling
Internationalization
A Session, user management, role-based permissions
Object-relational mapping (ORM)
Testing Framework
Fantastic Documentation

11) Explain the advantages of Django?
Advantages of Django:

Django is a Python's framework which is easy to learn.
It is clear and readable.
It is versatile.
It is fast to write.
No loopholes in design.
It is secure.
It is scalable.
It is versatile.

19) What are the signals in Django?
Signals are pieces of code which contain information about what is happening. A dispatcher is used to sending the signals and listen for those signals.
Two important parameters in signals are:
Receiver: It specifies the callback function which connected to the signal.
Sender: It specifies a particular sender from where a signal is received.

24) What is Django Session?
A session is a mechanism to store information on the server side during the interaction with the web application. By default, session stores in the database and also allows file-based and cache based sessions.

25) What is the role of Cookie in Django?
A cookie is a small piece of information which is stored in the client browser. It is used to store user's data in a file permanently (or for the specified time). Cookie has its expiry date and time and removes automatically when gets expire. Django provides built-in methods to set and fetch cookie.

The set_cookie() method is used to set a cookie and get() method is used to get the cookie.

The request.COOKIES['key'] array can also be used to get cookie values.
'''


'''

#----------------------OOPS Concepts in python-----------------------------
#Encapsulation
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variable. 
A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.


#protected & private members in class

Protected members are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.

Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class. However, to define a private member prefix the member name with double underscore “__”.
 
Note: Python’s private and protected member can be accessed outside the class through python name mangling.


#Polymorphism
Polymorphism : The word polymorphism means having many forms. In programming, polymorphism means same function name (but different signatures) being uses for different types.

Polymorphism with Inheritance:
In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.

Data Abstraction :
Abstraction means hiding the complexities of coding, programming, internal details, hide the real implementations, only shows the essential functionalities and features of object to the normal user. Abstraction is achieved  by using abstract classes & interfaces.

Abstract Classes in Python :
A class which contains one or more abstract methods is called an abstract class.
 An abstract method is a method that has a declaration but does not have an implementation.
An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class.  An abstract method is a method that has a declaration but does not have an implementation. While we are designing large functional units we use an abstract class. When we want to provide a common interface for different implementations of a component, we use an abstract class.
 
Why use Abstract Base Classes :
By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. This capability is especially useful in situations where a third-party is going to provide implementations, such as with plugins, but can also help you when working in a large team or with a large code-base where keeping all classes in your mind is difficult or not possible.
'''

#extra programs

#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
l1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
def sort1(i):
    return i[1]

l1.sort(key=sort1)
print(l1)
'''

#remove duplicates from list using for loop
'''
l1=[1,1,2,3,4,5,5,6,4]
count=0
for i in l1:
    for j in l1:
        if i==j:
            count+=1
            if count>=2:
                l1.remove(i)
                count=0
print(l1)
'''

#difference between two lists using loops
'''
l1=[1,2,3,4,5]
l2=[4,5,6,7]
# for i in l1:
#     for j in l2:
#         if i==j:
#             l1.remove(i)
#             l2.remove(j)
print(list((set(l1).union(l2)).difference(set(l1).intersection(l2))))            
# l1.extend(l2)
'''

#find the index of element in list:

l1=[1,"element2","element1","ele3"]
print(str(l1).find("element1"))
 
