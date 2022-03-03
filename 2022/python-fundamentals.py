#!/usr/bin/env python
# coding: utf-8

# # Python: The Fundamentals 
# #### Teacher: Shirsho Dasgupta, Miami Herald/McClatchy DC Bureau
# #### Coach: Joe Germuska, Knight Lab (Northwestern University)
# ##### Email: shirshodg94@gmail.com

# Python is a programming language that was first released in the early-1990s. The creators wanted the language to be fun to use and work with and hence the name — a tribute to the British comedy series Monty Python. 
# 
# In journalism, we use Python to automate routine work (think periodically scraping election results), analyze data and build vizualizations from the analysis. 
# 
# You can directly write Python code on the command line (Terminal in Macs, CMDR for Windows) or write down the code in a text editor, save it with a .py extension at the end and run the file on the command line ("python filename.py").
# 
# But today we'll use Jupyter Notebook, which allows us to test our code line-by-line or section-by-section, rewrite parts of it if needed and note down comments.
# 
# Always remember, Python computes the code from top to bottom, left to right. If a bit of code is within parentheses, then that bit is computed first (just like in math, remember PEMDAS?).

# ## Datatypes and variables

# In[1]:


"Hello IRE NICAR!"


# In[2]:


print("Hello IRE NICAR!")


# There are broadly three kinds of datatypes:
#     1. Strings (texts or numbers that you won't be doing math on, like zipcodes)
#     2. Numbers (integers, decimals, etc.)
#     3. Boolean (true or false)

# In[3]:


### shows data-type of the entry in the parenthesis
type("Hello IRE NICAR!")


# "str" stands for "String"

# Note: Strings are declared by wrapping up a text/number within quotes. It does not matter whether you use a single or a double quote. BUT if the text itself has a quote (like an apostrophe) then that can cause an error because Python will read that apostrophe as a regular quote.

# In[4]:


type(1)


# "int" stands for "Integer" (numbers like 0, 1, 2, -5 etc.)

# In[5]:


type(2.38)


# "float" stands for "Floating-point" (decimals like 5.68 or 97.82 etc.)

# In[6]:


type(True)


# In[7]:


type(False)


# "bool" stands for "Boolean" (True or False statements)

# Booleans are written by capitalizing the first letter — "True" or "False". 
# They are generally used in performing conditional operations. For instance, if the result from a condition is met, then subsequent mathematical operations are performed.

# #### Conditional operators
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== equal to
!= not equal to
# In[8]:


### checks whether 4 is greater than 6
4>6


# In[9]:


### checks whether 6 is greater than 4
6>4


# In[10]:


"IRE" == "ire"


# In[11]:


"IRE" == "IRE"


# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# #### Concatenation and adding

# In[12]:


print("IRE" + " " + "NICAR")


# In[13]:


print(4+5)


# In[14]:


### putting anything in quotes treats it as text/strings
print("4" + "5")


# #### Storing in variables

# General syntax for storing in variables: 
# variable_name = "some type of info"

# In[15]:


string = "Hello IRE NICAR!"
integer = 9 
decimal = 78.65

print(string)
print(integer)
print(decimal)


# In[16]:


### another way of concatenating two variables — especially useful if they are of different datatypes
print(string, integer)

### print(string + integer) will not concatenate because the "+" sign only works on strings


# In[17]:


x = 9
y = 6
adding = x + y
print(adding)


# In[18]:


name = "John"
print(name)


# In[19]:


name = "Susie"
print(name)


# Note: Some words are reserved in Python, like "float", "int", "for", "and" etc. These refer to certain functions or conditions and CANNOT be used as variable names. 

# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# ### Numbers and Math

# In[20]:


5+6+8


# In[21]:


5-10


# In[22]:


60/6


# In[23]:


int(60/6)


# In[24]:


x = 7
y = 8
mult = 7*8

print(mult)


# In[25]:


### ** raises the first number to the power of the second number 
10**2


# In[26]:


number = 5
power = 2
result = number ** power

print(result)


# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# ## Data collections

# ### Lists

# When you're working with Python, you may encounter a situation where you have to create a list of elements, all stored in one variable. Think of it as a big box with several compartments. 
# 
# To create one, we use square braces and a variable.

# In[27]:


names = ["John", "Susie", "Mike", "Sarah", "Teddy"]


# In[28]:


print(names)


# Note: Positions (from left to right) starts from 0. 
# 
# Position 0 is the first cell/compartment which has the word "John".
# Position 1 is the second cell which has the word "Susie" and so on.

# In[29]:


print(names[0])


# In[30]:


x = names[3]
print(x)


# Note: Positions (from right to left) starts from -1.
#     
# Position -1 is the last cell/compartment. Position -2 is the penultimate cell and so on. 

# In[31]:


y = names[-2]
print(y)


# In[32]:


### prints all elements before position 3.
x = names[:3]
print(x)


# In[33]:


### prints all elements in position 3 and beyond. 
x = names[3:]
print(x)


# In[34]:


### prints all elements in position 1 and beyond. 
x = names[1:]
print(x)


# In[35]:


### prints all elements which come before position 4 but also in position 2 and beyond. 
### the "2:" and ":4" sort of cancel each other out and the result is whatever elements remain. 

x = names[2:4]
print(x)


# In[36]:


### the last two items
x = names[-2:]
print(x)


# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# In[37]:


len(names)


# "len" is a function that stores the length or number of elements in a variable. 

# In[38]:


length = len(names)
print(length)


# In[39]:


print(names)


# In[40]:


### adds another element to the end of a list
names.append("Eleanor")


# In[41]:


print(names)


# In[42]:


### removes the last element of the list
names.pop()

### last_name = names.pop() will remove the last element and store it in variable "last_name"


# In[43]:


print(names)


# In[44]:


### removes element referred to by the position in the parenthesis
names.pop(2)


# In[45]:


print(names)


# "in" or "not in" checks whether a certain element is in a list. It returns a boolean value (True/False). 

# In[46]:


"Jack" in names


# In[47]:


x = "Jack"
x in names


# In[48]:


x = "Susie"
x in names


# In[49]:


x = "Susie"
x not in names


# In[50]:


x = "Jack"
x not in names


# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# ### Dictionaries

# A dictionary is essentially a more complicated list. It contains related values with "keys" to refer to them. Think of it as a spreadsheet where each "key" is a column name and the elements in each key are the cells below a column.
# 
# A dictionary is created by using curly braces. 

# In[51]:


dictionary = {
    "book": "moby-dick",
    "author": "melville",
    "year": 1851
}


# In[52]:


### refers to elements stored under key "book"
dictionary["book"]


# In[53]:


x = dictionary["year"]
print(x)


# In[54]:


type(x)


# In[55]:


x = dictionary["author"]
type(x)


# In[56]:


### creates a new key and stores a value under it
dictionary["publisher"] = "richard bentley"


# In[57]:


dictionary


# In[58]:


### deletes the key and all the elements stored under it
del dictionary["publisher"]


# In[59]:


dictionary


# In[60]:


### stores multiple elements under each key 
### each key is like a list, the dictionary now becomes a collection of lists
dictionary = {
    "book": ["moby-dick", "the grapes of wrath", "american pastoral"],
    "author": ["melville", "steinbeck", "roth"],
    "year": [1851, 1939, 1997]
}


# In[61]:


### refers to the first element (position 0) under key "book"
dictionary["book"][0]


# In[62]:


### refers to the second element (position 1) under key "book"
dictionary["author"][1]


# In[63]:


### stores the third element (position 2) under key "book"
x = dictionary["author"][2]
print(x)


# In[64]:


### adds a new element at the end of the lists stored under the keys
dictionary["book"].append("the great gatsby")
dictionary["author"].append("fitzgerald")


# In[65]:


dictionary


# In[66]:


### removes the last element under the key
dictionary["author"].pop(-1)


# In[67]:


dictionary


# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# ## Conditional statements

# Conditional statements are used to check, as the words suggest, whether certain conditions are met. 
# 
# Usually they take the form:
# IF a certain condition is met, THEN subsequent corresponding lines of code are executed; ELSE other code is executed or the code breaks.
# 
# In Python, they statements use the reserved words "if", "elif" (standing for "else if") or "else". 
# 
# Note: For conditional statements, indentation is very important. Jupyter indents automatically but if you are writing code in a text editor like Sublime, you have to be careful yourself. 

# In[68]:


if 5 < 10:
    print("5 is less than 10")


# In[69]:


x = 10
y = 9 

if x < y:
    print("10 is less than 9")
else:
    print("9 is less than 10")


# In[70]:


team_a = 4
team_b = 3

if team_a > team_b:
    print("We won!")
elif team_a == team_b:
    print("We tied!")
else:
    print("We lost!")


# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# ## Looping

# Loops are used to iterate and perform the same function again and again — very useful for automation. 
# 
# For instance, consider the list "names" again. If we wish to print each name, instead of writing separate print statements each time, we can just use a loop.

# In[71]:


names = ["John", "Susie", "Mike", "Sarah", "Teddy"] 


# In[72]:


for name in names:
    print(name)

### note: the word "name" is completely arbitrary, you can use any other word like "element", "row", "x" etc. 


# In[73]:


numbers = [70, 80, 90, 100, 110]

for number in numbers:
    print(number)


# In[74]:


### performing a mathematical function while executing a loop

### initializing a variable "x"
x = 0

for number in numbers:
    x = number/10
    print(x)


# In[75]:


sentence = "Hello IRE NICAR!"

for letter in sentence:
    print(letter)


# As an aside, a string is generally treated as a list with each letter acting as an element.

# In[76]:


len(sentence)


# In[77]:


sentence[:4]


# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# In[78]:


dictionary


# In[79]:


### iterating through each key
for key in dictionary:
    print(key)


# In[80]:


### iterating through each key and displaying elements for each
for key in dictionary:
    print(dictionary[key])


# In[81]:


### iterating through each key and displaying only the first element for each
for key in dictionary:
    print(dictionary[key][0])


# #### "For ... in range" loops

# The "for ... in range(x, y)" defines a loop that runs through the numbers starting for "x" and ending in the one right before "y"

# In[82]:


for i in range(0, 10):
    print(i)


# The "for ... in range(x, y, z)" defines a loop that runs through the numbers starting for "x" and ending in the one right before "y" but at intervals of "z"

# In[83]:


### prints the third number within the loop after starting
for i in range(0, 10, 3):
    print(i)


# #### Nested loops

# Nested loops are loops within loops. 
# 
# Say loop 2 is within loop 1, then for each iteration of loop 1, all iterations of loop 2 are performed

# In[84]:


dictionary


# In[85]:


### loop 1: runs through each key in the dictionary
for key in dictionary:
    
    ### stores length or the number of elements under each key
    x = len(dictionary[key])
    
    ### loop 2: for each key, it runs through all the elements stored in it and prints each one separately
    for i in range(0, x):
        entry = str(dictionary[key][i])
        print(key + ": " + entry)


# ##### Try it!

# In[ ]:





# In[ ]:





# In[ ]:





# #### Remember: 

# 1. Always, ALWAYS document your code using markdowns and comments. 
# 2. Keep saving your work as you code. 
# 3. When you get those errors, Google is your friend! 
# 4. Ask for help from data reporters in your newsroom or elsewhere (join the News Nerdery slack)! 
# 5. Expect to make mistakes. 
# 6. https://www.learnpython.org/ and https://learnpythonthehardway.org/ are great resources.
# 7. Practise with small datasets first. 

# ##### ... and finally

# In[86]:


import this


# In[ ]:




