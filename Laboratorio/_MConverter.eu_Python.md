---
jupyter:
  accelerator: GPU
  colab:
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.10.9
  nbformat: 4
  nbformat_minor: 0
---

::: {.cell .markdown id="UZYKtghDNdnr"}
# Introduction to Python
:::

::: {.cell .markdown id="BJIP7EzdNdns"}
This is a notebook. Respect to a classic script file, the notebook is organized in cells. We can mix textual cells and code cells. The code cells can be singularly executed and the relative output is automatically included in the notebook.

The first instruction, write in the cell the following instruction:

``` python
print("Hello, World!")
```

then execute the cell.
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":258,\"status\":\"ok\",\"timestamp\":1677858414810,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="HWDhCoXUNdnt" outputId="32c43443-cfae-4f99-eb57-3468756076ee"}
``` python
# write here #
print("ciao")
```

::: {.output .stream .stdout}
    ciao
:::
::::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-11T18:44:39.389686Z\",\"start_time\":\"2019-05-11T18:44:39.384244Z\"}" id="lnogpXbGNdnx"}
In Python, to have a guide for any method or type, we can use the function `help( )`. Try to execute the following cell.
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:45:23.584905Z\",\"start_time\":\"2019-05-11T18:45:23.579141Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":278,\"status\":\"ok\",\"timestamp\":1677858434871,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="2RYgsOZ9Ndny" outputId="1523963d-c9f9-438f-f534-84c2f853255d"}
``` python
help(print)
```

::: {.output .stream .stdout}
    Help on built-in function print in module builtins:

    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
:::
::::

::: {.cell .markdown id="8FJrhkv2Ndn1"}
# Variables & Primitive Types

Python is a dynamically-typed language. There is no explicit declaring of the variable type. The variable is created at the first assignment.

``` python
a = 100
c = "ALOHA!"
```

Variable name follows the classic rules. It must contain only letters, digits or underscores and it cannot start with a digits.

The basic types of Python include `int` (integers), `float` (floating point numbers), `str` (character strings) and `bool` (booleans).

``` python
a = 10         # an integer
b = 3.14       # a floating point number
c = "string"   # character string
d = True       # a boolean
```

Python has also an automatic memory management. We do not need to explicitly deallocate a variable. Eventually, we can use the command `del`. Try to execute the following cell.
:::

::: {.cell .code id="FrO8HyqbKVqe"}
``` python
c = c + c
```
:::

::: {.cell .code id="eMtwF_yGrKYz"}
``` python
c = "roses are red"
```
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-10T20:33:23.797692Z\",\"start_time\":\"2019-05-10T20:33:23.783433Z\"}" id="tEMyA2azNdn2"}
``` python

print(c)
del c
print(c)
```
:::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-10T20:39:37.966162Z\",\"start_time\":\"2019-05-10T20:39:37.961047Z\"}" id="TEjVDBhbNdn_"}
The function `int( )` converts the input to an integer.
Similarly, the functions `str( )` and `float( )`.
To obtain the type of any variable in Python, we can use the `type( )` function.
While, we can use the `isinstance( )` function to check the type of a variable.
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:47:21.826268Z\",\"start_time\":\"2019-05-11T18:47:21.815417Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":3,\"status\":\"ok\",\"timestamp\":1677858678451,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="zwWKo-_dNdoB" outputId="4b2b71c7-2bcf-4d4a-ab7e-82ea0cb694af"}
``` python
a = 5
b = str(a)
print("Is 'a' an integer?", isinstance(a, int))
print("Is 'a' an string ?", isinstance(a, str))
print("Is 'b' an integer?", isinstance(b, int))
print("Is 'b' an string ?", isinstance(b, str))
print("Which type is 'b' ?", type(b))
```

::: {.output .stream .stdout}
    Is 'a' an integer? True
    Is 'a' an string ? False
    Is 'b' an integer? False
    Is 'b' an string ? True
    Which type is 'b' ? <class 'str'>
:::
::::

::: {.cell .markdown id="lGfyLwd3PACE"}
## Operators and Functions
:::

::: {.cell .markdown id="4aowJMdfNdoF"}
### Main operations and functions for numeric types:

| Command  | Description                             |
|----------|-----------------------------------------|
| `+`      | Addition                                |
| `-`      | Subtraction                             |
| `*`      | Multiplication                          |
| `/`      | Division                                |
| `//`     | Floor division                          |
| `%`      | Modulo                                  |
| `**`     | Exponent                                |
| `abs( )` | Aabsolute value                         |
| `==`     | True, if it is equal                    |
| `!=`     | True, if it is not equal to             |
| `<`      | True, if it is less than                |
| `<=`     | True, if it is less than or equal to    |
| `>`      | True, if it is greater than             |
| `>=`     | True, if it is greater than or equal to |
| `and`    | True, if both arguments are True        |
| `or`     | True, if al least an argument is True   |
| `not`    | True, if the argument is False          |
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-10T20:57:39.506889Z\",\"start_time\":\"2019-05-10T20:57:39.501086Z\"}" id="aq5TUmYWNdoF"}
``` python
print(7 / 4)  # the division between two integers is a floating point number (note: this is not true in Python 2.x)
print(7 // 4) # use double slash to obtain a integer
```
:::

::: {.cell .markdown id="Ymtz_u16NdoI"}
### Main operations and functions for strings:

| Command  | Description                                         |
|----------|-----------------------------------------------------|
| `+`      | to concatenate two strings                          |
| `len( )` | to obtain the length of a string                    |
| `*`      | to replicate the string                             |
| `in`     | to determine if a string is included in another     |
| `not in` | to determine if a string is not included in another |
| `%`      | to obtain a formatted string inserting values       |
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-10T20:54:34.398946Z\",\"start_time\":\"2019-05-10T20:54:34.392387Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":2,\"status\":\"ok\",\"timestamp\":1677858849746,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="xa4bu0FjNdoJ" outputId="9c5337c8-80e2-47c4-87dc-8683a384397d"}
``` python
x = 'First'
y = "Second"
z = x + y
print(z)
```

::: {.output .stream .stdout}
    FirstSecond
:::
::::

::: {.cell .markdown id="Q-u1RoHmNdoL"}
Note, we can use both double `"` and singular `'` quotes to denote string values.
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T20:28:53.747861Z\",\"start_time\":\"2019-05-11T20:28:53.742194Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":2,\"status\":\"ok\",\"timestamp\":1677858856386,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="Ph9Xt3LRNdoO" outputId="971591be-3e85-4773-8b4c-1b6410ee03af"}
``` python
x = 'replicated '
y = x * 3
print(y)
```

::: {.output .stream .stdout}
    replicated replicated replicated 
:::
::::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T20:30:23.263952Z\",\"start_time\":\"2019-05-11T20:30:23.258427Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":15,\"status\":\"ok\",\"timestamp\":1677858865480,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="KMUBtdMANdoQ" outputId="615f994c-c20a-4b1a-fa36-f2b96d5ed58f"}
``` python
x = "roses are red"
print("is 'are' in x?"   , "are" in x)
print("is not 'is' in x?", "is" not in x)
```

::: {.output .stream .stdout}
    is 'are' in x? True
    is not 'is' in x? True
:::
::::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-10T20:54:36.291734Z\",\"start_time\":\"2019-05-10T20:54:36.286316Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":3,\"status\":\"ok\",\"timestamp\":1677858883915,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="vcC6L2IZNdoS" outputId="7b6c0571-e8f2-402d-bd4a-b8267921f958"}
``` python
y = 12.71634356576
x = "Number of months a year is %.2f" % y
print(x)
```

::: {.output .stream .stdout}
    Number of months a year is 12.72
:::
::::

::: {.cell .markdown id="qR1Wc0NLNdoU"}
Note, The operator `%` is equivalent to **printf** in C/C++.
:::

::: {.cell .markdown id="RyA3wgW9NdoU"}
# Data Structures

The Python natively includes structured types to collect or group data.
We introduce only the types `list`, `tuple`, and `dict`.
:::

::: {.cell .markdown id="ZsZPbsKHPNhM"}
## Lists

A `list` is a sequence of elements where each element can be of a different type.
We can define a list using the square brackets.

``` python
l = [first_element, second_element, ..., last_element]
```

An element of a list can be also another list.
:::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-10T21:08:24.715678Z\",\"start_time\":\"2019-05-10T21:08:24.710945Z\"}" id="GQ9l530RNdoV"}
##### Indexing

The square brackets are also used to index the list, remember that **indexing starts from 0 in Python**.
The index value can also be negative. Using the index value -1 we obtain the last element of the list. Using the index value -2 we obtain the second-last element of the list and so on.
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-10T21:24:39.660136Z\",\"start_time\":\"2019-05-10T21:24:39.648612Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":6,\"status\":\"ok\",\"timestamp\":1677858941468,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="YTWL8lOsNdoV" outputId="c34bab9f-f6c4-439d-96e8-424a61cd5a11"}
``` python
a = list()           # is a empty list.       a = []
s = 'cat'
b = [4, 6, s, 2.71]  # list of 4 elements
print('The second element is: ', b[1])
print('The third  element is: ', b[2])
b[1]  = 11.56        # we can modify the elements of the list
print('Now, the second element is: ', b[1])
```

::: {.output .stream .stdout}
    The second element is:  6
    The third  element is:  cat
    Now, the second element is:  11.56
:::
::::

::: {.cell .markdown id="mKqwRq00NdoX"}
##### Slicing

We can extract a part of a list using the syntax `[start:stop:step]`.
The extracted list will contain from element between index `start` and `stop -1` according to the `step`.
**Note that the element at index stop is not included**.

The `step` can be omitted using the syntax `[start:stop]`, in this case the `step` is equal to 1.
We can also omit either (or both) of `start` or `stop`, the default is respectively the beginning and the end of the list.
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:52:22.569739Z\",\"start_time\":\"2019-05-11T18:52:22.552598Z\"}" id="gudGLZu1NdoY"}
``` python
x = [ 1, '2', 3.0, 4, '5'] # a list of 5 elements
print("x      =", x)
y = x[2:4]   # extract a sublist of two elements skipping the first two elements
print("x[2:4] =", y)
y = x[3:]    # extract a sublist skipping the first three elements
print("x[3:]  =", y)
y = x[:-3]   # extract a sublist skipping the last  three elements
print("x[:-3] =", y)
y = x[::2]   # extract the elements with even index values
print("x[::2] =", y)
```
:::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-11T20:51:09.006685Z\",\"start_time\":\"2019-05-11T20:51:08.984104Z\"}" id="YV2hj5_HNdob"}
##### Insertion and Removing

The lists have the methods `insert`, `append` and `pop` respectively to insert an element in the list, to append an element at the end of the list and to remove an element.
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T20:54:24.521779Z\",\"start_time\":\"2019-05-11T20:54:24.510296Z\"}" id="g6ozrJzBNdoc"}
``` python
a_list = ['first', 'second', 'third']
print('initial list:', a_list)
print()

a_list.append('fourth')
print('modified list:', a_list) # now, the list has 4 elements
print('inserted element:', a_list[-1])
print()

el = a_list.pop()
print('modified list:', a_list) # now, the list has 3 elements
print('removed  element:', el)
```
:::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-10T21:37:28.413060Z\",\"start_time\":\"2019-05-10T21:37:28.404519Z\"}" id="Oel_ZuaJNdog"}
## Tuples

A `tuple` is similar to a `list` but only big difference is the elements inside a list can be changed but in tuple it cannot be changed. A tuple can define using the round brackets.

``` python
t = (first_element, second_element, ..., last_element)
```

The indexing and slicing of a tuple are using the square brackets like for the lists.
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:09:18.709739Z\",\"start_time\":\"2019-05-11T18:09:18.437989Z\"}" id="nUJa7ybkNdoh"}
``` python
x = [1, '2', 3.0, 4, '5']  # it is a list
x[1] = '2.0'               # this is allowed
```
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":183}" executionInfo="{\"elapsed\":7,\"status\":\"error\",\"timestamp\":1677859168283,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="zIciAQ0gwcUI" outputId="e910db2d-0145-4eea-ddf4-bc725d1c53c6"}
``` python
x = (1, '2', 3.0, 4, '5')  # it is a tuple
x[1] = '2.0'               # this is not allowed
```

::: {.output .error ename="TypeError" evalue="ignored"}
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-14-a4b3ea48f424> in <module>
          1 x = (1, '2', 3.0, 4, '5')  # it is a tuple
    ----> 2 x[1] = '2.0'               # this is not allowed

    TypeError: 'tuple' object does not support item assignment
:::
::::

::: {.cell .markdown id="9bl3_RxQNdoj"}
##### List of main functions and operations on the lists or tuples

| Command     | Description                                     |
|-------------|-------------------------------------------------|
| `+`         | concatenation of two list                       |
| `*`         | replication of the list                         |
| `len( )`    | the number of elements                          |
| `min( )`    | minimum value in the list                       |
| `max( )`    | maximum value in the list                       |
| `sum( )`    | sum of the elements in the list                 |
| `sorted( )` | return a copy of the list in sorted order       |
| `in`        | True, if the element is present in the list     |
| `not in`    | True, if the element is not present in the list |
:::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-10T21:37:28.413060Z\",\"start_time\":\"2019-05-10T21:37:28.404519Z\"}" id="HNqIq6klNdoj"}
## Dictionaries

In a `dict` for each element is a key-value pair. The syntax for dictionaries is:

``` python
d = {key1 : value1, key2 : value2, ... }
```
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T21:04:39.264667Z\",\"start_time\":\"2019-05-11T21:04:39.243763Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":299,\"status\":\"ok\",\"timestamp\":1677859288912,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="LP2h4mNuNdok" outputId="96732f1e-3856-43d1-fe91-0d00c4612a07"}
``` python
# A dictionary with people names as keys and their ages as values
ages = {"Alice": 17, 'Matt': 27, 'David': 33}

# We can access to the values using the square brackets with the key
print("The age of Matt is", ages["Matt"])

# We can check is a key is in the dictionary
print("Is Bob in the dictionary?", "Bob" in ages)

# We can add a new element
ages["Bob"] = 40
print("Is Bob in the dictionary?", "Bob" in ages)

# We can remove a key-value pair
ages.pop("David")

# We can obtain the list of key
print('list of peoples:', list(ages.keys()) )
```

::: {.output .stream .stdout}
    The age of Matt is 27
    Is Bob in the dictionary? False
    Is Bob in the dictionary? True
    list of peoples: ['Alice', 'Matt', 'Bob']
:::
::::

::: {.cell .markdown id="N98HK239Ndon"}
# Control Flow Statements & Loops

Remember that in Python the *indentation* is used to define program blocks.
If the *indentation* is not correct the program is not correct.
:::

::: {.cell .markdown id="cEzqVbOuOX6K"}
## if-else if -else

``` python
if condition1:  
    code1
elif condition2:
    code2
else:
    code3
```
:::

::: {.cell .code id="JtwDrParBdh_"}
``` python
a = 9
if a>10:
  print("printed only if 'a' is greater than 10")
print("alway printed because now we are outside the if block")
```
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:28:13.229746Z\",\"start_time\":\"2019-05-11T18:28:13.222134Z\"}" id="IRZbqGFxNdon"}
``` python
a = 4
if a>10:
  print("printed only if 'a' is greater than 10")
  print("also this is printed only if 'a' is greater than 10")
```
:::

::: {.cell .markdown id="2AM1wzbCNdop"}
## while

``` python
while condition:  
    code
```
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:30:02.082201Z\",\"start_time\":\"2019-05-11T18:30:02.075534Z\"}" id="IY9-2MkVNdoq"}
``` python
a = 4
while a>0:
    print("printed until 'a' is greater than 0")
    a = a -1
```
:::

::: {.cell .markdown id="WdqI22cHNdos"}
## for

``` python
for variable in iterator:
    code
```

For looping over integers, we can use the function the `range(start,stop,step)`, for examples:

- `range(b)` = 0, 1, \..., b-1
- `range(a,b)` = a, a+1, \..., b-1
- `range(a,b,s)` = a, a+s, a+2s, \..., a + ((a-b-1)//s) \* s
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:34:36.245536Z\",\"start_time\":\"2019-05-11T18:34:36.240724Z\"}" id="slMVsbgcNdot"}
``` python
# print the number from 0 to 9
for x in range(10): 
    print(x)
```
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:34:59.023972Z\",\"start_time\":\"2019-05-11T18:34:59.017248Z\"}" id="90Mql8r4Ndow"}
``` python
# print the number from 5 to 9
for x in range(5,10): 
    print(x)
```
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:38:33.423547Z\",\"start_time\":\"2019-05-11T18:38:33.418024Z\"}" id="Lej0Zm3fNdox"}
``` python
l = ["dog", "cat", "mouse"]
# print the elements of the list
for x in l: 
    print(x)
```
:::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-10T21:35:23.827812Z\",\"start_time\":\"2019-05-10T21:35:23.819860Z\"}" id="-nyQ3-rlNdoz"}
## List comprehension

A very powerful concept in Python is the list comprehension. We can create lists using *for* loops in a compact way.

``` python
[fun(item) for item in a_list ]
```
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:32:27.514002Z\",\"start_time\":\"2019-05-11T18:32:27.508491Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":303,\"status\":\"ok\",\"timestamp\":1677859689390,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="bAYBo5VgNdo0" outputId="3f206987-91bc-4ef2-9e5e-6cd001b60fa1"}
``` python
l = [5.7, 3.0, 4, 1]  #  a list of numbers
squared_l = [x**2 for x in l if x < 3.5]  #  the list of squared elements
print(squared_l)
```

::: {.output .stream .stdout}
    [9.0, 1]
:::
::::

::: {.cell .markdown id="9VIoXZeiNdo2"}
# Functions

The keyword `def` is used to define function. The basic syntax of a function is:

``` python
def function_name(argIn1, argIn2,... argInN):
    code
    return argOut1, argOut2,... argOutN
```
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T18:42:25.512903Z\",\"start_time\":\"2019-05-11T18:42:25.505903Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1677859728118,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="vWBH0VCZNdo2" outputId="a7264d1f-74f3-4943-c5e3-06bcfe97d764"}
``` python
# define a function
def HelloWorld():   
    print("Hello, World!")
    
# execute a function
HelloWorld()
```

::: {.output .stream .stdout}
    Hello, World!
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":5,\"status\":\"ok\",\"timestamp\":1677859742709,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="y8Tbb2L88EaJ" outputId="3058e213-0641-4380-85d0-40ecec5faaa5"}
``` python
HelloWorld()
```

::: {.output .stream .stdout}
    Hello, World!
:::
::::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-11T19:00:43.880790Z\",\"start_time\":\"2019-05-11T19:00:43.875774Z\"}" id="g3UEKT-ANdo4"}
We can description the functions including the comments after the function definition, before the code in the function body.
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T19:04:29.721982Z\",\"start_time\":\"2019-05-11T19:04:29.711694Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":310,\"status\":\"ok\",\"timestamp\":1677859768123,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="MjvI1MH3Ndo5" outputId="9d17f239-b5e6-45c4-bf03-2f1145875187"}
``` python
def half(x):
    """
    Return the half value of x.
    """
    return x / 2

help(half)
```

::: {.output .stream .stdout}
    Help on function half in module __main__:

    half(x)
        Return the half value of x.
:::
::::

::: {.cell .markdown id="h5S67SmzNdo8"}
We can set a default value for input arguments of the function in the following way:
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T20:36:06.035756Z\",\"start_time\":\"2019-05-11T20:36:06.030869Z\"}" id="6K5Woh9lNdo8"}
``` python
def half(x = 1):
    """
    Return the half value of x.
    If the input argument is not specified, the value 0.5 is returned.
    """
    return x / 2

print(half(2))
print(half())
```
:::

::: {.cell .markdown id="kJgEcPzrNdo-"}
# Modules & Packages

In Python, a module is a file with extention **.py** where we can collect related variables, functions and others.

Create the file \'my_module.py\' executing the following code:
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T21:18:49.518760Z\",\"start_time\":\"2019-05-11T21:18:49.512666Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":313,\"status\":\"ok\",\"timestamp\":1677859898688,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="TSgUYKr1Ndo-" outputId="a46fdefc-5341-44c2-f5d6-40a01bef0ca4"}
``` python
%%file my_module.py
"""
Example of a python module. Contains a variable called my_variable,
a function called my_function.
"""

my_variable = 0

def my_function():
    """
    Example function
    """
    return my_variable+1
    
```

::: {.output .stream .stdout}
    Writing my_module.py
:::
::::

::: {.cell .markdown id="9ZyZDvw_NdpC"}
A module can be made accessible to other Python modules using the `import` keyword.
We can use the variables, functions in the module through the dot operator.
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-11T21:18:51.634818Z\",\"start_time\":\"2019-05-11T21:18:51.626659Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":348,\"status\":\"ok\",\"timestamp\":1677859939752,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="ucNMMu0NNdpD" outputId="66970c67-4fc4-4ba8-eb54-afd731bcefeb"}
``` python
import my_module
a = my_module.my_variable
print(a)
b = my_module.my_function()
print(b)
```

::: {.output .stream .stdout}
    0
    1
:::
::::

::: {.cell .markdown id="g_TQFvlfNdpE"}
We can also set a alias for the module using the syntax:

``` python
import module_name as alias
```

Different modules are logically combined together into collections called packages. A package is a plain folder with `__init__.py` file. We can use
`import` keyword to have access to the whole package:

``` python
import package_name
package_name.module_name.function_name()
```

We may avoid using the dot operator by importing the thing you need directly, for examples:

``` python
from package_name import module_name
module_name.function_name()

from package_name.module_name import function_name
function_name()
```

The `os.path` module is a standard module of Python. It is useful to manager file paths.
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T09:01:43.157453Z\",\"start_time\":\"2019-05-16T09:01:43.147087Z\"}" id="19r0PDcgNdpF"}
``` python
import os   # import of the package
a = os.path.isfile('my_module.py') # access to the function using dots

from os import path   # import of the module
a = path.isfile('my_module.py') 

from os.path import isfile # import of the function
a = isfile('my_module.py') # access to the function without dots
```
:::
