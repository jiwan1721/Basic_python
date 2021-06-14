
if 5 > 2:
	print("Five is greater than two")
	if 2 < 5:
		print("two is less than five")


x = 5
y = "hello, world"
print(x)
print(y)
#this is not easy.
x = 4 # x is type of int.
x = "sally" # x is now type of string.
print(x)

a = str(3)      # a will be in '3'
b = int(3)      # b will be 3
c = float(3)    # c will be 3.0

print(a)
print(b)
print(c)
x = 5
y = "john"
print(type(x))
print(type(y))

m = 3
M = 'jiwan'
print(m)
print(M)

#legal variable names.
myvar = "jiwan"
my_var = "jiwan"
_my_var = "jiwan"
myVar = "jiwan"
MYVAR = "jiwan"
myvar2 = "jiwan"
_myvar = "jiwan chand"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print(_myvar) 


#Multi words variable names.
#Camel case.
myVariableName = "sanchaii"
print(myVariableName)

#Pascal case.
MyVariableName = "hero horw"
print(MyVariableName)

#snake case.
my_Var_name = "hello"
print(my_Var_name)

#many values to multiple variables.
X, Y, Z = "orange", "Banana", "cherry"
print(X)
print(Y)
print(Z)

#One value to multiple variables.
A = B = C = "mero mutu"
print(A)
print(B)
print(C)

#unpack a collection.
fruits = ["water", "milk", "iceream"]
K, J, L = fruits
print(J)
print(K)
print(L)

#Output Variables.
S = "awsome"
s = " and wow "
print("Python is " + S + s)
D = S + s
print(D)
#new value.
s = 3
S = 5
D = s + S
print(D)

#Global Variables.
x = "fantastic"

def myfunc():
	print("python is " + x)

myfunc()

#new variable again
x = "wow"
def myfunc():
	x = "good"
	print("python is " + x)
myfunc()

print("python is " + x)

#The global keyword
def myfunc():
	global x
	x = "babal"
myfunc()
print("python is " + x)

#To change the global value
x = "awsome"
def myfunc():
	global x
	x ="fantastic"
myfunc()

#python data types
x = 50
print(type(x))
#You can get the data type of any object by using the type() function.
a = ["apple", "mango", "banana"]   #list
b = {"apple", "mango", "banana"}   #set
c = ("apple", "mango", "banana")   #touple
d = {"name" : "jiwan", "age" : 36} #dict
e = "true"                         #bool
f = b"hello"
print(a)                       #byte
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))

x = float(20.5)
print(x)
print(type(x))

c = complex(1j)
print(c)
print(type(c))

d = dict(name="jiwan", age=36)
print(d)
print(type(d))

#Python Numbers
#INT
x = 1
y = 35565477675568556
z = -3456765758
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#FLOAT
x = 1.10
y = 1.0
z = -334.345
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#using scientific numbers
x = 35e6
y = 32E5
z = -76.7e100
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#COMPLEX
x = 3+5j
y = 5j
z = -4j
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))


#Type Conversion
#convert from one type to another
x = 12
y = 23.456
z = 7j
a = float(x)
b = int(y)
c = complex(7j)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#Random Number
import random
print(random.randrange(1, 11))

#string
#Assign String to a variable
a = "hellooooo"
print(a)

#Musltiline string
#Three double quotes
a = """my name is jiwan,
and i'm not a terriorist."""
print(a) 

#Three single quotes
a = '''who is your dady,
dady swami G.'''
print(a)
print(type(a))

#String are arrays.
a = "hello, world, k xa "
print(a[1])
print(a[9])

#Looping through a string.
for x in "jiwanchand":
 print(x)

#string length.
a = "hello, k xa"
print(len(a))

#Check String.
txt = "the best thing in life are free"
print("free" in txt)
print("wow" in txt)

#Check if
txt = "the best thing in life are free"
if "free" in txt:
 print("yes, 'free' is present.")

#check if not
txt = "the best thing in life are free"
print("expensive" not in txt)
if "expensive" not in txt:
	print("yes 'expensive' not in txt")

#Slicing Strings.
b = "jiwan , k xa"
print(b[1:9])

#Slice from the start.
b = "hello, world"
print(b[:10])
#Slice to the end
print(b[3:])
#Negative indexing.
print(b[-5:-2])

#Modify String.
#Upper case.
a = "Hello, World!"
print(a.upper())
#Lower case.
print(a.lower())

#remove whitespace.
a = " hello, world  "
print(a.strip())

#Replace String.
a = "Hello, World!"
b = (a.replace("H", "J"))
print(b.replace("o", "X"))

#Split String
a = "hello, world"
print(a.split(","))

#String Concatenation
a = "hello"
b = "world"
c = a + b
print(c)

a = "hello"
b = "world"
c = a + " " + b
print(c)

#FORMAT STRING
#string format
age = 36
txt = "my name is jiwan, i m {}"
print(txt.format(age))

quantity = 3
itemno = 675
price = 49.78
myorder = "i want {} pices of item {} for {} dollors."
print(myorder.format(quantity, itemno, price))

myorder = "i want to pay {2} dollors for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#Escape character
txt = "we are so-called \"Vikings\" from the north."
print(txt)

#String Method
txt = "jiwan"
x = txt.center(20)
print(x)

txt = "i love nepal, nepal is very beautiful country"
x = txt.count("nepal")
print(x)
y = txt.count("nepal", 10, 24)
print(y)
z = txt.encode()
print(z)
print(txt.encode(encoding="ascii",errors="backslashreplace"))

jiwan = "H\te\tl\tl\to"
print(jiwan.expandtabs(10))
a = txt.find("e")
print(a)
print(txt.find("q"))
print(txt.index("e"))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt2)

meat = "we have {:<8} chickens".format(49)
print(meat)

b = txt.partition("nepal")
print(b)

myTuple = ("jiwan", "ram", "hari")
x = "#".join(myTuple)
print(x)
y = "*".join(myTuple)
print(y)

#Python BOOLEANS.
#Boolean values
print(10>9)
print(10==9)
print(10<9)

a = 244
b = 66
if b > a :
	print("b is greater than a")
else :
	print("b is not greater than a")

#Evaluate Values and variables
print(bool("helo"))
print(bool(15))

#Evaluate tw variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#Most values are true.
print(bool("abc"))
print(bool(123))
print(bool(["apple", "banana", "mango"]))

#some values are false
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#__len__
class jiwan():
	def __len__(self):
		return 0
code = jiwan()
print(bool(code))

#Function can Return a boolean
def myfunction():
	return True
print(myfunction())	
if myfunction():
	print("YES!")
else:
	print("NO!")

x = 200
print(isinstance(x, int))

#PYTHON OPERATOR
#Arthmetic Operators
x = 10
y = 5
print(x % y)
print(x ** y)
print(x // y)


#Python Assignment Operators.
x = 5
x += 3
print(x)
x &= 3
print(x)

x = 8
x ^= 3
print(x)
x >>= 3
print(x)

x = 9
x <<= 3
print(x)


#Python comparioson Operators
x = 7
y = 17
print(x == y)
print(x != y)   #NOT equal
print(x > y)    #Greater than
print(x < y)
print(x >= y)   #Greater than equal to
print(x <= y)

#Python LOGICAL Operators
x = 4
print(x < 5 and x < 7)   #AND
print(x<5 and x<3)
print(x<5 or x<3)        #OR
print(x<2 or x<4)
print(not(x < 5 and x < 7)) #NOT(reverse the result)
print(not(x < 5 and x < 3))

#Python IDENTITY Operators
x = ["banana", "mango"]
y = ["banana", "mango"]
z = x
print(x is y)
print(x is z)
print(x == y)
print(x is not z)
print(x is not y)

#Python MEMBERSHIP operators
x = ["jiwan", "hari"]
print("jiwan" in x)
print("ram" not in x)

#Python LIST
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print(len(thislist)) #List length

#List items - Datattypes
list1 = ["apple", "banana", "mango"]
list2 = [1, 3, 7, 5, 4]
list3 = [True, False, False]
list4 = ["abc", 54, True, 30, "male"]
print(list1)
print(list2)
print(list3)
print(list4)
print(type(list4))

#the List() Constructor
jiwan = list(("apple", "banana", "cherry"))  #note the double round brackets.
print(jiwan)

#Access Items
jiwan = ["banana", "mango"]
print(jiwan[1])

#Negative Indexing
thislist = ["apple", "banana"]
print(thislist[-1])

#Range of Indexes.
thislist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(thislist[2:5])
print(thislist[:4])  #the range will start at the first item.
print(thislist[2:])  #the range will go on to the end of the list.


#range of negative indexes.
list1 = ["apple", "mango", "cherry", "orange", "kiwi", "melon", "mango"]
print(list1[-4:-2])
if "apple" in list1:
	print("yes, 'apple' is in the fruit list")

#CHANGE list item
thislist = ["banana", "apple", "mango"]
thislist[1] = "cherry"
print(thislist)

#change the RANGE of item values.
jiwan = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
jiwan[1:3] = ["blackcurrant", "watermelon"]
print(jiwan)

hera = ["apple", "banana", "cherry"]
hera[1:2] = ["blackcurrent", "watermelon"]
print(hera)
hera[1:3] = ["mango"]
print(hera)

#Insert Items.jiwan = ["appple", "banana", "cherrry"]
jiwan.insert(2, "watermelon")
print(jiwan)

#Add list items.
#Append Items.
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items.
jiwan = ["banana", "mango", "cherry"]
jiwan.insert(1, "orange")
print(jiwan)

#Extend List.
jiwan = ["apple", "banana", "cherry"]
chand = ["mango", "pineaple", "papaya"]
jiwan.extend(chand)
print(jiwan)

#Add Any Iterable.
thislist = ["apple", "banana", "cherry"]
thistuple = ("mango", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove List item.
#remove Specified Item.
jiwan = ["apple", "banana"]
jiwan.remove("banana")
print(jiwan)

#Remove specified Index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)

jiwan = ["apple", "banana", "cherry", "kiwi"]
del jiwan[0]  #Remove the first item.
print(jiwan) 
del jiwan   #delete the entire list.

#Clear the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#LOOP lists.
#Looop through a list.
jiwan = ["apple", "banana", "orange"]
for x in jiwan:
	print(x)

#Loop through the Index Numbers.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
	print(thislist[i])

#Using a WHILE loop.
thislist = ["mango", "kiwi", "watermelon"]
i = 0
while i < len(thislist):
	print(thislist[i])
	i = i + 1

#Looping using List comprehension.
thislist = ["jiwan", "chand", "thaluri"]
[print(x) for x in thislist]

#without List Comprehension.
fruits = ["apple", "banana", "cherry", "mango"]
newlist = []

for x in fruits:
	if "a" in x:
		newlist.append(x)

print(newlist)

#with list comprehension.
fruits = ["apple", "banana", "cherry", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Iterable
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x<5]
print(newlist)

#Expression.
fruits = ["apple", "banana", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#sort list
#sort list Alphanumerically.
thislist = ["apple", "mango", "banana", "orange"]
thislist.sort()
print(thislist)

#sort the list Numerically.
jiwan = [100, 34, 56,78]
jiwan.sort()
print(jiwan)

#sort decending.
thislist = ["orangr", "mango", "kiwi"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#customize sort function.
def myfunc(n):
	return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case insensitive sort:
thislist = ["banana", "Orange", "kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse Order:
thislist = ["banana", "Orange", "kiwi"]
thislist.reverse()
print(thislist)

#Copy Lists:
jiwan = ["apple", "banana", "cherry"]
mylist = jiwan.copy()
print(mylist)

thislist = ["banana", "mango", "apple"]
mylist = list(thislist)
print(mylist)

#Join Lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

for x in list2:
	list1.append(x)
print(list1)

list1 = ["a", "b", "c"]
list2 = list2.copy()
list1.extend(list2)
print(list1)

#Python Tuples:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#allow Duplicates:
thistuple = ("apple", "banana", "apple")
print(thistuple)

#Tuple Length:
jiwan = ("apple", "banana", "cherry")
print(len(jiwan))

#Create Tuple With One Item:
thistuple = ("apple",)
print(type(thistuple))

#The tuple() Constructor:
Jiwan = tuple(("appple", "banana"))
print(Jiwan)

#Access Tuple Items:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1]) #Negative Indexing.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi")
print(thistuple[:3])
print(thistuple[2:])

#Range of negative Indexes:
jiwan = ("apple", "banana", "cherry", "orange", "kiwi", "mango")
print(jiwan[-4:-2])
if "apple" in jiwan:
	print("yes, 'apple' in fruit tuple")

#Change Tuple Values:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Item:
a = ("apple", "banana", "cherry")
b = list(a)
b.append("kiwi")
a = tuple(b)
print(a)

#remove Items:
x = ("appple", "banana", "cherry")
y = list(x)
y.remove("cherry")

#Unpacking Items:
Fruits = ("apple", "banana", "cherry")
(green, yellow, red) = Fruits
print(green)
print(yellow)
print(red)

#Using ASTERIX*:
Fruits = ("apple", "banana", "cherry", "mango", "kiwi")
(green, yello, *red) = Fruits
print(green)
print(yellow)
print(red)

Fruits = ("apple", "banana", "cherry", "mango", "kiwi")
(green, *tropic, red) = Fruits
print(green)
print(tropic)
print(red)

#Loop Tuples:
jiwan = ("apple", "banana", "cherry")
for x in jiwan:
	print(x)

#LOOP Through index Number:
ajaydai = ("appple", "hero", "villain")
for i in range(len(ajaydai)):
	print(ajaydai[i])

#using while Loop:
khattra = ("ram", "hari", "syam")
i = 0
while i<len(khattra):
	print(khattra[i])
	i = i + 1

#Join Tuples:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply tuples:
fruits = ("appple", "mango", "kiwi")
rayzr = fruits * 2
print(rayzr)

#PYTHON SETS:
myset = {"apple", "banana", "cherry"}
print(myset)
hero = {"apple", "banana", "cherry", "apple"}
print(hero)
print(len(hero))
print(type(hero))

#Access Item:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
	print(x)

Jiwan = {"apple", "banana", "cherry"}
print("apple" in Jiwan)

#Add items:
jiwan = {"apple", "banana", "cherry"}
jiwan.add("orange")
print(jiwan)

#Addd sets:
ram = {"apple", "banana", "cherry"}
hari = {"orange", "mango", "cherry"}
ram.update(hari)
print(ram)

#Add any iterable:
meroset = {"apple", "banana", "cherry"}
merolist = ["kiwi", "orange"]
meroset.update(merolist)
print(meroset )

#Remove set items:
meroset = {"apple", "banana", "cherry"}
meroset.remove("banana")
print(meroset)
 
#removing cherry using discard() function:
meroset.discard("cherry")
print(meroset)

meroset = {"apple", "banana", "cherry"}
x = meroset.pop()
print(x)
print(meroset)

meroset = {"apple", "banana", "cherry"}
meroset.clear()
print(meroset)

#Loop Items:
meroset = {"apple", "banana", "cherry"}
for x in meroset:
	print(x)

#Join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "banana", "cherry"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#python_dictionary:
thisdict = {
	"Brand": "ford",
	"Model": "Mustang",
	"year": 1964,
	"year": 2029
}
print(thisdict)
print(thisdict["Brand"])
print(len(thisdict))

merodict = {
	"brand": "ford",
	"electric": False,
	"year": 1964,
	"colors": ["red", "white", "blue"]
}
print(merodict)
print(type(thisdict))

#Accessing Items:
merodict = {
	"brand": "ford",
	"Model": "Mustang",
	"year": 1964
}
x = merodict["Model"]
print(x)
y = merodict.get("Model")
print(y)
x = merodict.keys()
print(x)
merodict["color"] = "white"
print(x)
x = merodict.values()
print(x)
merodict["year"] = 2020
print(x)

car = {
	"brand": "ford",
	"model": "Mustang",
	"year": 1964
}
x = car.items()
print(x)
car["color"] = "red"
print(x)

if "model" in car:
	print("yes, 'model' is one of the keys in the thsdict dictionary")

#Chnage Values:
Merodict = {
	"brand": "Ford",
	"model": "Mustang",
	"year": 1783
}

Merodict["year"] = 1767
print(Merodict)

jiwan = {
	"brand" : "ford",
	"roll no" : "17",
	"year" : 1890

}
jiwan.update({"year": 2020})
print(jiwan)

#ADD items:
jiwan["color"] = "red"
print(jiwan)
jiwan.update({'prize': 18999})
print(jiwan)

#Removig Items
jiwan = {
	"brand" : "ford",
	"roll no" : "17",
	"year" : 1890

}
jiwan.update({"year": 2020})
print(jiwan)
jiwan["color"] = "red"
print(jiwan)
jiwan.update({'prize': 18999})
print(jiwan)
jiwan.pop("prize")
print(jiwan)
jiwan.popitem()
print(jiwan)
del jiwan["roll no"]
print(jiwan)
jiwan.clear()

#Loop Dictionary:
merodict = {
	"name": "jiwan",
	"surname": "chand",
	"rollno": 17
}
for x in merodict:
	print(x)
for x in merodict:
	print(merodict[x])
for x in merodict.values():
	print(x)
for x in merodict.keys():
	print(x)
for x, y in merodict.items():
	print(x, y)
#Copy dictonaries:
mydict = merodict.copy()
print(merodict)
jiwan = dict(mydict)

#Nested Dictionaries:
myfamily = {
	"bachha1" : {
	"name" : "hero",
	"year" : 3000
	},
	"child2" : {
	"name" : "gadha",
	"year" : 2003
	},
	"bachha3" : {
	"name" : "badar",
	"year" : 3002
	}
}
print(myfamily)

#PYTHON IF Else:
a = 33
b = 46
if b>a:
	print("b is greater than a")

#ELIF:
a = 44
b = 44
if b>a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")

#ELSE:
a = 300
b = 56
if b>a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else:
	print("a is greater than b")

#Short Hand IF:
a = 300
b = 40
if a>b: print("a is greater than b")

#Short hand if else:
a = 8
b = 500
print("A") if a > b else print("B")

a = 90
b = 80
print("A") if a>b else print("=") if a == b else print("B")

a = 200
b = 44
c = 799
if a>b and c>a:
	print("both condition are True")

a = 45
b = 67
c = 7
if a>c or a<b:
	print("atleat aauta tw thik xa")

x = 60
if x>40:
	print("40 vanda thulo")
	if x>50:
		print("50 vanda ni thulo xa")
	else:
		print("But not above 59")

a = 9
b = 8
if b>a:
	pass


#While Loop:
i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i<6:
	print(i)
	if (i == 3):
		break
	i += 1

k = 0
while k < 6:
	k += 1
	if k == 3:
		continue
	print(k)

i = 1
while i < 9:
	print(i)
	i += 1
else:
	print("i aba 9 vanda sano xaina")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
for x in "banana":
	print(x)

#the break statement:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		break

falful = ["mango", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		break
	print(x)

#the continue statement:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		continue
	print(x)

for x in range(6):
	print(x)

for x in range(2, 6):
	print(x)

#Else in for loop:
for x in range(6):
	print(x)
else:
	print("finally sakkyo")

for x in range(6):
	if x == 3: break
	print(x)
else:
	print("yo pani sakkyo")

#Nested Loops:
adj = ["red", "big", "tasty"]
fruits = ["apple", "mango", "angur"]

for x in adj:
	for y in fruits:
		print(x, y)

#the pass statement:
for x in [0, 1, 2]:
	pass

#creating function:
def my_myfunction():
	print("hello from the function")
my_myfunction()

#Arguments:
def my_function(fname):
	print(fname + " refsnes" + " haha")
my_function("emill")
my_function("tobias")
my_function("linus")

def my_function(nam, lname):
	print(nam + " " + lname)
my_function("emil", "refsens")

#Arbitrary Arguments:
def my_function(*kids):
	print("the youngest child is" + kids[2])

my_function("Emil", "Tobias", "Linus")

#Arbitaray keyword arguments, **kwargs:
def my_function(**kid):
	print("his last name is " + kid["lname"])

my_function(fname = "tobias", lname = "refsens")

#Default parameter value:
def my_function(country = "Norway"):
	print("i am from " + country)

my_function("sweden")
my_function("Nepal")
my_function()
my_function("brazil")

#passing a list as an argument:
def my_function(food):
	for x in food:
		print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return values:
def my_function(x):
	return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Recursion:
def tri_recursion(k):
	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result
print("\n\nRecursion example results")
tri_recursion(6)

#Lambda:
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(7, 6))

x = lambda a, b, c : a + b + c
print(x(4, 6, 7))

def myfunc(n):
	return lambda a : a * n
mydoubler = myfunc(3)
print(mydoubler(11))

def func(n):
	return lambda a : a * n

dob = func(2)
tri = func(3)

print(dob(11))
print(tri(11))

array = ["ford", "volvo", "BMW"]
print(array)
x = array[0]
print(x)

car = ["ford", "volvo", "BMW"]
car[0] = "toyota"
print(car)
x = len(car)
print(x)
#loop:
for x in car:
	print(x)
car.append("honda")
print(car)
car.pop(1)
print(car)
car.remove("BMW")
print(car)

#create a class
class myclass:
	x = 5
print(myclass)

#crate Object:
class MyClass:
	x = 5
p1 = MyClass()
print(p1.x)

#The__init__Function:
class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
p1 = person("John", 36)
print(p1.name)
print(p1.age)

#Object Methods:
class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("Hello my name is" + self.name)
p1 = person(" john", 36)
p1.myfunc()

#THe self Paramete:
class person:
	def __init__(mysillyobject, name, age):
		mysillyobject.name = name
		mysillyobject.age = age
	def myfunc(abc):
		print("hello my name is jiwan chand " + abc.name)

p1 = person("john", 36)
p1.myfunc()


#Modify object:
class person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("namaskar ma jiwan" + self.name)
p1 = person("john", 36)
p1.age = 40
print(p1.age)

#python Innheritance:
class person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)
x = person("jiwan", "chand")
x.printname()
#crate a chhild:
class person:
	def __init__(self, fname, lname):

	    self.firstname = fname
	    self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)
class student(person):
	pass
x = student("Mike", "olsen")
x.printname()

#Add init funnction:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

class person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)
class student(person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)
x = student("jiwan", "chand")
x.printname()

#ADD properties:
class Jerson:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)
class student(Jerson):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)
		self.graduationyear = 2039
x = student("jiwan", "olsen")
print(x.graduationyear)

#Add methods:
class manxey:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname
	def printname(self):
		print(self.firstname, self.lastname)
class student(manxey):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

	def welcome(self):
		print("welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = student("jiwan", "chand", 2057)
x.welcome()

#python Iterator:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mero = ("banan", "mango",  "cherry")
for x in mero:
	print(x)

jiwan = "mango"
for x in jiwan:
	print(x)

#Create an Iterator:
class mynumber:
	def __iter__(self):
		self.a = 1
		return self
	def __next__(self):
		x = self.a
		self.a += 1
		return x
myclass = mynumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#stop Itteration:
class numbers:
	def __iter__(self):
		self.a =1
		return self
	def __next__(self):
		if self.a <= 20:
			x = self.a
			self.a += 1
			return x
		else:
			raise StopIteration
chand = numbers()
iteration = iter(chand)

for x in iteration:
	print(x)

#Python scope:
def myfunc():
	x = 300
	print(x)
myfunc()

#Function inside function:
def myfunc():
	x = 456
	def myinnerfunc():
		print(x)
	myinnerfunc()
myfunc()
#global scope:
x = 345
def myfunc():
	print(x)
myfunc()
print(x)

#Naming varables:
x = 300
def myfunc():
	x = 200
	print(x)
myfunc()
print(x)

#global keyword:
def myfunc():
	global x
	x = 300
myfunc()
print(x)