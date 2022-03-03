# Python: The Fundamentals 
#### Teacher: Shirsho Dasgupta, Miami Herald/McClatchy DC Bureau
#### Coach: Joe Germuska, Knight Lab (Northwestern University)
##### Email: shirshodg94@gmail.com

Python is a programming language that was first released in the early-1990s. The creators wanted the language to be fun to use and work with and hence the name — a tribute to the British comedy series Monty Python. 

In journalism, we use Python to automate routine work (think periodically scraping election results), analyze data and build vizualizations from the analysis. 

You can directly write Python code on the command line (Terminal in Macs, CMDR for Windows) or write down the code in a text editor, save it with a .py extension at the end and run the file on the command line ("python filename.py").

But today we'll use Jupyter Notebook, which allows us to test our code line-by-line or section-by-section, rewrite parts of it if needed and note down comments.

Always remember, Python computes the code from top to bottom, left to right. If a bit of code is within parentheses, then that bit is computed first (just like in math, remember PEMDAS?).

## Datatypes and variables


```python
"Hello IRE NICAR!"
```




    'Hello IRE NICAR!'




```python
print("Hello IRE NICAR!")
```

    Hello IRE NICAR!


There are broadly three kinds of datatypes:
    1. Strings (texts or numbers that you won't be doing math on, like zipcodes)
    2. Numbers (integers, decimals, etc.)
    3. Boolean (true or false)


```python
### shows data-type of the entry in the parenthesis
type("Hello IRE NICAR!")
```




    str



"str" stands for "String"

Note: Strings are declared by wrapping up a text/number within quotes. It does not matter whether you use a single or a double quote. BUT if the text itself has a quote (like an apostrophe) then that can cause an error because Python will read that apostrophe as a regular quote.


```python
type(1)
```




    int



"int" stands for "Integer" (numbers like 0, 1, 2, -5 etc.)


```python
type(2.38)
```




    float



"float" stands for "Floating-point" (decimals like 5.68 or 97.82 etc.)


```python
type(True)
```




    bool




```python
type(False)
```




    bool



"bool" stands for "Boolean" (True or False statements)

Booleans are written by capitalizing the first letter — "True" or "False". 
They are generally used in performing conditional operations. For instance, if the result from a condition is met, then subsequent mathematical operations are performed.

#### Conditional operators
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== equal to
!= not equal to

```python
### checks whether 4 is greater than 6
4>6
```




    False




```python
### checks whether 6 is greater than 4
6>4
```




    True




```python
"IRE" == "ire"
```




    False




```python
"IRE" == "IRE"
```




    True



##### Try it!


```python

```


```python

```


```python

```

#### Concatenation and adding


```python
print("IRE" + " " + "NICAR")
```

    IRE NICAR



```python
print(4+5)
```

    9



```python
### putting anything in quotes treats it as text/strings
print("4" + "5")
```

    45


#### Storing in variables

General syntax for storing in variables: 
variable_name = "some type of info"


```python
string = "Hello IRE NICAR!"
integer = 9 
decimal = 78.65

print(string)
print(integer)
print(decimal)
```

    Hello IRE NICAR!
    9
    78.65



```python
### another way of concatenating two variables — especially useful if they are of different datatypes
print(string, integer)

### print(string + integer) will not concatenate because the "+" sign only works on strings
```

    Hello IRE NICAR! 9



```python
x = 9
y = 6
adding = x + y
print(adding)
```

    15



```python
name = "John"
print(name)
```

    John



```python
name = "Susie"
print(name)
```

    Susie


Note: Some words are reserved in Python, like "float", "int", "for", "and" etc. These refer to certain functions or conditions and CANNOT be used as variable names. 

##### Try it!


```python

```


```python

```


```python

```

### Numbers and Math


```python
5+6+8
```




    19




```python
5-10
```




    -5




```python
60/6
```




    10.0




```python
int(60/6)
```




    10




```python
x = 7
y = 8
mult = 7*8

print(mult)
```

    56



```python
### ** raises the first number to the power of the second number 
10**2
```




    100




```python
number = 5
power = 2
result = number ** power

print(result)
```

    25


##### Try it!


```python

```


```python

```


```python

```

## Data collections

### Lists

When you're working with Python, you may encounter a situation where you have to create a list of elements, all stored in one variable. Think of it as a big box with several compartments. 

To create one, we use square braces and a variable.


```python
names = ["John", "Susie", "Mike", "Sarah", "Teddy"]
```


```python
print(names)
```

    ['John', 'Susie', 'Mike', 'Sarah', 'Teddy']


Note: Positions (from left to right) starts from 0. 

Position 0 is the first cell/compartment which has the word "John".
Position 1 is the second cell which has the word "Susie" and so on.


```python
print(names[0])
```

    John



```python
x = names[3]
print(x)
```

    Sarah


Note: Positions (from right to left) starts from -1.
    
Position -1 is the last cell/compartment. Position -2 is the penultimate cell and so on. 


```python
y = names[-2]
print(y)
```

    Sarah



```python
### prints all elements before position 3.
x = names[:3]
print(x)
```

    ['John', 'Susie', 'Mike']



```python
### prints all elements in position 3 and beyond. 
x = names[3:]
print(x)
```

    ['Sarah', 'Teddy']



```python
### prints all elements in position 1 and beyond. 
x = names[1:]
print(x)
```

    ['Susie', 'Mike', 'Sarah', 'Teddy']



```python
### prints all elements which come before position 4 but also in position 2 and beyond. 
### the "2:" and ":4" sort of cancel each other out and the result is whatever elements remain. 

x = names[2:4]
print(x)
```

    ['Mike', 'Sarah']



```python
### the last two items
x = names[-2:]
print(x)
```

    ['Sarah', 'Teddy']


##### Try it!


```python

```


```python

```


```python

```


```python
len(names)
```




    5



"len" is a function that stores the length or number of elements in a variable. 


```python
length = len(names)
print(length)
```

    5



```python
print(names)
```

    ['John', 'Susie', 'Mike', 'Sarah', 'Teddy']



```python
### adds another element to the end of a list
names.append("Eleanor")
```


```python
print(names)
```

    ['John', 'Susie', 'Mike', 'Sarah', 'Teddy', 'Eleanor']



```python
### removes the last element of the list
names.pop()

### last_name = names.pop() will remove the last element and store it in variable "last_name"
```




    'Eleanor'




```python
print(names)
```

    ['John', 'Susie', 'Mike', 'Sarah', 'Teddy']



```python
### removes element referred to by the position in the parenthesis
names.pop(2)
```




    'Mike'




```python
print(names)
```

    ['John', 'Susie', 'Sarah', 'Teddy']


"in" or "not in" checks whether a certain element is in a list. It returns a boolean value (True/False). 


```python
"Jack" in names
```




    False




```python
x = "Jack"
x in names
```




    False




```python
x = "Susie"
x in names
```




    True




```python
x = "Susie"
x not in names
```




    False




```python
x = "Jack"
x not in names
```




    True



##### Try it!


```python

```


```python

```


```python

```

### Dictionaries

A dictionary is essentially a more complicated list. It contains related values with "keys" to refer to them. Think of it as a spreadsheet where each "key" is a column name and the elements in each key are the cells below a column.

A dictionary is created by using curly braces. 


```python
dictionary = {
    "book": "moby-dick",
    "author": "melville",
    "year": 1851
}
```


```python
### refers to elements stored under key "book"
dictionary["book"]
```




    'moby-dick'




```python
x = dictionary["year"]
print(x)
```

    1851



```python
type(x)
```




    int




```python
x = dictionary["author"]
type(x)
```




    str




```python
### creates a new key and stores a value under it
dictionary["publisher"] = "richard bentley"
```


```python
dictionary
```




    {'book': 'moby-dick',
     'author': 'melville',
     'year': 1851,
     'publisher': 'richard bentley'}




```python
### deletes the key and all the elements stored under it
del dictionary["publisher"]
```


```python
dictionary
```




    {'book': 'moby-dick', 'author': 'melville', 'year': 1851}




```python
### stores multiple elements under each key 
### each key is like a list, the dictionary now becomes a collection of lists
dictionary = {
    "book": ["moby-dick", "the grapes of wrath", "american pastoral"],
    "author": ["melville", "steinbeck", "roth"],
    "year": [1851, 1939, 1997]
}
```


```python
### refers to the first element (position 0) under key "book"
dictionary["book"][0]
```




    'moby-dick'




```python
### refers to the second element (position 1) under key "book"
dictionary["author"][1]
```




    'steinbeck'




```python
### stores the third element (position 2) under key "book"
x = dictionary["author"][2]
print(x)
```

    roth



```python
### adds a new element at the end of the lists stored under the keys
dictionary["book"].append("the great gatsby")
dictionary["author"].append("fitzgerald")
```


```python
dictionary
```




    {'book': ['moby-dick',
      'the grapes of wrath',
      'american pastoral',
      'the great gatsby'],
     'author': ['melville', 'steinbeck', 'roth', 'fitzgerald'],
     'year': [1851, 1939, 1997]}




```python
### removes the last element under the key
dictionary["author"].pop(-1)
```




    'fitzgerald'




```python
dictionary
```




    {'book': ['moby-dick',
      'the grapes of wrath',
      'american pastoral',
      'the great gatsby'],
     'author': ['melville', 'steinbeck', 'roth'],
     'year': [1851, 1939, 1997]}



##### Try it!


```python

```


```python

```


```python

```

## Conditional statements

Conditional statements are used to check, as the words suggest, whether certain conditions are met. 

Usually they take the form:
IF a certain condition is met, THEN subsequent corresponding lines of code are executed; ELSE other code is executed or the code breaks.

In Python, they statements use the reserved words "if", "elif" (standing for "else if") or "else". 

Note: For conditional statements, indentation is very important. Jupyter indents automatically but if you are writing code in a text editor like Sublime, you have to be careful yourself. 


```python
if 5 < 10:
    print("5 is less than 10")
```

    5 is less than 10



```python
x = 10
y = 9 

if x < y:
    print("10 is less than 9")
else:
    print("9 is less than 10")
```

    9 is less than 10



```python
team_a = 4
team_b = 3

if team_a > team_b:
    print("We won!")
elif team_a == team_b:
    print("We tied!")
else:
    print("We lost!")
```

    We won!


##### Try it!


```python

```


```python

```


```python

```

## Looping

Loops are used to iterate and perform the same function again and again — very useful for automation. 

For instance, consider the list "names" again. If we wish to print each name, instead of writing separate print statements each time, we can just use a loop.


```python
names = ["John", "Susie", "Mike", "Sarah", "Teddy"] 
```


```python
for name in names:
    print(name)

### note: the word "name" is completely arbitrary, you can use any other word like "element", "row", "x" etc. 
```

    John
    Susie
    Mike
    Sarah
    Teddy



```python
numbers = [70, 80, 90, 100, 110]

for number in numbers:
    print(number)
```

    70
    80
    90
    100
    110



```python
### performing a mathematical function while executing a loop

### initializing a variable "x"
x = 0

for number in numbers:
    x = number/10
    print(x)
```

    7.0
    8.0
    9.0
    10.0
    11.0



```python
sentence = "Hello IRE NICAR!"

for letter in sentence:
    print(letter)
```

    H
    e
    l
    l
    o
     
    I
    R
    E
     
    N
    I
    C
    A
    R
    !


As an aside, a string is generally treated as a list with each letter acting as an element.


```python
len(sentence)
```




    16




```python
sentence[:4]
```




    'Hell'



##### Try it!


```python

```


```python

```


```python

```


```python
dictionary
```




    {'book': ['moby-dick',
      'the grapes of wrath',
      'american pastoral',
      'the great gatsby'],
     'author': ['melville', 'steinbeck', 'roth'],
     'year': [1851, 1939, 1997]}




```python
### iterating through each key
for key in dictionary:
    print(key)
```

    book
    author
    year



```python
### iterating through each key and displaying elements for each
for key in dictionary:
    print(dictionary[key])
```

    ['moby-dick', 'the grapes of wrath', 'american pastoral', 'the great gatsby']
    ['melville', 'steinbeck', 'roth']
    [1851, 1939, 1997]



```python
### iterating through each key and displaying only the first element for each
for key in dictionary:
    print(dictionary[key][0])
```

    moby-dick
    melville
    1851


#### "For ... in range" loops

The "for ... in range(x, y)" defines a loop that runs through the numbers starting for "x" and ending in the one right before "y"


```python
for i in range(0, 10):
    print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9


The "for ... in range(x, y, z)" defines a loop that runs through the numbers starting for "x" and ending in the one right before "y" but at intervals of "z"


```python
### prints the third number within the loop after starting
for i in range(0, 10, 3):
    print(i)
```

    0
    3
    6
    9


#### Nested loops

Nested loops are loops within loops. 

Say loop 2 is within loop 1, then for each iteration of loop 1, all iterations of loop 2 are performed


```python
dictionary
```




    {'book': ['moby-dick',
      'the grapes of wrath',
      'american pastoral',
      'the great gatsby'],
     'author': ['melville', 'steinbeck', 'roth'],
     'year': [1851, 1939, 1997]}




```python
### loop 1: runs through each key in the dictionary
for key in dictionary:
    
    ### stores length or the number of elements under each key
    x = len(dictionary[key])
    
    ### loop 2: for each key, it runs through all the elements stored in it and prints each one separately
    for i in range(0, x):
        entry = str(dictionary[key][i])
        print(key + ": " + entry)
```

    book: moby-dick
    book: the grapes of wrath
    book: american pastoral
    book: the great gatsby
    author: melville
    author: steinbeck
    author: roth
    year: 1851
    year: 1939
    year: 1997


##### Try it!


```python

```


```python

```


```python

```

#### Remember: 

1. Always, ALWAYS document your code using markdowns and comments. 
2. Keep saving your work as you code. 
3. When you get those errors, Google is your friend! 
4. Ask for help from data reporters in your newsroom or elsewhere (join the News Nerdery slack)! 
5. Expect to make mistakes. 
6. https://www.learnpython.org/ and https://learnpythonthehardway.org/ are great resources.
7. Practise with small datasets first. 

##### ... and finally


```python
import this
```

    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!



```python

```
