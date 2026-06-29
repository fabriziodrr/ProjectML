---
jupyter:
  colab:
  gpuClass: standard
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

::: {.cell .markdown id="SvrSpbgNNTl_"}
# Introduction to Numpy

Vectors and matrices are not natively managered in Python.
Although a list of lists can be used as a matrix, we need a set of function to easily work with it.
For this reason, the Numpy library is essential for dealing with vectors and matrices.
The Numpy array (`numpy.ndarray`) is generally used for vectors, matrices, and multi-dimensional data sets.
Respect to a list, the elements of a Numpy array must be homogeneous. In other words, all elements of a Numpy array must be of the same type that is defined when the array is created.

To begin to use the Numpy library, we need to import the `numpy` module.
:::

::: {.cell .code execution_count="1" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:14.551540Z\",\"start_time\":\"2019-05-16T13:48:14.397473Z\"}" executionInfo="{\"elapsed\":80,\"status\":\"ok\",\"timestamp\":1740855690424,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="Q9Fk4AhFNTmB"}
``` python
import numpy as np
```
:::

::: {.cell .markdown id="weS-04XZNTmH"}
Note that we have used an alias. In this way, we will access only using `np.` to the variables and functions of the Numpy library.

For convenience, the Numpy array will be called simply array. An array can be created in different ways. A first way is to create if from a list using the function `np.array( )`.
:::

:::: {.cell .code execution_count="2" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:14.571838Z\",\"start_time\":\"2019-05-16T13:48:14.554874Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":48,\"status\":\"ok\",\"timestamp\":1740855690493,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="d7j_Ed4nNTmI" outputId="5c47644f-6ee5-4660-be0b-23eb5dc13480"}
``` python
# to create new vector from a lists we can use the `np.array` function.
l1 = [[ 4, 5, 1, 3, 4]]  # it is a list
a1 = np.array(l1)      # it is an array
print('Vector:', a1)

l2 = [ [5.0, 1.4,], [5.5, 2.1] ]  # it is a list of lists
a2 = np.array(l2)                # it is an array
print('Matrix:\n', a2)

# We can explicitly define the type of data using the `dtype` argument:
a3 = np.array(l2, dtype=int)
print('Matrix of integeres:\n', a3)
```

::: {.output .stream .stdout}
    Vector: [[4 5 1 3 4]]
    Matrix:
     [[5.  1.4]
     [5.5 2.1]]
    Matrix of integeres:
     [[5 1]
     [5 2]]
:::
::::

::: {.cell .markdown id="i1kfewigNTmL"}
## Data Type

Numpy supportd differents data types, such as: `np.uint8`, `np.int64`, `np.float32`, `np.float64`, `np.complex64`, `np.bool`.

Using the `dtype` property of an array, we can know the data type.
:::

:::: {.cell .code execution_count="3" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:14.694101Z\",\"start_time\":\"2019-05-16T13:48:14.574439Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":17,\"status\":\"ok\",\"timestamp\":1740855690643,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="WPWzac0YNTmM" outputId="d18d011f-22ad-4a32-96cc-5062ea908c6e"}
``` python
print("The data type of 'a1' is ", a1.dtype)
print("The data type of 'a2' is ", a2.dtype)
print("The data type of 'a3' is ", a3.dtype)
```

::: {.output .stream .stdout}
    The data type of 'a1' is  int64
    The data type of 'a2' is  float64
    The data type of 'a3' is  int64
:::
::::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-12T12:16:12.819758Z\",\"start_time\":\"2019-05-12T12:16:12.814014Z\"}" id="MiF2E89eNTmP"}
## Properties of arrays

An array has other useful properties:

- `.ndim` : returns the number of dimensions.
- `.shape` : returns a tuple where each element is the length along that dimension.
- `.size` : returns the number of elements of the array.
- `.nbytes`: returns the bytes of the array.
:::

:::: {.cell .code execution_count="4" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":20,\"status\":\"ok\",\"timestamp\":1740855690670,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="KqZ5DhBQyR5v" outputId="4ce5c5e7-6b6b-462b-bd82-149d99ef5012"}
``` python
print("The  ndim of 'a1' is ", a1.ndim )
print("The  ndim of 'a2' is ", a2.ndim )
```

::: {.output .stream .stdout}
    The  ndim of 'a1' is  2
    The  ndim of 'a2' is  2
:::
::::

:::: {.cell .code execution_count="5" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":9,\"status\":\"ok\",\"timestamp\":1740855690680,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="Om0tB7lwyZCg" outputId="943d2c56-a52d-4d98-81f7-1b8d93deb106"}
``` python
print("The shape of 'a1' is ", a1.shape)
print("The shape of 'a2' is ", a2.shape)
```

::: {.output .stream .stdout}
    The shape of 'a1' is  (1, 5)
    The shape of 'a2' is  (2, 2)
:::
::::

:::: {.cell .code execution_count="6" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:14.786104Z\",\"start_time\":\"2019-05-16T13:48:14.696758Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":43,\"status\":\"ok\",\"timestamp\":1740855690728,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="YwBj3aEgNTmQ" outputId="f753a74d-8cb8-4b60-cfef-ec0bc61ebbf2"}
``` python
print("The  size of 'a1' is ", a1.size )
print("The  size of 'a2' is ", a2.size )
```

::: {.output .stream .stdout}
    The  size of 'a1' is  5
    The  size of 'a2' is  4
:::
::::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-12T12:49:56.847706Z\",\"start_time\":\"2019-05-12T12:49:56.835266Z\"}" id="QTuK_jQrNTmU"}
# Creating Arrays

There are many functions that generate arrays of different forms. For examples:

- `np.array( )`: constructs an array from a list.
- `np.zeros( )`: creates an array with zeros of a given shape.
- `np.ones( )`: creates an array with ones of a given shape.
- `np.arange( )`: creates a mono-dimensional array that contains a sequence of numbers.
- `np.copy( )`: creates an array replicating another array.
- `np.random.rand( )`: creates an array with randomly-generated values from a uniform distribution.
- `np.random.randn( )`: creates an array with randomly-generated values from a normal distribution.
:::

:::: {.cell .code execution_count="7" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:14.864214Z\",\"start_time\":\"2019-05-16T13:48:14.788786Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":11,\"status\":\"ok\",\"timestamp\":1740855690742,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="vEyclBnMNTmV" outputId="005095ad-3586-4ea6-b045-e8b52b3b0512"}
``` python
# to create an array with zeros of shape (2,1,3) and dtype uint8
z = np.zeros((2,1,3), dtype=np.uint8)
print('array with zeros:\n', z)

# to create an array with ones of shape (3,2) and dtype float32
o = np.ones((3,2), dtype=np.float32)
print('array with oness:\n', o)

# to create an array with the even numbers from 0 to 10 (10 is excluded).
r = np.arange(0, 10, 2) # arguments: start, stop, step
print('array with a sequence:\n', r)

# to create an array of shape (4,4) with uniform random numbers in [0,1[
u = np.random.rand(4,4)
print('random array:\n', u)
# Note that the result of 'np.random.rand( )' is different for each execution
```

::: {.output .stream .stdout}
    array with zeros:
     [[[0 0 0]]

     [[0 0 0]]]
    array with oness:
     [[1. 1.]
     [1. 1.]
     [1. 1.]]
    array with a sequence:
     [0 2 4 6 8]
    random array:
     [[0.74088862 0.56966787 0.73169787 0.33853324]
     [0.07382178 0.18292084 0.09518032 0.00545076]
     [0.50335957 0.80780222 0.05191269 0.36509672]
     [0.41015117 0.6106163  0.70342099 0.98771382]]
:::
::::

:::: {.cell .code execution_count="8" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":5,\"status\":\"ok\",\"timestamp\":1740855690747,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="-IdaYY-gSNVK" outputId="26a7fb3c-a6ed-4f77-b2ed-f184ef52a2b6"}
``` python
z.size
```

::: {.output .execute_result execution_count="8"}
    6
:::
::::

::: {.cell .markdown id="Fd2NMTuqNTmX"}
# Indexing and Slicing

We can access a single element of an array or a sub-array using the square brackets likewise to the indexing and slicing of Python list.
Moreover, Numpy also supports the Fancy-Indexing and the Boolean-Indexing, for a complete guide see the [official page](https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html).

Example of single element indexing:
:::

::: {.cell .code execution_count="9" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.002432Z\",\"start_time\":\"2019-05-16T13:48:14.868323Z\"}" executionInfo="{\"elapsed\":63,\"status\":\"ok\",\"timestamp\":1740855690815,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="4gn0HGDANTmY"}
``` python
matrix = np.random.rand(5,4)
element = matrix[0,1] # get the element in first row and second column
matrix[2,0] = 5.6     # set the element in third row and first column
```
:::

:::: {.cell .code execution_count="10" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1740855690819,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="F6Y3ngbJAbHP" outputId="c68580d6-dce9-4de0-d5c5-1b6086d247b6"}
``` python
matrix
```

::: {.output .execute_result execution_count="10"}
    array([[0.37950928, 0.3169662 , 0.8268082 , 0.56000652],
           [0.29042958, 0.4113962 , 0.02299949, 0.09832009],
           [5.6       , 0.48237626, 0.29922682, 0.70865825],
           [0.89894296, 0.64898845, 0.24902456, 0.65207568],
           [0.91464907, 0.33893847, 0.39160606, 0.67191685]])
:::
::::

::: {.cell .markdown id="TlApv6_yNTma"}
Example of simple slicing:
:::

::: {.cell .code execution_count="11" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.111229Z\",\"start_time\":\"2019-05-16T13:48:15.005781Z\"}" executionInfo="{\"elapsed\":0,\"status\":\"ok\",\"timestamp\":1740855690819,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="EncPbk1sNTmb"}
``` python
matrix = np.random.rand(5,4)
row = matrix[2,:]   # get the third row
col = matrix[:,-1]  # get the last column
```
:::

:::: {.cell .code execution_count="12" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":6,\"status\":\"ok\",\"timestamp\":1740855690826,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="GWtq0AEaApm-" outputId="c677b765-dd40-4426-d6f2-0b435974fb7c"}
``` python
matrix
```

::: {.output .execute_result execution_count="12"}
    array([[0.82129761, 0.59738565, 0.53846934, 0.21838815],
           [0.87913302, 0.53663752, 0.82818001, 0.26596751],
           [0.38933634, 0.75385764, 0.96764666, 0.86699365],
           [0.00150005, 0.08179629, 0.6741496 , 0.51987686],
           [0.59208825, 0.68168112, 0.58397873, 0.35655196]])
:::
::::

:::: {.cell .code execution_count="13" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":51,\"status\":\"ok\",\"timestamp\":1740855690878,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="bmHVGJB_Ar_N" outputId="cebc2c7c-814a-4501-adf6-f763350c0032"}
``` python
row
```

::: {.output .execute_result execution_count="13"}
    array([0.38933634, 0.75385764, 0.96764666, 0.86699365])
:::
::::

:::: {.cell .code execution_count="14" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":1,\"status\":\"ok\",\"timestamp\":1740855690880,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="W4Q_np9dAtY0" outputId="24ccefd8-07d9-4689-f0ac-c960675a6b62"}
``` python
col
```

::: {.output .execute_result execution_count="14"}
    array([0.21838815, 0.26596751, 0.86699365, 0.51987686, 0.35655196])
:::
::::

::: {.cell .markdown id="vyilOftTNTmf"}
Note that in the previous example the arrays `row` and `col` are the same data type of `matrix` but a different number of dimensions.

Also for the arrays, we can use the syntax `start:stop:step`, for examples:
:::

:::: {.cell .code execution_count="15" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.193730Z\",\"start_time\":\"2019-05-16T13:48:15.114653Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":23,\"status\":\"ok\",\"timestamp\":1740855690916,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="YZVV30UDNTmf" outputId="ce9be3f5-85ac-493d-f412-5dd113107d1c"}
``` python
matrix = np.random.rand(5,4)
a = matrix[:2,:]      # sub-array with the first two rows
b = matrix[1:3,2:4]   # sub-array 2x2
#matrix[:,1:2] = 0     # set to zero the second and third columns
print(matrix)
print(a)
print(b)
```

::: {.output .stream .stdout}
    [[0.71387619 0.34746524 0.84168738 0.82348066]
     [0.75114008 0.35767639 0.59138335 0.92595441]
     [0.40216487 0.96244776 0.9927364  0.07354503]
     [0.64008744 0.08916182 0.29014649 0.13893265]
     [0.2726703  0.77833937 0.57998138 0.78702298]]
    [[0.71387619 0.34746524 0.84168738 0.82348066]
     [0.75114008 0.35767639 0.59138335 0.92595441]]
    [[0.59138335 0.92595441]
     [0.9927364  0.07354503]]
:::
::::

::: {.cell .markdown id="sqPT-otqNTmk"}
# Element-wise operations and functions

Numpy library provides efficient element-wise operations and functions applied across one or more arrays. For examples:

- Arithmetic Operators (`+`, `-`, `*`, `/`, \...)
- Comparisons (`==`, `>`, `!=`, \...)
- Boolean Functions (`np.logical_and( )`, `np.logical_not( )`, \...)
- Math Functions (`np.maximum( )`, `np.exp( )`, `np.sin( )`, \...)
:::

:::: {.cell .code execution_count="16" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.285706Z\",\"start_time\":\"2019-05-16T13:48:15.196995Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":44,\"status\":\"ok\",\"timestamp\":1740855690960,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="l2f0u45aNTmk" outputId="564a7d1b-a4b3-4347-d614-588d698449c5"}
``` python
l1 = [ 4, 5, 1, 3, 4]  # it is a list
a1 = np.array(l1)      # it is an array

l2 = [ 0, 3, 2, 7, 9]  # it is a list
a2 = np.array(l2)      # it is an array

# the sum of two lists is different from the sum of two arrays
print('the sum of the two lists :', l1+l2)
```

::: {.output .stream .stdout}
    the sum of the two lists : [4, 5, 1, 3, 4, 0, 3, 2, 7, 9]
:::
::::

:::: {.cell .code execution_count="17" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":2,\"status\":\"ok\",\"timestamp\":1740855690982,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="8LIr7gNG14Vd" outputId="8db21a32-73c0-4413-8941-44d54233817f"}
``` python
print('the sum of the two arrays:', a1+a2)
```

::: {.output .stream .stdout}
    the sum of the two arrays: [ 4  8  3 10 13]
:::
::::

:::: {.cell .code execution_count="18" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":2,\"status\":\"ok\",\"timestamp\":1740855690984,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="StE0_zkN2I4W" outputId="c3463210-4b38-41df-fcc9-314fc7086694"}
``` python
l1 * 5
```

::: {.output .execute_result execution_count="18"}
    [4, 5, 1, 3, 4, 4, 5, 1, 3, 4, 4, 5, 1, 3, 4, 4, 5, 1, 3, 4, 4, 5, 1, 3, 4]
:::
::::

:::: {.cell .code execution_count="19" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":79,\"status\":\"ok\",\"timestamp\":1740855691063,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="r2toxzsp2WqO" outputId="298df85a-c0a2-48a0-96c5-7e6c5d7e185f"}
``` python
a1 *5
```

::: {.output .execute_result execution_count="19"}
    array([20, 25,  5, 15, 20])
:::
::::

:::: {.cell .code execution_count="20" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.399317Z\",\"start_time\":\"2019-05-16T13:48:15.289894Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":14,\"status\":\"ok\",\"timestamp\":1740855691077,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="jtJgyk9vNTmm" outputId="aa77708f-da93-46ad-9732-bde092dd4f39"}
``` python
a1 = np.array([[4, 5], [1, 3]] ) # fist array
a2 = np.array([[1, 3], [2, 7]] ) # second array

# Some examples of element-wise operations and functions
print('the maximum  of the two arrays:\n', np.maximum(a1, a2) )
print('the prodoct  of the two arrays:\n', a1 * a2) # it is the element-wise prodoct
print('the division of the two arrays:\n', a1 / a2) # it is the element-wise division
print('the floor-division of the two arrays:\n', a1 // a2) # it is the element-wise floor-division
```

::: {.output .stream .stdout}
    the maximum  of the two arrays:
     [[4 5]
     [2 7]]
    the prodoct  of the two arrays:
     [[ 4 15]
     [ 2 21]]
    the division of the two arrays:
     [[4.         1.66666667]
     [0.5        0.42857143]]
    the floor-division of the two arrays:
     [[4 1]
     [0 0]]
:::
::::

::: {.cell .markdown id="BbS2Evt2NTmo"}
# Stacking & Reshaping & Transposing

Numpy provides functions to stack, to reshape and to transpose the arrays.
:::

::: {.cell .markdown id="RiYQknOWNTmo"}
## `np.concatenate(arrays_list, axis)`

joins a list of arrays along an axis.
:::

::: {.cell .code execution_count="21" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.534925Z\",\"start_time\":\"2019-05-16T13:48:15.403344Z\"}" executionInfo="{\"elapsed\":0,\"status\":\"ok\",\"timestamp\":1740855691078,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="zUYllhj_NTmp"}
``` python
a0 = np.array([[1, 2], [3, 4]])  # it is an array 2x2
a1 = np.array([[5, 6]])          # it is an array 1x2
a2 = np.array([[5, ], [6,]])     # it is an array 2x1
```
:::

:::: {.cell .code execution_count="22" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":33,\"status\":\"ok\",\"timestamp\":1740855691112,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="M4Eo0XVp3Ps3" outputId="ad20c163-eb58-4491-e85f-fa84bd9b4a79"}
``` python
#print('matrix "a0":\n', a0)
print('shape of "a0":', a0.shape)
#print('matrix "a1":\n', a1)
print('shape of "a1":', a1.shape)
#print('matrix "a2":\n', a2)
print('shape of "a2":', a2.shape)
print()
```

::: {.output .stream .stdout}
    shape of "a0": (2, 2)
    shape of "a1": (1, 2)
    shape of "a2": (2, 1)
:::
::::

:::: {.cell .code execution_count="23" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":162}" executionInfo="{\"elapsed\":11,\"status\":\"error\",\"timestamp\":1740855691127,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="9pl9l3B_CavR" outputId="9248c98e-5f37-48fd-a722-2dc177309c07"}
``` python
np.concatenate([a0,a1], 1).shape
```

::: {.output .error ename="ValueError" evalue="all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1"}
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-23-5598f0215fd3> in <cell line: 0>()
    ----> 1 np.concatenate([a0,a1], 1).shape

    ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1
:::
::::

:::: {.cell .code execution_count="24" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":29,\"status\":\"ok\",\"timestamp\":1740855709432,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="tYAkYptPFC5R" outputId="846f884e-bbb3-48ce-8833-3a50841a7388"}
``` python
# Concatenation along the rows
b = np.concatenate([a0,a1], 0) # it is an array 3x2
print('matrix  "b":\n', b)
print('shape of  "b"', b.shape)
```

::: {.output .stream .stdout}
    matrix  "b":
     [[1 2]
     [3 4]
     [5 6]]
    shape of  "b" (3, 2)
:::
::::

:::: {.cell .code execution_count="25" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":122,\"status\":\"ok\",\"timestamp\":1740855709542,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="xTBV2oUUFHpI" outputId="768f40e7-2f73-44ee-f3f4-a914493b65d3"}
``` python
# Concatenation along the columns
c = np.concatenate([a0,a2], 1) # it is an array 2x3
print('matrix  "c":\n',c)
print('shape of  "c"', c.shape)
```

::: {.output .stream .stdout}
    matrix  "c":
     [[1 2 5]
     [3 4 6]]
    shape of  "c" (2, 3)
:::
::::

::: {.cell .markdown id="Yyw4-AlINTmr"}
## `np.stack(arrays_list, axis)`

joins a list of arrays along a new axis. if axis=0 the new axis is created at the beginning while if axis=-1 the new axis is created at the end.
:::

:::: {.cell .code execution_count="26" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.634604Z\",\"start_time\":\"2019-05-16T13:48:15.539077Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":37,\"status\":\"ok\",\"timestamp\":1740855709542,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="aQbv0ymHNTmr" outputId="30273e4d-fd10-48a8-cd9a-4134af264f18"}
``` python
a0 = np.array([[1, 2, 4], [3, 4, 8]])  # it is a matrix 2x3
a1 = np.array([[5, 6, 7], [5, 7, 9]])  # it is a matrix 2x3
print('matrix "a0":\n', a0)
print('shape of "a0":', a0.shape)
print('matrix "a1":\n', a1)
print('shape of "a1":', a1.shape)
print()

# stacking
b = np.stack([a0,a1],0)      # it is an array 2x2x3
print('array  "b":\n', b)
print('shape of  "b"', b.shape)

# stacking
c = np.stack([a0,a1], -1)   # it is an array 2x3x2
print('array  "c":\n', c)
print('shape of  "c"', c.shape)
```

::: {.output .stream .stdout}
    matrix "a0":
     [[1 2 4]
     [3 4 8]]
    shape of "a0": (2, 3)
    matrix "a1":
     [[5 6 7]
     [5 7 9]]
    shape of "a1": (2, 3)

    array  "b":
     [[[1 2 4]
      [3 4 8]]

     [[5 6 7]
      [5 7 9]]]
    shape of  "b" (2, 2, 3)
    array  "c":
     [[[1 5]
      [2 6]
      [4 7]]

     [[3 5]
      [4 7]
      [8 9]]]
    shape of  "c" (2, 3, 2)
:::
::::

::: {.cell .markdown id="E3TvTtK6NTmt"}
## `np.reshape(array, newshape, order='C')`

modifies the shape to the array without changing its data.
:::

:::: {.cell .code execution_count="27" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.739227Z\",\"start_time\":\"2019-05-16T13:48:15.637619Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":15,\"status\":\"ok\",\"timestamp\":1740855709543,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="-g6CVfE8NTmu" outputId="4845543a-9e2e-425b-a78b-6395f41ead10"}
``` python
vector = np.random.rand(12)
matrix = np.reshape(vector, (4,3))

print("vector:\n", vector)
print("matrix:\n", matrix)

# "vector" and "matrix" have same data but different shapes
```

::: {.output .stream .stdout}
    vector:
     [0.54491255 0.37361058 0.94231831 0.64855749 0.5724887  0.94300513
     0.00785319 0.30131814 0.89610937 0.32893149 0.64593977 0.51779159]
    matrix:
     [[0.54491255 0.37361058 0.94231831]
     [0.64855749 0.5724887  0.94300513]
     [0.00785319 0.30131814 0.89610937]
     [0.32893149 0.64593977 0.51779159]]
:::
::::

::: {.cell .markdown id="21WLS69INTmw"}
Note, by default the reshape follows the C-like index order (the rows of the matrix are placed in contiguous indexes like in C/C++).

While, executing the reshape with `order='F'`, it follows the F-like index order (the columns of the matrix are placed in contiguous indexes like in Fortran and Matlab).
:::

:::: {.cell .code execution_count="28" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.821275Z\",\"start_time\":\"2019-05-16T13:48:15.742384Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":9,\"status\":\"ok\",\"timestamp\":1740855709543,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="qfW0HcePNTmw" outputId="8055ac8f-b7bd-4bee-e443-26606c16bdd6"}
``` python
matrixF = np.reshape(vector, (4,3), order='F')

print("matrix in C-like order:\n", matrix)
print("matrix in F-like order:\n", matrixF)
```

::: {.output .stream .stdout}
    matrix in C-like order:
     [[0.54491255 0.37361058 0.94231831]
     [0.64855749 0.5724887  0.94300513]
     [0.00785319 0.30131814 0.89610937]
     [0.32893149 0.64593977 0.51779159]]
    matrix in F-like order:
     [[0.54491255 0.5724887  0.89610937]
     [0.37361058 0.94300513 0.32893149]
     [0.94231831 0.00785319 0.64593977]
     [0.64855749 0.30131814 0.51779159]]
:::
::::

::: {.cell .markdown id="I7_lL6MWNTm0"}
## `np.transpose(array, axes)`

swaps the dimensions of the array.
:::

:::: {.cell .code execution_count="29" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:15.934783Z\",\"start_time\":\"2019-05-16T13:48:15.825420Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":7,\"status\":\"ok\",\"timestamp\":1740855709543,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="ZLhzgJJpNTm1" outputId="d9e149f6-30c2-4ea1-dda5-1ad48fee79be"}
``` python
# transpose of a matrix
matrix = np.random.rand(4,3)  # a bidimensional matrix

# swap the first dimension with the second one
matrixT = np.transpose(matrix, (1,0) )

print("original  matrix:\n", matrix)
print("shape of original  matrix:", matrix.shape)
print()

print("transpose matrix:\n", matrixT)
print("shape of transpose matrix:", matrixT.shape)
print()
```

::: {.output .stream .stdout}
    original  matrix:
     [[0.13850847 0.82657347 0.54251056]
     [0.27778697 0.88733815 0.2269697 ]
     [0.2218252  0.24697658 0.26079171]
     [0.31624    0.34332581 0.88367972]]
    shape of original  matrix: (4, 3)

    transpose matrix:
     [[0.13850847 0.27778697 0.2218252  0.31624   ]
     [0.82657347 0.88733815 0.24697658 0.34332581]
     [0.54251056 0.2269697  0.26079171 0.88367972]]
    shape of transpose matrix: (3, 4)
:::
::::

:::: {.cell .code execution_count="30" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:16.037644Z\",\"start_time\":\"2019-05-16T13:48:15.938881Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":7,\"status\":\"ok\",\"timestamp\":1740855709550,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="Ti6LbKWtNTm4" outputId="6f982bc1-8d86-48de-8853-c613c63a96ae"}
``` python
# transpose of a multidimensional array
array = np.random.rand(4,2,3)  # an array with three dimensions

# swap the first dimension with the third one
arrayT = np.transpose(array, (2,1,0) )

print("original  array:\n", array)
print("shape of original  array:", array.shape)
print()

print("transpose array:\n", arrayT)
print("shape of transpose array:", arrayT.shape)
print()
```

::: {.output .stream .stdout}
    original  array:
     [[[0.55280628 0.13880707 0.0035281 ]
      [0.00762383 0.34147241 0.79701965]]

     [[0.38851737 0.68062808 0.9149975 ]
      [0.85162365 0.18589959 0.47172847]]

     [[0.83671065 0.14289811 0.4833691 ]
      [0.31279526 0.80195352 0.46629634]]

     [[0.22065761 0.23269435 0.30908528]
      [0.73552358 0.80072914 0.33074079]]]
    shape of original  array: (4, 2, 3)

    transpose array:
     [[[0.55280628 0.38851737 0.83671065 0.22065761]
      [0.00762383 0.85162365 0.31279526 0.73552358]]

     [[0.13880707 0.68062808 0.14289811 0.23269435]
      [0.34147241 0.18589959 0.80195352 0.80072914]]

     [[0.0035281  0.9149975  0.4833691  0.30908528]
      [0.79701965 0.47172847 0.46629634 0.33074079]]]
    shape of transpose array: (3, 2, 4)
:::
::::

::: {.cell .markdown id="8gPUquNmNTm6"}
# Reductions

Numpy provides functions to \"aggregate\" our data along a particular axis or the whole array, such as `np.sum( )`, `np.mean( )`, `np.var( )`, `np.median( )`, `np.min( )`, `np.max( )`.
:::

:::: {.cell .code execution_count="31" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:16.128080Z\",\"start_time\":\"2019-05-16T13:48:16.041412Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":11,\"status\":\"ok\",\"timestamp\":1740855709561,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="HhxLVZpLNTm6" outputId="df9eba30-2eae-41db-bd29-9d7a968eb0d2"}
``` python
a1 = np.array([[4.4, 5.0], [1.0, 3.2], [1.7, 2.4]] )  # array 3x2

print("sum of the whole array:", np.sum(a1) )
print("sum of the array along the columns:", np.sum(a1, axis=0) )
print("sum of the array along the rows:", np.sum(a1, 1) )
```

::: {.output .stream .stdout}
    sum of the whole array: 17.7
    sum of the array along the columns: [ 7.1 10.6]
    sum of the array along the rows: [9.4 4.2 4.1]
:::
::::

::: {.cell .markdown id="tfPnYmnRNTm9"}
The other functions to \"aggregate\" have the same syntax.
:::

::: {.cell .markdown id="z6HlrPQsNTm9"}
# Save & Load

To save and load an array, we can use the functions `np.save( )` and `np.load( )`.
:::

:::: {.cell .code execution_count="32" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":23036,\"status\":\"ok\",\"timestamp\":1740855732598,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="_N2K96XW66wG" outputId="8db08477-72df-4a92-d0df-8f39c4206b69"}
``` python
from google.colab import drive
drive.mount('/content/drive')
```

::: {.output .stream .stdout}
    Mounted at /content/drive
:::
::::

:::: {.cell .code execution_count="33" ExecuteTime="{\"end_time\":\"2019-05-16T13:48:16.281600Z\",\"start_time\":\"2019-05-16T13:48:16.132191Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1740855732601,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="EjB8hR4SNTm-" outputId="ad880c3f-644a-4a4f-b665-790826e6549f"}
``` python
a1 = np.array([[4.4, 5.0], [1.0, 3.2], [1.7, 2.4]] )  # array 3x2

np.save("/content/drive/MyDrive/array_file.npy", a1)

del a1

a1 = np.load("/content/drive/MyDrive/array_file.npy")
print(a1)

```

::: {.output .stream .stdout}
    [[4.4 5. ]
     [1.  3.2]
     [1.7 2.4]]
:::
::::

::: {.cell .markdown id="FQ2UI6bRNTnA"}
File extension used by Numpy to store an array is `.npy`
:::
