---
jupyter:
  colab:
  kernelspec:
    display_name: Python 3
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

::: {.cell .markdown id="xAnkEpDbNbpx"}
# Opening an image using `PIL` package

The `PIL` package provides functions for opening, manipulating, and saving many different image file formats.
In the following, there is an example:
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:41.505711Z\",\"start_time\":\"2019-05-16T15:00:41.248685Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":873,\"status\":\"ok\",\"timestamp\":1740855784314,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="vkyzgugkNbpy" outputId="c82fb6a6-9b02-4c48-c584-738cd8106cec"}
``` python
# at first, download 'lena.jpg' from web
import requests
response = requests.get("http://ndevilla.free.fr/lena/lena.jpg")
open("lena.jpg", "wb").write(response.content)
```

::: {.output .execute_result execution_count="1"}
    20401
:::
::::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:41.728532Z\",\"start_time\":\"2019-05-16T15:00:41.508955Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":29,\"status\":\"ok\",\"timestamp\":1740855784331,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="jYC2Rc-4Nbp1" outputId="37603ec6-035a-4ea7-ab99-fb7b0cc20bd4"}
``` python
import numpy as np     # import Numpy
from PIL import Image  # import the 'Image' module from the 'PIL' package

# Open the image
img = Image.open('lena.jpg')  # this is an object of 'Image' type defined in the 'PIL' package

# Convert the object of 'Image' type into a Numpy array
array = np.asarray(img)

print('shape of the image:', array.shape)
```

::: {.output .stream .stdout}
    shape of the image: (256, 256, 3)
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":43,\"status\":\"ok\",\"timestamp\":1740855784375,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="i65SvuF69_o9" outputId="4cd2f371-3083-40af-8429-9111931cfe73"}
``` python
vars(img)
```

::: {.output .execute_result execution_count="3"}
    {'_im': <ImagingCore at 0x7b50838ee2b0>,
     '_mode': 'RGB',
     '_size': (256, 256),
     'palette': None,
     'info': {'jfif': 258,
      'jfif_version': (1, 2),
      'dpi': (72, 72),
      'jfif_unit': 1,
      'jfif_density': (72, 72),
      'adobe': 100,
      'adobe_transform': 1},
     'readonly': 0,
     '_exif': None,
     '_min_frame': 0,
     'custom_mimetype': None,
     'tile': [],
     'decoderconfig': (),
     'decodermaxblock': 65536,
     'fp': None,
     'filename': 'lena.jpg',
     '_exclusive_fp': True,
     'bits': 8,
     'layers': 3,
     '_exif_offset': 0,
     'layer': [(1, 2, 2, 0), (2, 1, 1, 1), (3, 1, 1, 1)],
     '_huffman_dc': {},
     '_huffman_ac': {},
     'quantization': {0: [4,
       2,
       2,
       3,
       5,
       7,
       10,
       13,
       3,
       3,
       3,
       4,
       6,
       10,
       13,
       13,
       3,
       3,
       4,
       5,
       8,
       12,
       15,
       16,
       4,
       4,
       5,
       6,
       12,
       15,
       17,
       18,
       5,
       5,
       8,
       12,
       14,
       17,
       20,
       21,
       7,
       10,
       12,
       15,
       17,
       21,
       21,
       21,
       10,
       13,
       16,
       18,
       21,
       21,
       21,
       21,
       14,
       16,
       19,
       21,
       21,
       21,
       21,
       21],
      1: [4,
       4,
       5,
       5,
       7,
       10,
       12,
       13,
       4,
       4,
       5,
       7,
       10,
       14,
       17,
       21,
       5,
       5,
       6,
       12,
       15,
       17,
       21,
       21,
       5,
       7,
       12,
       16,
       19,
       21,
       21,
       21,
       8,
       10,
       15,
       19,
       21,
       21,
       21,
       21,
       10,
       14,
       17,
       21,
       21,
       21,
       21,
       21,
       13,
       17,
       21,
       21,
       21,
       21,
       21,
       21,
       15,
       21,
       21,
       21,
       21,
       21,
       21,
       21]},
     'app': {'APP0': b'JFIF\x00\x01\x02\x01\x00H\x00H\x00\x00',
      'APP13': b"Adobe_Photoshop2.5:\x00H\x00\x00\x00H\x00\x008BIM\x03\xe9\x00\x00\x00\x00\x00x\x00\x08\x00\x00\x00H\x00H\x00\x00\x00\x00\x02\xdb\x02@\xff\xe7\xff\xee\x02\xff\x02R\x1f\x03\x05(\x03\xfc\x00\x01\x00\x00\x01,\x01,\x00\x00\x00\x00\x0b\xe7\t`\x01,\x00-\x05\xa0^\xec\x00&\x02\x01\x01\x01\x00\x18\x00\x01'\x0f\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x02\x04\x05\x00\x00\x00\x008BIM\x03\xed\x00\x00\x00\x00\x00\x10\x00H\x00\x00\x00\x01\x00\x01\x00H\x00\x00\x00\x01\x00\x018BIM\x03\xf3\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x008BIM\x03\xf5\x00\x00\x00\x00\x00H\x00/ff\x00\x01\x00lff\x00\x00\x00\x00\x00\x00\x00\x00\x00/ff\x00\x01\x00\xa1\x99\x99\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x01\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005\x00\x00\x00\x01\x00-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008BIM\x03\xf8\x00\x00\x00\x00\x00p\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00",
      'APP14': b'Adobe\x00d\x80\x00\x00\x00\x01'},
     'applist': [('APP0', b'JFIF\x00\x01\x02\x01\x00H\x00H\x00\x00'),
      ('APP13',
       b"Adobe_Photoshop2.5:\x00H\x00\x00\x00H\x00\x008BIM\x03\xe9\x00\x00\x00\x00\x00x\x00\x08\x00\x00\x00H\x00H\x00\x00\x00\x00\x02\xdb\x02@\xff\xe7\xff\xee\x02\xff\x02R\x1f\x03\x05(\x03\xfc\x00\x01\x00\x00\x01,\x01,\x00\x00\x00\x00\x0b\xe7\t`\x01,\x00-\x05\xa0^\xec\x00&\x02\x01\x01\x01\x00\x18\x00\x01'\x0f\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x04\x02\x04\x05\x00\x00\x00\x008BIM\x03\xed\x00\x00\x00\x00\x00\x10\x00H\x00\x00\x00\x01\x00\x01\x00H\x00\x00\x00\x01\x00\x018BIM\x03\xf3\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x008BIM\x03\xf5\x00\x00\x00\x00\x00H\x00/ff\x00\x01\x00lff\x00\x00\x00\x00\x00\x00\x00\x00\x00/ff\x00\x01\x00\xa1\x99\x99\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x01\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005\x00\x00\x00\x01\x00-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008BIM\x03\xf8\x00\x00\x00\x00\x00p\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x03\xe8\x00\x00"),
      ('APP14', b'Adobe\x00d\x80\x00\x00\x00\x01')],
     'icclist': [],
     'map': None}
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":6,\"status\":\"ok\",\"timestamp\":1740855784381,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="r8eajsh5_tPy" outputId="bf632975-292f-4e6d-8dba-8519c8863da5"}
``` python
array[:3,:3,0]
```

::: {.output .execute_result execution_count="4"}
    array([[225, 225, 226],
           [225, 225, 225],
           [227, 227, 227]], dtype=uint8)
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":41,\"status\":\"ok\",\"timestamp\":1740855784423,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="S1j_8hPKAEEC" outputId="82b3d29d-066c-4d70-ad35-7f119f08a83a"}
``` python
array[-3:,-3:,0]
```

::: {.output .execute_result execution_count="5"}
    array([[144, 155, 159],
           [155, 164, 165],
           [164, 174, 177]], dtype=uint8)
:::
::::

::: {.cell .code id="_aJgHsmiA8-I"}
``` python
array = array.astype("float")
```
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:41.733218Z\",\"start_time\":\"2019-05-16T15:00:41.730556Z\"}" id="B-_2BH2SNbp5"}
``` python
# Modify the array
array = array + 30
```
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":17,\"status\":\"ok\",\"timestamp\":1740855784526,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="oZ_U_8vrvOtL" outputId="ce877684-faee-47ee-9a30-60507f9acd96"}
``` python
array > 255
```

::: {.output .execute_result execution_count="8"}
    array([[[False, False, False],
            [False, False, False],
            [ True, False, False],
            ...,
            [ True, False, False],
            [ True, False, False],
            [False, False, False]],

           [[False, False, False],
            [False, False, False],
            [False, False, False],
            ...,
            [ True, False, False],
            [ True, False, False],
            [False, False, False]],

           [[ True, False, False],
            [ True, False, False],
            [ True, False, False],
            ...,
            [False, False, False],
            [False, False, False],
            [False, False, False]],

           ...,

           [[False, False, False],
            [False, False, False],
            [False, False, False],
            ...,
            [False, False, False],
            [False, False, False],
            [False, False, False]],

           [[False, False, False],
            [False, False, False],
            [False, False, False],
            ...,
            [False, False, False],
            [False, False, False],
            [False, False, False]],

           [[False, False, False],
            [False, False, False],
            [False, False, False],
            ...,
            [False, False, False],
            [False, False, False],
            [False, False, False]]])
:::
::::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:41.847523Z\",\"start_time\":\"2019-05-16T15:00:41.735002Z\"}" id="3HQF1U2pNbp7"}
``` python
# Convert the Numpy array into an object of 'Image' type

array[array > 255] = 255
array = array.astype("uint8")
img = Image.fromarray(array)

# Save the image
img.save('lena_mod.png')
```
:::

::: {.cell .markdown id="QAbVexCbNbp9"}
# Graphics using `matplotlib` package

Matplotlib is an easy graphics library for generating scientific figures (e.g. plots, scatters, histograms). The generated figures can be stored in many formats, including PNG, PDF, SVG, EPS.
More information at the official web site <http://matplotlib.org>

We will use the `matplotlib.pyplot` module that provides a MATLAB-like set of functions. It is easy to use if you are familiar with MATLAB.
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:42.187187Z\",\"start_time\":\"2019-05-16T15:00:41.849404Z\"}" id="uoEq4JAeNbp-"}
``` python
%matplotlib inline
import matplotlib.pyplot as plt
```
:::

::: {.cell .markdown id="k81b6UhHVSpK"}
The statement \"`%matplotlib inline`\" specifies that the figures created using matplotlib are displayed in the notebook as the output of the cell.
:::

::: {.cell .markdown ExecuteTime="{\"end_time\":\"2019-05-12T11:11:17.902194Z\",\"start_time\":\"2019-05-12T11:11:17.895069Z\"}" id="uIfp3DQYNbqA"}
### Example of Plot
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:42.192738Z\",\"start_time\":\"2019-05-16T15:00:42.189377Z\"}" id="Te7t1b0JNbqA" run_control="{\"marked\":false}"}
``` python
# create the data to plot
import numpy as np
x = np.arange(0, 5, 0.1)
y = x ** 2
```
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:42.356320Z\",\"start_time\":\"2019-05-16T15:00:42.194632Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":487}" executionInfo="{\"elapsed\":307,\"status\":\"ok\",\"timestamp\":1740855784841,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="Q56UMDN3NbqC" outputId="72f25ef5-7c42-4978-b675-8a4f89f3248b"}
``` python
# create the figure
fig = plt.figure(figsize=(5, 5))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('title')
plt.grid(True)
```

::: {.output .display_data}
![](2718079c7e750aece88e7cc6627af766a778d6ad.png)
:::
::::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:42.597860Z\",\"start_time\":\"2019-05-16T15:00:42.557032Z\"}" id="APSyetP6NbqI"}
``` python
# the figure can be saved using the `.savefig()` method
fig.savefig("filename.png")
```
:::

::: {.cell .markdown id="rBnqmCFENbqK"}
### Example of image show
:::

::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:42.636654Z\",\"start_time\":\"2019-05-16T15:00:42.599666Z\"}" id="6As-ZGTeNbqK"}
``` python
# import modules
import numpy as np
from PIL import Image

# Open the image
img = np.asarray(Image.open('lena.jpg'))
```
:::

:::: {.cell .code ExecuteTime="{\"end_time\":\"2019-05-16T15:00:42.927611Z\",\"start_time\":\"2019-05-16T15:00:42.638453Z\"}" colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":468}" executionInfo="{\"elapsed\":953,\"status\":\"ok\",\"timestamp\":1740855785834,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="6owchDunNbqN" outputId="8bd7729f-11d9-4893-de3d-625ec5ae44d8"}
``` python
# create the figure
fig = plt.figure(figsize=(5, 5))
plt.imshow(img)
plt.title('image')
plt.grid(False)
```

::: {.output .display_data}
![](336c870d2101410eb3078d4f5d138794b67f509e.png)
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":468}" executionInfo="{\"elapsed\":238,\"status\":\"ok\",\"timestamp\":1740855786075,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="zINMhOknNU4i" outputId="55ab1fdc-d13b-4564-d36b-80ef344fe52d"}
``` python
# import modules
import numpy as np
from PIL import Image

# Open the image
img = np.asarray(Image.open('lena_mod.png'))

# create the figure
fig = plt.figure(figsize=(5, 5))
plt.imshow(img)
plt.title('image')
plt.grid(False)
```

::: {.output .display_data}
![](24d3cd5f0a67d9b047e1f6965498d2fe97ec643a.png)
:::
::::

::: {.cell .markdown id="fWUaSJhaNbqP"}
# Some functions in `os` package

The standard `os` package provides functions for interacting with the operating system. In particular, the `os.path` module contains some useful functions on pathnames, such as:

- `os.path.isfile(filepath)` returns True if filepath is an existing file.
- `os.path.basename(filepath)` is used to obtain the name of the file from the whole filepath.
- `os.path.dirname(filepath)` is used to obtain the directory name from the filepath.
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":69,\"status\":\"ok\",\"timestamp\":1740855786146,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="eeELx7uCT1Vk" outputId="b0147737-e272-41c2-d8b2-1680e0e969ed"}
``` python
import os
help(os)
```

::: {.output .stream .stdout}
    Help on module os:

    NAME
        os - OS routines for NT or Posix depending on what system we're on.

    MODULE REFERENCE
        https://docs.python.org/3.11/library/os.html
        
        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.

    DESCRIPTION
        This exports:
          - all functions from posix or nt, e.g. unlink, stat, etc.
          - os.path is either posixpath or ntpath
          - os.name is either 'posix' or 'nt'
          - os.curdir is a string representing the current directory (always '.')
          - os.pardir is a string representing the parent directory (always '..')
          - os.sep is the (or a most common) pathname separator ('/' or '\\')
          - os.extsep is the extension separator (always '.')
          - os.altsep is the alternate pathname separator (None or '/')
          - os.pathsep is the component separator used in $PATH etc
          - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
          - os.defpath is the default search path for executables
          - os.devnull is the file path of the null device ('/dev/null', etc.)
        
        Programs that import and use 'os' stand a better chance of being
        portable between different platforms.  Of course, they must then
        only use functions that are defined by all platforms (e.g., unlink
        and opendir), and leave all pathname manipulation to os.path
        (e.g., split and join).

    CLASSES
        builtins.Exception(builtins.BaseException)
            builtins.OSError
        builtins.object
            posix.DirEntry
        builtins.tuple(builtins.object)
            stat_result
            statvfs_result
            terminal_size
            posix.sched_param
            posix.times_result
            posix.uname_result
            posix.waitid_result
        
        class DirEntry(builtins.object)
         |  Methods defined here:
         |  
         |  __fspath__(self, /)
         |      Returns the path for the entry.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  inode(self, /)
         |      Return inode of the entry; cached per entry.
         |  
         |  is_dir(self, /, *, follow_symlinks=True)
         |      Return True if the entry is a directory; cached per entry.
         |  
         |  is_file(self, /, *, follow_symlinks=True)
         |      Return True if the entry is a file; cached per entry.
         |  
         |  is_symlink(self, /)
         |      Return True if the entry is a symbolic link; cached per entry.
         |  
         |  stat(self, /, *, follow_symlinks=True)
         |      Return stat_result object for the entry; cached per entry.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |  
         |  __class_getitem__(...)
         |      See PEP 585
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  name
         |      the entry's base filename, relative to scandir() "path" argument
         |  
         |  path
         |      the entry's full path name; equivalent to os.path.join(scandir_path, entry.name)
        
        error = class OSError(Exception)
         |  Base class for I/O related errors.
         |  
         |  Method resolution order:
         |      OSError
         |      Exception
         |      BaseException
         |      object
         |  
         |  Built-in subclasses:
         |      BlockingIOError
         |      ChildProcessError
         |      ConnectionError
         |      FileExistsError
         |      ... and 7 other subclasses
         |  
         |  Methods defined here:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  characters_written
         |  
         |  errno
         |      POSIX exception code
         |  
         |  filename
         |      exception filename
         |  
         |  filename2
         |      second exception filename
         |  
         |  strerror
         |      exception strerror
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from BaseException:
         |  
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |  
         |  __setstate__(...)
         |  
         |  add_note(...)
         |      Exception.add_note(note) --
         |      add a note to the exception
         |  
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from BaseException:
         |  
         |  __cause__
         |      exception cause
         |  
         |  __context__
         |      exception context
         |  
         |  __dict__
         |  
         |  __suppress_context__
         |  
         |  __traceback__
         |  
         |  args
        
        class sched_param(builtins.tuple)
         |  sched_param(sched_priority)
         |  
         |  Currently has only one field: sched_priority
         |  
         |  sched_priority
         |    A scheduling parameter.
         |  
         |  Method resolution order:
         |      sched_param
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  sched_priority
         |      the scheduling priority
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __match_args__ = ('sched_priority',)
         |  
         |  n_fields = 1
         |  
         |  n_sequence_fields = 1
         |  
         |  n_unnamed_fields = 0
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __getnewargs__(self, /)
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from builtins.tuple:
         |  
         |  __class_getitem__(...)
         |      See PEP 585
        
        class stat_result(builtins.tuple)
         |  stat_result(iterable=(), /)
         |  
         |  stat_result: Result from stat, fstat, or lstat.
         |  
         |  This object may be accessed either as a tuple of
         |    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
         |  or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
         |  
         |  Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
         |  or st_flags, they are available as attributes only.
         |  
         |  See os.stat for more information.
         |  
         |  Method resolution order:
         |      stat_result
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  st_atime
         |      time of last access
         |  
         |  st_atime_ns
         |      time of last access in nanoseconds
         |  
         |  st_blksize
         |      blocksize for filesystem I/O
         |  
         |  st_blocks
         |      number of blocks allocated
         |  
         |  st_ctime
         |      time of last change
         |  
         |  st_ctime_ns
         |      time of last change in nanoseconds
         |  
         |  st_dev
         |      device
         |  
         |  st_gid
         |      group ID of owner
         |  
         |  st_ino
         |      inode
         |  
         |  st_mode
         |      protection bits
         |  
         |  st_mtime
         |      time of last modification
         |  
         |  st_mtime_ns
         |      time of last modification in nanoseconds
         |  
         |  st_nlink
         |      number of hard links
         |  
         |  st_rdev
         |      device type (if inode device)
         |  
         |  st_size
         |      total size, in bytes
         |  
         |  st_uid
         |      user ID of owner
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __match_args__ = ('st_mode', 'st_ino', 'st_dev', 'st_nlink', 'st_uid',...
         |  
         |  n_fields = 19
         |  
         |  n_sequence_fields = 10
         |  
         |  n_unnamed_fields = 3
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __getnewargs__(self, /)
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from builtins.tuple:
         |  
         |  __class_getitem__(...)
         |      See PEP 585
        
        class statvfs_result(builtins.tuple)
         |  statvfs_result(iterable=(), /)
         |  
         |  statvfs_result: Result from statvfs or fstatvfs.
         |  
         |  This object may be accessed either as a tuple of
         |    (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
         |  or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
         |  
         |  See os.statvfs for more information.
         |  
         |  Method resolution order:
         |      statvfs_result
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  f_bavail
         |  
         |  f_bfree
         |  
         |  f_blocks
         |  
         |  f_bsize
         |  
         |  f_favail
         |  
         |  f_ffree
         |  
         |  f_files
         |  
         |  f_flag
         |  
         |  f_frsize
         |  
         |  f_fsid
         |  
         |  f_namemax
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __match_args__ = ('f_bsize', 'f_frsize', 'f_blocks', 'f_bfree', 'f_bav...
         |  
         |  n_fields = 11
         |  
         |  n_sequence_fields = 10
         |  
         |  n_unnamed_fields = 0
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __getnewargs__(self, /)
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from builtins.tuple:
         |  
         |  __class_getitem__(...)
         |      See PEP 585
        
        class terminal_size(builtins.tuple)
         |  terminal_size(iterable=(), /)
         |  
         |  A tuple of (columns, lines) for holding terminal window size
         |  
         |  Method resolution order:
         |      terminal_size
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  columns
         |      width of the terminal window in characters
         |  
         |  lines
         |      height of the terminal window in characters
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __match_args__ = ('columns', 'lines')
         |  
         |  n_fields = 2
         |  
         |  n_sequence_fields = 2
         |  
         |  n_unnamed_fields = 0
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __getnewargs__(self, /)
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from builtins.tuple:
         |  
         |  __class_getitem__(...)
         |      See PEP 585
        
        class times_result(builtins.tuple)
         |  times_result(iterable=(), /)
         |  
         |  times_result: Result from os.times().
         |  
         |  This object may be accessed either as a tuple of
         |    (user, system, children_user, children_system, elapsed),
         |  or via the attributes user, system, children_user, children_system,
         |  and elapsed.
         |  
         |  See os.times for more information.
         |  
         |  Method resolution order:
         |      times_result
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  children_system
         |      system time of children
         |  
         |  children_user
         |      user time of children
         |  
         |  elapsed
         |      elapsed time since an arbitrary point in the past
         |  
         |  system
         |      system time
         |  
         |  user
         |      user time
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __match_args__ = ('user', 'system', 'children_user', 'children_system'...
         |  
         |  n_fields = 5
         |  
         |  n_sequence_fields = 5
         |  
         |  n_unnamed_fields = 0
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __getnewargs__(self, /)
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from builtins.tuple:
         |  
         |  __class_getitem__(...)
         |      See PEP 585
        
        class uname_result(builtins.tuple)
         |  uname_result(iterable=(), /)
         |  
         |  uname_result: Result from os.uname().
         |  
         |  This object may be accessed either as a tuple of
         |    (sysname, nodename, release, version, machine),
         |  or via the attributes sysname, nodename, release, version, and machine.
         |  
         |  See os.uname for more information.
         |  
         |  Method resolution order:
         |      uname_result
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  machine
         |      hardware identifier
         |  
         |  nodename
         |      name of machine on network (implementation-defined)
         |  
         |  release
         |      operating system release
         |  
         |  sysname
         |      operating system name
         |  
         |  version
         |      operating system version
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __match_args__ = ('sysname', 'nodename', 'release', 'version', 'machin...
         |  
         |  n_fields = 5
         |  
         |  n_sequence_fields = 5
         |  
         |  n_unnamed_fields = 0
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __getnewargs__(self, /)
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from builtins.tuple:
         |  
         |  __class_getitem__(...)
         |      See PEP 585
        
        class waitid_result(builtins.tuple)
         |  waitid_result(iterable=(), /)
         |  
         |  waitid_result: Result from waitid.
         |  
         |  This object may be accessed either as a tuple of
         |    (si_pid, si_uid, si_signo, si_status, si_code),
         |  or via the attributes si_pid, si_uid, and so on.
         |  
         |  See os.waitid for more information.
         |  
         |  Method resolution order:
         |      waitid_result
         |      builtins.tuple
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __reduce__(...)
         |      Helper for pickle.
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs)
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  si_code
         |  
         |  si_pid
         |  
         |  si_signo
         |  
         |  si_status
         |  
         |  si_uid
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  __match_args__ = ('si_pid', 'si_uid', 'si_signo', 'si_status', 'si_cod...
         |  
         |  n_fields = 5
         |  
         |  n_sequence_fields = 5
         |  
         |  n_unnamed_fields = 0
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.tuple:
         |  
         |  __add__(self, value, /)
         |      Return self+value.
         |  
         |  __contains__(self, key, /)
         |      Return key in self.
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __getnewargs__(self, /)
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __mul__(self, value, /)
         |      Return self*value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  __rmul__(self, value, /)
         |      Return value*self.
         |  
         |  count(self, value, /)
         |      Return number of occurrences of value.
         |  
         |  index(self, value, start=0, stop=9223372036854775807, /)
         |      Return first index of value.
         |      
         |      Raises ValueError if the value is not present.
         |  
         |  ----------------------------------------------------------------------
         |  Class methods inherited from builtins.tuple:
         |  
         |  __class_getitem__(...)
         |      See PEP 585

    FUNCTIONS
        WCOREDUMP(status, /)
            Return True if the process returning status was dumped to a core file.
        
        WEXITSTATUS(status)
            Return the process return code from status.
        
        WIFCONTINUED(status)
            Return True if a particular process was continued from a job control stop.
            
            Return True if the process returning status was continued from a
            job control stop.
        
        WIFEXITED(status)
            Return True if the process returning status exited via the exit() system call.
        
        WIFSIGNALED(status)
            Return True if the process returning status was terminated by a signal.
        
        WIFSTOPPED(status)
            Return True if the process returning status was stopped.
        
        WSTOPSIG(status)
            Return the signal that stopped the process that provided the status value.
        
        WTERMSIG(status)
            Return the signal that terminated the process that provided the status value.
        
        _exit(status)
            Exit to the system with specified status, without normal exit processing.
        
        abort()
            Abort the interpreter immediately.
            
            This function 'dumps core' or otherwise fails in the hardest way possible
            on the hosting operating system.  This function never returns.
        
        access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)
            Use the real uid/gid to test for access to a path.
            
              path
                Path to be tested; can be string, bytes, or a path-like object.
              mode
                Operating-system mode bitfield.  Can be F_OK to test existence,
                or the inclusive-OR of R_OK, W_OK, and X_OK.
              dir_fd
                If not None, it should be a file descriptor open to a directory,
                and path should be relative; path will then be relative to that
                directory.
              effective_ids
                If True, access will use the effective uid/gid instead of
                the real uid/gid.
              follow_symlinks
                If False, and the last element of the path is a symbolic link,
                access will examine the symbolic link itself instead of the file
                the link points to.
            
            dir_fd, effective_ids, and follow_symlinks may not be implemented
              on your platform.  If they are unavailable, using them will raise a
              NotImplementedError.
            
            Note that most operations will use the effective uid/gid, therefore this
              routine can be used in a suid/sgid environment to test if the invoking user
              has the specified access to the path.
        
        chdir(path)
            Change the current working directory to the specified path.
            
            path may always be specified as a string.
            On some platforms, path may also be specified as an open file descriptor.
              If this functionality is unavailable, using it raises an exception.
        
        chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
            Change the access permissions of a file.
            
              path
                Path to be modified.  May always be specified as a str, bytes, or a path-like object.
                On some platforms, path may also be specified as an open file descriptor.
                If this functionality is unavailable, using it raises an exception.
              mode
                Operating-system mode bitfield.
              dir_fd
                If not None, it should be a file descriptor open to a directory,
                and path should be relative; path will then be relative to that
                directory.
              follow_symlinks
                If False, and the last element of the path is a symbolic link,
                chmod will modify the symbolic link itself instead of the file
                the link points to.
            
            It is an error to use dir_fd or follow_symlinks when specifying path as
              an open file descriptor.
            dir_fd and follow_symlinks may not be implemented on your platform.
              If they are unavailable, using them will raise a NotImplementedError.
        
        chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)
            Change the owner and group id of path to the numeric uid and gid.\
            
              path
                Path to be examined; can be string, bytes, a path-like object, or open-file-descriptor int.
              dir_fd
                If not None, it should be a file descriptor open to a directory,
                and path should be relative; path will then be relative to that
                directory.
              follow_symlinks
                If False, and the last element of the path is a symbolic link,
                stat will examine the symbolic link itself instead of the file
                the link points to.
            
            path may always be specified as a string.
            On some platforms, path may also be specified as an open file descriptor.
              If this functionality is unavailable, using it raises an exception.
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            If follow_symlinks is False, and the last element of the path is a symbolic
              link, chown will modify the symbolic link itself instead of the file the
              link points to.
            It is an error to use dir_fd or follow_symlinks when specifying path as
              an open file descriptor.
            dir_fd and follow_symlinks may not be implemented on your platform.
              If they are unavailable, using them will raise a NotImplementedError.
        
        chroot(path)
            Change root directory to path.
        
        close(fd)
            Close a file descriptor.
        
        closerange(fd_low, fd_high, /)
            Closes all file descriptors in [fd_low, fd_high), ignoring errors.
        
        confstr(name, /)
            Return a string-valued system configuration variable.
        
        copy_file_range(src, dst, count, offset_src=None, offset_dst=None)
            Copy count bytes from one file descriptor to another.
            
              src
                Source file descriptor.
              dst
                Destination file descriptor.
              count
                Number of bytes to copy.
              offset_src
                Starting offset in src.
              offset_dst
                Starting offset in dst.
            
            If offset_src is None, then src is read from the current position;
            respectively for offset_dst.
        
        cpu_count()
            Return the number of CPUs in the system; return None if indeterminable.
            
            This number is not equivalent to the number of CPUs the current process can
            use.  The number of usable CPUs can be obtained with
            ``len(os.sched_getaffinity(0))``
        
        ctermid()
            Return the name of the controlling terminal for this process.
        
        device_encoding(fd)
            Return a string describing the encoding of a terminal's file descriptor.
            
            The file descriptor must be attached to a terminal.
            If the device is not a terminal, return None.
        
        dup(fd, /)
            Return a duplicate of a file descriptor.
        
        dup2(fd, fd2, inheritable=True)
            Duplicate file descriptor.
        
        eventfd(initval, flags=524288)
            Creates and returns an event notification file descriptor.
        
        eventfd_read(fd)
            Read eventfd value
        
        eventfd_write(fd, value)
            Write eventfd value.
        
        execl(file, *args)
            execl(file, *args)
            
            Execute the executable file with argument list args, replacing the
            current process.
        
        execle(file, *args)
            execle(file, *args, env)
            
            Execute the executable file with argument list args and
            environment env, replacing the current process.
        
        execlp(file, *args)
            execlp(file, *args)
            
            Execute the executable file (which is searched for along $PATH)
            with argument list args, replacing the current process.
        
        execlpe(file, *args)
            execlpe(file, *args, env)
            
            Execute the executable file (which is searched for along $PATH)
            with argument list args and environment env, replacing the current
            process.
        
        execv(path, argv, /)
            Execute an executable path with arguments, replacing current process.
            
            path
              Path of executable file.
            argv
              Tuple or list of strings.
        
        execve(path, argv, env)
            Execute an executable path with arguments, replacing current process.
            
            path
              Path of executable file.
            argv
              Tuple or list of strings.
            env
              Dictionary of strings mapping to strings.
        
        execvp(file, args)
            execvp(file, args)
            
            Execute the executable file (which is searched for along $PATH)
            with argument list args, replacing the current process.
            args may be a list or tuple of strings.
        
        execvpe(file, args, env)
            execvpe(file, args, env)
            
            Execute the executable file (which is searched for along $PATH)
            with argument list args and environment env, replacing the
            current process.
            args may be a list or tuple of strings.
        
        fchdir(fd)
            Change to the directory of the given file descriptor.
            
            fd must be opened on a directory, not a file.
            Equivalent to os.chdir(fd).
        
        fchmod(fd, mode)
            Change the access permissions of the file given by file descriptor fd.
            
            Equivalent to os.chmod(fd, mode).
        
        fchown(fd, uid, gid)
            Change the owner and group id of the file specified by file descriptor.
            
            Equivalent to os.chown(fd, uid, gid).
        
        fdatasync(fd)
            Force write of fd to disk without forcing update of metadata.
        
        fdopen(fd, mode='r', buffering=-1, encoding=None, *args, **kwargs)
        
        fork()
            Fork a child process.
            
            Return 0 to child process and PID of child to parent process.
        
        forkpty()
            Fork a new process with a new pseudo-terminal as controlling tty.
            
            Returns a tuple of (pid, master_fd).
            Like fork(), return pid of 0 to the child process,
            and pid of child to the parent process.
            To both, return fd of newly opened pseudo-terminal.
        
        fpathconf(fd, name, /)
            Return the configuration limit name for the file descriptor fd.
            
            If there is no limit, return -1.
        
        fsdecode(filename)
            Decode filename (an os.PathLike, bytes, or str) from the filesystem
            encoding with 'surrogateescape' error handler, return str unchanged. On
            Windows, use 'strict' error handler if the file system encoding is
            'mbcs' (which is the default encoding).
        
        fsencode(filename)
            Encode filename (an os.PathLike, bytes, or str) to the filesystem
            encoding with 'surrogateescape' error handler, return bytes unchanged.
            On Windows, use 'strict' error handler if the file system encoding is
            'mbcs' (which is the default encoding).
        
        fspath(path)
            Return the file system path representation of the object.
            
            If the object is str or bytes, then allow it to pass through as-is. If the
            object defines __fspath__(), then return the result of that method. All other
            types raise a TypeError.
        
        fstat(fd)
            Perform a stat system call on the given file descriptor.
            
            Like stat(), but for an open file descriptor.
            Equivalent to os.stat(fd).
        
        fstatvfs(fd, /)
            Perform an fstatvfs system call on the given fd.
            
            Equivalent to statvfs(fd).
        
        fsync(fd)
            Force write of fd to disk.
        
        ftruncate(fd, length, /)
            Truncate a file, specified by file descriptor, to a specific length.
        
        fwalk(top='.', topdown=True, onerror=None, *, follow_symlinks=False, dir_fd=None)
            Directory tree generator.
            
            This behaves exactly like walk(), except that it yields a 4-tuple
            
                dirpath, dirnames, filenames, dirfd
            
            `dirpath`, `dirnames` and `filenames` are identical to walk() output,
            and `dirfd` is a file descriptor referring to the directory `dirpath`.
            
            The advantage of fwalk() over walk() is that it's safe against symlink
            races (when follow_symlinks is False).
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and top should be relative; top will then be relative to that directory.
              (dir_fd is always supported for fwalk.)
            
            Caution:
            Since fwalk() yields file descriptors, those are only valid until the
            next iteration step, so you should dup() them if you want to keep them
            for a longer period.
            
            Example:
            
            import os
            for root, dirs, files, rootfd in os.fwalk('python/Lib/email'):
                print(root, "consumes", end="")
                print(sum(os.stat(name, dir_fd=rootfd).st_size for name in files),
                      end="")
                print("bytes in", len(files), "non-directory files")
                if 'CVS' in dirs:
                    dirs.remove('CVS')  # don't visit CVS directories
        
        get_blocking(fd, /)
            Get the blocking mode of the file descriptor.
            
            Return False if the O_NONBLOCK flag is set, True if the flag is cleared.
        
        get_exec_path(env=None)
            Returns the sequence of directories that will be searched for the
            named executable (similar to a shell) when launching a process.
            
            *env* must be an environment variable dict or None.  If *env* is None,
            os.environ will be used.
        
        get_inheritable(fd, /)
            Get the close-on-exe flag of the specified file descriptor.
        
        get_terminal_size(...)
            Return the size of the terminal window as (columns, lines).
            
            The optional argument fd (default standard output) specifies
            which file descriptor should be queried.
            
            If the file descriptor is not connected to a terminal, an OSError
            is thrown.
            
            This function will only be defined if an implementation is
            available for this system.
            
            shutil.get_terminal_size is the high-level function which should
            normally be used, os.get_terminal_size is the low-level implementation.
        
        getcwd()
            Return a unicode string representing the current working directory.
        
        getcwdb()
            Return a bytes string representing the current working directory.
        
        getegid()
            Return the current process's effective group id.
        
        getenv(key, default=None)
            Get an environment variable, return None if it doesn't exist.
            The optional second argument can specify an alternate default.
            key, default and the result are str.
        
        getenvb(key, default=None)
            Get an environment variable, return None if it doesn't exist.
            The optional second argument can specify an alternate default.
            key, default and the result are bytes.
        
        geteuid()
            Return the current process's effective user id.
        
        getgid()
            Return the current process's group id.
        
        getgrouplist(user, group, /)
            Returns a list of groups to which a user belongs.
            
            user
              username to lookup
            group
              base group id of the user
        
        getgroups()
            Return list of supplemental group IDs for the process.
        
        getloadavg()
            Return average recent system load information.
            
            Return the number of processes in the system run queue averaged over
            the last 1, 5, and 15 minutes as a tuple of three floats.
            Raises OSError if the load average was unobtainable.
        
        getlogin()
            Return the actual login name.
        
        getpgid(pid)
            Call the system call getpgid(), and return the result.
        
        getpgrp()
            Return the current process group id.
        
        getpid()
            Return the current process id.
        
        getppid()
            Return the parent's process id.
            
            If the parent process has already exited, Windows machines will still
            return its id; others systems will return the id of the 'init' process (1).
        
        getpriority(which, who)
            Return program scheduling priority.
        
        getrandom(size, flags=0)
            Obtain a series of random bytes.
        
        getresgid()
            Return a tuple of the current process's real, effective, and saved group ids.
        
        getresuid()
            Return a tuple of the current process's real, effective, and saved user ids.
        
        getsid(pid, /)
            Call the system call getsid(pid) and return the result.
        
        getuid()
            Return the current process's user id.
        
        getxattr(path, attribute, *, follow_symlinks=True)
            Return the value of extended attribute attribute on path.
            
            path may be either a string, a path-like object, or an open file descriptor.
            If follow_symlinks is False, and the last element of the path is a symbolic
              link, getxattr will examine the symbolic link itself instead of the file
              the link points to.
        
        initgroups(username, gid, /)
            Initialize the group access list.
            
            Call the system initgroups() to initialize the group access list with all of
            the groups of which the specified username is a member, plus the specified
            group id.
        
        isatty(fd, /)
            Return True if the fd is connected to a terminal.
            
            Return True if the file descriptor is an open file descriptor
            connected to the slave end of a terminal.
        
        kill(pid, signal, /)
            Kill a process with a signal.
        
        killpg(pgid, signal, /)
            Kill a process group with a signal.
        
        lchown(path, uid, gid)
            Change the owner and group id of path to the numeric uid and gid.
            
            This function will not follow symbolic links.
            Equivalent to os.chown(path, uid, gid, follow_symlinks=False).
        
        link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
            Create a hard link to a file.
            
            If either src_dir_fd or dst_dir_fd is not None, it should be a file
              descriptor open to a directory, and the respective path string (src or dst)
              should be relative; the path will then be relative to that directory.
            If follow_symlinks is False, and the last element of src is a symbolic
              link, link will create a link to the symbolic link itself instead of the
              file the link points to.
            src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
              platform.  If they are unavailable, using them will raise a
              NotImplementedError.
        
        listdir(path=None)
            Return a list containing the names of the files in the directory.
            
            path can be specified as either str, bytes, or a path-like object.  If path is bytes,
              the filenames returned will also be bytes; in all other circumstances
              the filenames returned will be str.
            If path is None, uses the path='.'.
            On some platforms, path may also be specified as an open file descriptor;\
              the file descriptor must refer to a directory.
              If this functionality is unavailable, using it raises NotImplementedError.
            
            The list is in arbitrary order.  It does not include the special
            entries '.' and '..' even if they are present in the directory.
        
        listxattr(path=None, *, follow_symlinks=True)
            Return a list of extended attributes on path.
            
            path may be either None, a string, a path-like object, or an open file descriptor.
            if path is None, listxattr will examine the current directory.
            If follow_symlinks is False, and the last element of the path is a symbolic
              link, listxattr will examine the symbolic link itself instead of the file
              the link points to.
        
        lockf(fd, command, length, /)
            Apply, test or remove a POSIX lock on an open file descriptor.
            
            fd
              An open file descriptor.
            command
              One of F_LOCK, F_TLOCK, F_ULOCK or F_TEST.
            length
              The number of bytes to lock, starting at the current position.
        
        login_tty(fd, /)
            Prepare the tty of which fd is a file descriptor for a new login session.
            
            Make the calling process a session leader; make the tty the
            controlling tty, the stdin, the stdout, and the stderr of the
            calling process; close fd.
        
        lseek(fd, position, whence, /)
            Set the position of a file descriptor.  Return the new position.
            
              fd
                An open file descriptor, as returned by os.open().
              position
                Position, interpreted relative to 'whence'.
              whence
                The relative position to seek from. Valid values are:
                - SEEK_SET: seek from the start of the file.
                - SEEK_CUR: seek from the current file position.
                - SEEK_END: seek from the end of the file.
            
            The return value is the number of bytes relative to the beginning of the file.
        
        lstat(path, *, dir_fd=None)
            Perform a stat system call on the given path, without following symbolic links.
            
            Like stat(), but do not follow symbolic links.
            Equivalent to stat(path, follow_symlinks=False).
        
        major(device, /)
            Extracts a device major number from a raw device number.
        
        makedev(major, minor, /)
            Composes a raw device number from the major and minor device numbers.
        
        makedirs(name, mode=511, exist_ok=False)
            makedirs(name [, mode=0o777][, exist_ok=False])
            
            Super-mkdir; create a leaf directory and all intermediate ones.  Works like
            mkdir, except that any intermediate path segment (not just the rightmost)
            will be created if it does not exist. If the target directory already
            exists, raise an OSError if exist_ok is False. Otherwise no exception is
            raised.  This is recursive.
        
        memfd_create(name, flags=1)
        
        minor(device, /)
            Extracts a device minor number from a raw device number.
        
        mkdir(path, mode=511, *, dir_fd=None)
            Create a directory.
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            dir_fd may not be implemented on your platform.
              If it is unavailable, using it will raise a NotImplementedError.
            
            The mode argument is ignored on Windows. Where it is used, the current umask
            value is first masked out.
        
        mkfifo(path, mode=438, *, dir_fd=None)
            Create a "fifo" (a POSIX named pipe).
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            dir_fd may not be implemented on your platform.
              If it is unavailable, using it will raise a NotImplementedError.
        
        mknod(path, mode=384, device=0, *, dir_fd=None)
            Create a node in the file system.
            
            Create a node in the file system (file, device special file or named pipe)
            at path.  mode specifies both the permissions to use and the
            type of node to be created, being combined (bitwise OR) with one of
            S_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO.  If S_IFCHR or S_IFBLK is set on mode,
            device defines the newly created device special file (probably using
            os.makedev()).  Otherwise device is ignored.
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            dir_fd may not be implemented on your platform.
              If it is unavailable, using it will raise a NotImplementedError.
        
        nice(increment, /)
            Add increment to the priority of process and return the new priority.
        
        open(path, flags, mode=511, *, dir_fd=None)
            Open a file for low level IO.  Returns a file descriptor (integer).
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            dir_fd may not be implemented on your platform.
              If it is unavailable, using it will raise a NotImplementedError.
        
        openpty()
            Open a pseudo-terminal.
            
            Return a tuple of (master_fd, slave_fd) containing open file descriptors
            for both the master and slave ends.
        
        pathconf(path, name)
            Return the configuration limit name for the file or directory path.
            
            If there is no limit, return -1.
            On some platforms, path may also be specified as an open file descriptor.
              If this functionality is unavailable, using it raises an exception.
        
        pidfd_open(pid, flags=0)
            Return a file descriptor referring to the process *pid*.
            
            The descriptor can be used to perform process management without races and
            signals.
        
        pipe()
            Create a pipe.
            
            Returns a tuple of two file descriptors:
              (read_fd, write_fd)
        
        pipe2(flags, /)
            Create a pipe with flags set atomically.
            
            Returns a tuple of two file descriptors:
              (read_fd, write_fd)
            
            flags can be constructed by ORing together one or more of these values:
            O_NONBLOCK, O_CLOEXEC.
        
        popen(cmd, mode='r', buffering=-1)
        
        posix_fadvise(fd, offset, length, advice, /)
            Announce an intention to access data in a specific pattern.
            
            Announce an intention to access data in a specific pattern, thus allowing
            the kernel to make optimizations.
            The advice applies to the region of the file specified by fd starting at
            offset and continuing for length bytes.
            advice is one of POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL,
            POSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED, or
            POSIX_FADV_DONTNEED.
        
        posix_fallocate(fd, offset, length, /)
            Ensure a file has allocated at least a particular number of bytes on disk.
            
            Ensure that the file specified by fd encompasses a range of bytes
            starting at offset bytes from the beginning and continuing for length bytes.
        
        posix_spawn(...)
            Execute the program specified by path in a new process.
            
            path
              Path of executable file.
            argv
              Tuple or list of strings.
            env
              Dictionary of strings mapping to strings.
            file_actions
              A sequence of file action tuples.
            setpgroup
              The pgroup to use with the POSIX_SPAWN_SETPGROUP flag.
            resetids
              If the value is `true` the POSIX_SPAWN_RESETIDS will be activated.
            setsid
              If the value is `true` the POSIX_SPAWN_SETSID or POSIX_SPAWN_SETSID_NP will be activated.
            setsigmask
              The sigmask to use with the POSIX_SPAWN_SETSIGMASK flag.
            setsigdef
              The sigmask to use with the POSIX_SPAWN_SETSIGDEF flag.
            scheduler
              A tuple with the scheduler policy (optional) and parameters.
        
        posix_spawnp(...)
            Execute the program specified by path in a new process.
            
            path
              Path of executable file.
            argv
              Tuple or list of strings.
            env
              Dictionary of strings mapping to strings.
            file_actions
              A sequence of file action tuples.
            setpgroup
              The pgroup to use with the POSIX_SPAWN_SETPGROUP flag.
            resetids
              If the value is `True` the POSIX_SPAWN_RESETIDS will be activated.
            setsid
              If the value is `True` the POSIX_SPAWN_SETSID or POSIX_SPAWN_SETSID_NP will be activated.
            setsigmask
              The sigmask to use with the POSIX_SPAWN_SETSIGMASK flag.
            setsigdef
              The sigmask to use with the POSIX_SPAWN_SETSIGDEF flag.
            scheduler
              A tuple with the scheduler policy (optional) and parameters.
        
        pread(fd, length, offset, /)
            Read a number of bytes from a file descriptor starting at a particular offset.
            
            Read length bytes from file descriptor fd, starting at offset bytes from
            the beginning of the file.  The file offset remains unchanged.
        
        preadv(fd, buffers, offset, flags=0, /)
            Reads from a file descriptor into a number of mutable bytes-like objects.
            
            Combines the functionality of readv() and pread(). As readv(), it will
            transfer data into each buffer until it is full and then move on to the next
            buffer in the sequence to hold the rest of the data. Its fourth argument,
            specifies the file offset at which the input operation is to be performed. It
            will return the total number of bytes read (which can be less than the total
            capacity of all the objects).
            
            The flags argument contains a bitwise OR of zero or more of the following flags:
            
            - RWF_HIPRI
            - RWF_NOWAIT
            
            Using non-zero flags requires Linux 4.6 or newer.
        
        putenv(name, value, /)
            Change or add an environment variable.
        
        pwrite(fd, buffer, offset, /)
            Write bytes to a file descriptor starting at a particular offset.
            
            Write buffer to fd, starting at offset bytes from the beginning of
            the file.  Returns the number of bytes writte.  Does not change the
            current file offset.
        
        pwritev(fd, buffers, offset, flags=0, /)
            Writes the contents of bytes-like objects to a file descriptor at a given offset.
            
            Combines the functionality of writev() and pwrite(). All buffers must be a sequence
            of bytes-like objects. Buffers are processed in array order. Entire contents of first
            buffer is written before proceeding to second, and so on. The operating system may
            set a limit (sysconf() value SC_IOV_MAX) on the number of buffers that can be used.
            This function writes the contents of each object to the file descriptor and returns
            the total number of bytes written.
            
            The flags argument contains a bitwise OR of zero or more of the following flags:
            
            - RWF_DSYNC
            - RWF_SYNC
            - RWF_APPEND
            
            Using non-zero flags requires Linux 4.7 or newer.
        
        read(fd, length, /)
            Read from a file descriptor.  Returns a bytes object.
        
        readlink(path, *, dir_fd=None)
            Return a string representing the path to which the symbolic link points.
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that directory.
            
            dir_fd may not be implemented on your platform.  If it is unavailable,
            using it will raise a NotImplementedError.
        
        readv(fd, buffers, /)
            Read from a file descriptor fd into an iterable of buffers.
            
            The buffers should be mutable buffers accepting bytes.
            readv will transfer data into each buffer until it is full
            and then move on to the next buffer in the sequence to hold
            the rest of the data.
            
            readv returns the total number of bytes read,
            which may be less than the total capacity of all the buffers.
        
        register_at_fork(...)
            Register callables to be called when forking a new process.
            
              before
                A callable to be called in the parent before the fork() syscall.
              after_in_child
                A callable to be called in the child after fork().
              after_in_parent
                A callable to be called in the parent after fork().
            
            'before' callbacks are called in reverse order.
            'after_in_child' and 'after_in_parent' callbacks are called in order.
        
        remove(path, *, dir_fd=None)
            Remove a file (same as unlink()).
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            dir_fd may not be implemented on your platform.
              If it is unavailable, using it will raise a NotImplementedError.
        
        removedirs(name)
            removedirs(name)
            
            Super-rmdir; remove a leaf directory and all empty intermediate
            ones.  Works like rmdir except that, if the leaf directory is
            successfully removed, directories corresponding to rightmost path
            segments will be pruned away until either the whole path is
            consumed or an error occurs.  Errors during this latter phase are
            ignored -- they generally mean that a directory was not empty.
        
        removexattr(path, attribute, *, follow_symlinks=True)
            Remove extended attribute attribute on path.
            
            path may be either a string, a path-like object, or an open file descriptor.
            If follow_symlinks is False, and the last element of the path is a symbolic
              link, removexattr will modify the symbolic link itself instead of the file
              the link points to.
        
        rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
            Rename a file or directory.
            
            If either src_dir_fd or dst_dir_fd is not None, it should be a file
              descriptor open to a directory, and the respective path string (src or dst)
              should be relative; the path will then be relative to that directory.
            src_dir_fd and dst_dir_fd, may not be implemented on your platform.
              If they are unavailable, using them will raise a NotImplementedError.
        
        renames(old, new)
            renames(old, new)
            
            Super-rename; create directories as necessary and delete any left
            empty.  Works like rename, except creation of any intermediate
            directories needed to make the new pathname good is attempted
            first.  After the rename, directories corresponding to rightmost
            path segments of the old name will be pruned until either the
            whole path is consumed or a nonempty directory is found.
            
            Note: this function can fail with the new directory structure made
            if you lack permissions needed to unlink the leaf directory or
            file.
        
        replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
            Rename a file or directory, overwriting the destination.
            
            If either src_dir_fd or dst_dir_fd is not None, it should be a file
              descriptor open to a directory, and the respective path string (src or dst)
              should be relative; the path will then be relative to that directory.
            src_dir_fd and dst_dir_fd, may not be implemented on your platform.
              If they are unavailable, using them will raise a NotImplementedError.
        
        rmdir(path, *, dir_fd=None)
            Remove a directory.
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            dir_fd may not be implemented on your platform.
              If it is unavailable, using it will raise a NotImplementedError.
        
        scandir(path=None)
            Return an iterator of DirEntry objects for given path.
            
            path can be specified as either str, bytes, or a path-like object.  If path
            is bytes, the names of yielded DirEntry objects will also be bytes; in
            all other circumstances they will be str.
            
            If path is None, uses the path='.'.
        
        sched_get_priority_max(policy)
            Get the maximum scheduling priority for policy.
        
        sched_get_priority_min(policy)
            Get the minimum scheduling priority for policy.
        
        sched_getaffinity(pid, /)
            Return the affinity of the process identified by pid (or the current process if zero).
            
            The affinity is returned as a set of CPU identifiers.
        
        sched_getparam(pid, /)
            Returns scheduling parameters for the process identified by pid.
            
            If pid is 0, returns parameters for the calling process.
            Return value is an instance of sched_param.
        
        sched_getscheduler(pid, /)
            Get the scheduling policy for the process identified by pid.
            
            Passing 0 for pid returns the scheduling policy for the calling process.
        
        sched_rr_get_interval(pid, /)
            Return the round-robin quantum for the process identified by pid, in seconds.
            
            Value returned is a float.
        
        sched_setaffinity(pid, mask, /)
            Set the CPU affinity of the process identified by pid to mask.
            
            mask should be an iterable of integers identifying CPUs.
        
        sched_setparam(pid, param, /)
            Set scheduling parameters for the process identified by pid.
            
            If pid is 0, sets parameters for the calling process.
            param should be an instance of sched_param.
        
        sched_setscheduler(pid, policy, param, /)
            Set the scheduling policy for the process identified by pid.
            
            If pid is 0, the calling process is changed.
            param is an instance of sched_param.
        
        sched_yield()
            Voluntarily relinquish the CPU.
        
        sendfile(out_fd, in_fd, offset, count)
            Copy count bytes from file descriptor in_fd to file descriptor out_fd.
        
        set_blocking(fd, blocking, /)
            Set the blocking mode of the specified file descriptor.
            
            Set the O_NONBLOCK flag if blocking is False,
            clear the O_NONBLOCK flag otherwise.
        
        set_inheritable(fd, inheritable, /)
            Set the inheritable flag of the specified file descriptor.
        
        setegid(egid, /)
            Set the current process's effective group id.
        
        seteuid(euid, /)
            Set the current process's effective user id.
        
        setgid(gid, /)
            Set the current process's group id.
        
        setgroups(groups, /)
            Set the groups of the current process to list.
        
        setpgid(pid, pgrp, /)
            Call the system call setpgid(pid, pgrp).
        
        setpgrp()
            Make the current process the leader of its process group.
        
        setpriority(which, who, priority)
            Set program scheduling priority.
        
        setregid(rgid, egid, /)
            Set the current process's real and effective group ids.
        
        setresgid(rgid, egid, sgid, /)
            Set the current process's real, effective, and saved group ids.
        
        setresuid(ruid, euid, suid, /)
            Set the current process's real, effective, and saved user ids.
        
        setreuid(ruid, euid, /)
            Set the current process's real and effective user ids.
        
        setsid()
            Call the system call setsid().
        
        setuid(uid, /)
            Set the current process's user id.
        
        setxattr(path, attribute, value, flags=0, *, follow_symlinks=True)
            Set extended attribute attribute on path to value.
            
            path may be either a string, a path-like object,  or an open file descriptor.
            If follow_symlinks is False, and the last element of the path is a symbolic
              link, setxattr will modify the symbolic link itself instead of the file
              the link points to.
        
        spawnl(mode, file, *args)
            spawnl(mode, file, *args) -> integer
            
            Execute file with arguments from args in a subprocess.
            If mode == P_NOWAIT return the pid of the process.
            If mode == P_WAIT return the process's exit code if it exits normally;
            otherwise return -SIG, where SIG is the signal that killed it.
        
        spawnle(mode, file, *args)
            spawnle(mode, file, *args, env) -> integer
            
            Execute file with arguments from args in a subprocess with the
            supplied environment.
            If mode == P_NOWAIT return the pid of the process.
            If mode == P_WAIT return the process's exit code if it exits normally;
            otherwise return -SIG, where SIG is the signal that killed it.
        
        spawnlp(mode, file, *args)
            spawnlp(mode, file, *args) -> integer
            
            Execute file (which is looked for along $PATH) with arguments from
            args in a subprocess with the supplied environment.
            If mode == P_NOWAIT return the pid of the process.
            If mode == P_WAIT return the process's exit code if it exits normally;
            otherwise return -SIG, where SIG is the signal that killed it.
        
        spawnlpe(mode, file, *args)
            spawnlpe(mode, file, *args, env) -> integer
            
            Execute file (which is looked for along $PATH) with arguments from
            args in a subprocess with the supplied environment.
            If mode == P_NOWAIT return the pid of the process.
            If mode == P_WAIT return the process's exit code if it exits normally;
            otherwise return -SIG, where SIG is the signal that killed it.
        
        spawnv(mode, file, args)
            spawnv(mode, file, args) -> integer
            
            Execute file with arguments from args in a subprocess.
            If mode == P_NOWAIT return the pid of the process.
            If mode == P_WAIT return the process's exit code if it exits normally;
            otherwise return -SIG, where SIG is the signal that killed it.
        
        spawnve(mode, file, args, env)
            spawnve(mode, file, args, env) -> integer
            
            Execute file with arguments from args in a subprocess with the
            specified environment.
            If mode == P_NOWAIT return the pid of the process.
            If mode == P_WAIT return the process's exit code if it exits normally;
            otherwise return -SIG, where SIG is the signal that killed it.
        
        spawnvp(mode, file, args)
            spawnvp(mode, file, args) -> integer
            
            Execute file (which is looked for along $PATH) with arguments from
            args in a subprocess.
            If mode == P_NOWAIT return the pid of the process.
            If mode == P_WAIT return the process's exit code if it exits normally;
            otherwise return -SIG, where SIG is the signal that killed it.
        
        spawnvpe(mode, file, args, env)
            spawnvpe(mode, file, args, env) -> integer
            
            Execute file (which is looked for along $PATH) with arguments from
            args in a subprocess with the supplied environment.
            If mode == P_NOWAIT return the pid of the process.
            If mode == P_WAIT return the process's exit code if it exits normally;
            otherwise return -SIG, where SIG is the signal that killed it.
        
        splice(src, dst, count, offset_src=None, offset_dst=None, flags=0)
            Transfer count bytes from one pipe to a descriptor or vice versa.
            
              src
                Source file descriptor.
              dst
                Destination file descriptor.
              count
                Number of bytes to copy.
              offset_src
                Starting offset in src.
              offset_dst
                Starting offset in dst.
              flags
                Flags to modify the semantics of the call.
            
            If offset_src is None, then src is read from the current position;
            respectively for offset_dst. The offset associated to the file
            descriptor that refers to a pipe must be None.
        
        stat(path, *, dir_fd=None, follow_symlinks=True)
            Perform a stat system call on the given path.
            
              path
                Path to be examined; can be string, bytes, a path-like object or
                open-file-descriptor int.
              dir_fd
                If not None, it should be a file descriptor open to a directory,
                and path should be a relative string; path will then be relative to
                that directory.
              follow_symlinks
                If False, and the last element of the path is a symbolic link,
                stat will examine the symbolic link itself instead of the file
                the link points to.
            
            dir_fd and follow_symlinks may not be implemented
              on your platform.  If they are unavailable, using them will raise a
              NotImplementedError.
            
            It's an error to use dir_fd or follow_symlinks when specifying path as
              an open file descriptor.
        
        statvfs(path)
            Perform a statvfs system call on the given path.
            
            path may always be specified as a string.
            On some platforms, path may also be specified as an open file descriptor.
              If this functionality is unavailable, using it raises an exception.
        
        strerror(code, /)
            Translate an error code to a message string.
        
        symlink(src, dst, target_is_directory=False, *, dir_fd=None)
            Create a symbolic link pointing to src named dst.
            
            target_is_directory is required on Windows if the target is to be
              interpreted as a directory.  (On Windows, symlink requires
              Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
              target_is_directory is ignored on non-Windows platforms.
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            dir_fd may not be implemented on your platform.
              If it is unavailable, using it will raise a NotImplementedError.
        
        sync()
            Force write of everything to disk.
        
        sysconf(name, /)
            Return an integer-valued system configuration variable.
        
        system(command)
            Execute the command in a subshell.
        
        tcgetpgrp(fd, /)
            Return the process group associated with the terminal specified by fd.
        
        tcsetpgrp(fd, pgid, /)
            Set the process group associated with the terminal specified by fd.
        
        times()
            Return a collection containing process timing information.
            
            The object returned behaves like a named tuple with these fields:
              (utime, stime, cutime, cstime, elapsed_time)
            All fields are floating point numbers.
        
        truncate(path, length)
            Truncate a file, specified by path, to a specific length.
            
            On some platforms, path may also be specified as an open file descriptor.
              If this functionality is unavailable, using it raises an exception.
        
        ttyname(fd, /)
            Return the name of the terminal device connected to 'fd'.
            
            fd
              Integer file descriptor handle.
        
        umask(mask, /)
            Set the current numeric umask and return the previous umask.
        
        uname()
            Return an object identifying the current operating system.
            
            The object behaves like a named tuple with the following fields:
              (sysname, nodename, release, version, machine)
        
        unlink(path, *, dir_fd=None)
            Remove a file (same as remove()).
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            dir_fd may not be implemented on your platform.
              If it is unavailable, using it will raise a NotImplementedError.
        
        unsetenv(name, /)
            Delete an environment variable.
        
        urandom(size, /)
            Return a bytes object containing random bytes suitable for cryptographic use.
        
        utime(...)
            Set the access and modified time of path.
            
            path may always be specified as a string.
            On some platforms, path may also be specified as an open file descriptor.
              If this functionality is unavailable, using it raises an exception.
            
            If times is not None, it must be a tuple (atime, mtime);
                atime and mtime should be expressed as float seconds since the epoch.
            If ns is specified, it must be a tuple (atime_ns, mtime_ns);
                atime_ns and mtime_ns should be expressed as integer nanoseconds
                since the epoch.
            If times is None and ns is unspecified, utime uses the current time.
            Specifying tuples for both times and ns is an error.
            
            If dir_fd is not None, it should be a file descriptor open to a directory,
              and path should be relative; path will then be relative to that directory.
            If follow_symlinks is False, and the last element of the path is a symbolic
              link, utime will modify the symbolic link itself instead of the file the
              link points to.
            It is an error to use dir_fd or follow_symlinks when specifying path
              as an open file descriptor.
            dir_fd and follow_symlinks may not be available on your platform.
              If they are unavailable, using them will raise a NotImplementedError.
        
        wait()
            Wait for completion of a child process.
            
            Returns a tuple of information about the child process:
                (pid, status)
        
        wait3(options)
            Wait for completion of a child process.
            
            Returns a tuple of information about the child process:
              (pid, status, rusage)
        
        wait4(pid, options)
            Wait for completion of a specific child process.
            
            Returns a tuple of information about the child process:
              (pid, status, rusage)
        
        waitid(idtype, id, options, /)
            Returns the result of waiting for a process or processes.
            
              idtype
                Must be one of be P_PID, P_PGID or P_ALL.
              id
                The id to wait on.
              options
                Constructed from the ORing of one or more of WEXITED, WSTOPPED
                or WCONTINUED and additionally may be ORed with WNOHANG or WNOWAIT.
            
            Returns either waitid_result or None if WNOHANG is specified and there are
            no children in a waitable state.
        
        waitpid(pid, options, /)
            Wait for completion of a given child process.
            
            Returns a tuple of information regarding the child process:
                (pid, status)
            
            The options argument is ignored on Windows.
        
        waitstatus_to_exitcode(status)
            Convert a wait status to an exit code.
            
            On Unix:
            
            * If WIFEXITED(status) is true, return WEXITSTATUS(status).
            * If WIFSIGNALED(status) is true, return -WTERMSIG(status).
            * Otherwise, raise a ValueError.
            
            On Windows, return status shifted right by 8 bits.
            
            On Unix, if the process is being traced or if waitpid() was called with
            WUNTRACED option, the caller must first check if WIFSTOPPED(status) is true.
            This function must not be called if WIFSTOPPED(status) is true.
        
        walk(top, topdown=True, onerror=None, followlinks=False)
            Directory tree generator.
            
            For each directory in the directory tree rooted at top (including top
            itself, but excluding '.' and '..'), yields a 3-tuple
            
                dirpath, dirnames, filenames
            
            dirpath is a string, the path to the directory.  dirnames is a list of
            the names of the subdirectories in dirpath (including symlinks to directories,
            and excluding '.' and '..').
            filenames is a list of the names of the non-directory files in dirpath.
            Note that the names in the lists are just names, with no path components.
            To get a full path (which begins with top) to a file or directory in
            dirpath, do os.path.join(dirpath, name).
            
            If optional arg 'topdown' is true or not specified, the triple for a
            directory is generated before the triples for any of its subdirectories
            (directories are generated top down).  If topdown is false, the triple
            for a directory is generated after the triples for all of its
            subdirectories (directories are generated bottom up).
            
            When topdown is true, the caller can modify the dirnames list in-place
            (e.g., via del or slice assignment), and walk will only recurse into the
            subdirectories whose names remain in dirnames; this can be used to prune the
            search, or to impose a specific order of visiting.  Modifying dirnames when
            topdown is false has no effect on the behavior of os.walk(), since the
            directories in dirnames have already been generated by the time dirnames
            itself is generated. No matter the value of topdown, the list of
            subdirectories is retrieved before the tuples for the directory and its
            subdirectories are generated.
            
            By default errors from the os.scandir() call are ignored.  If
            optional arg 'onerror' is specified, it should be a function; it
            will be called with one argument, an OSError instance.  It can
            report the error to continue with the walk, or raise the exception
            to abort the walk.  Note that the filename is available as the
            filename attribute of the exception object.
            
            By default, os.walk does not follow symbolic links to subdirectories on
            systems that support them.  In order to get this functionality, set the
            optional argument 'followlinks' to true.
            
            Caution:  if you pass a relative pathname for top, don't change the
            current working directory between resumptions of walk.  walk never
            changes the current directory, and assumes that the client doesn't
            either.
            
            Example:
            
            import os
            from os.path import join, getsize
            for root, dirs, files in os.walk('python/Lib/email'):
                print(root, "consumes ")
                print(sum(getsize(join(root, name)) for name in files), end=" ")
                print("bytes in", len(files), "non-directory files")
                if 'CVS' in dirs:
                    dirs.remove('CVS')  # don't visit CVS directories
        
        write(fd, data, /)
            Write a bytes object to a file descriptor.
        
        writev(fd, buffers, /)
            Iterate over buffers, and write the contents of each to a file descriptor.
            
            Returns the total number of bytes written.
            buffers must be a sequence of bytes-like objects.

    DATA
        CLD_CONTINUED = 6
        CLD_DUMPED = 3
        CLD_EXITED = 1
        CLD_KILLED = 2
        CLD_STOPPED = 5
        CLD_TRAPPED = 4
        EFD_CLOEXEC = 524288
        EFD_NONBLOCK = 2048
        EFD_SEMAPHORE = 1
        EX_CANTCREAT = 73
        EX_CONFIG = 78
        EX_DATAERR = 65
        EX_IOERR = 74
        EX_NOHOST = 68
        EX_NOINPUT = 66
        EX_NOPERM = 77
        EX_NOUSER = 67
        EX_OK = 0
        EX_OSERR = 71
        EX_OSFILE = 72
        EX_PROTOCOL = 76
        EX_SOFTWARE = 70
        EX_TEMPFAIL = 75
        EX_UNAVAILABLE = 69
        EX_USAGE = 64
        F_LOCK = 1
        F_OK = 0
        F_TEST = 3
        F_TLOCK = 2
        F_ULOCK = 0
        GRND_NONBLOCK = 1
        GRND_RANDOM = 2
        MFD_ALLOW_SEALING = 2
        MFD_CLOEXEC = 1
        MFD_HUGETLB = 4
        MFD_HUGE_16GB = 2281701376
        MFD_HUGE_16MB = 1610612736
        MFD_HUGE_1GB = 2013265920
        MFD_HUGE_1MB = 1342177280
        MFD_HUGE_256MB = 1879048192
        MFD_HUGE_2GB = 2080374784
        MFD_HUGE_2MB = 1409286144
        MFD_HUGE_32MB = 1677721600
        MFD_HUGE_512KB = 1275068416
        MFD_HUGE_512MB = 1946157056
        MFD_HUGE_64KB = 1073741824
        MFD_HUGE_8MB = 1543503872
        MFD_HUGE_MASK = 63
        MFD_HUGE_SHIFT = 26
        NGROUPS_MAX = 65536
        O_ACCMODE = 3
        O_APPEND = 1024
        O_ASYNC = 8192
        O_CLOEXEC = 524288
        O_CREAT = 64
        O_DIRECT = 16384
        O_DIRECTORY = 65536
        O_DSYNC = 4096
        O_EXCL = 128
        O_FSYNC = 1052672
        O_LARGEFILE = 0
        O_NDELAY = 2048
        O_NOATIME = 262144
        O_NOCTTY = 256
        O_NOFOLLOW = 131072
        O_NONBLOCK = 2048
        O_PATH = 2097152
        O_RDONLY = 0
        O_RDWR = 2
        O_RSYNC = 1052672
        O_SYNC = 1052672
        O_TMPFILE = 4259840
        O_TRUNC = 512
        O_WRONLY = 1
        POSIX_FADV_DONTNEED = 4
        POSIX_FADV_NOREUSE = 5
        POSIX_FADV_NORMAL = 0
        POSIX_FADV_RANDOM = 1
        POSIX_FADV_SEQUENTIAL = 2
        POSIX_FADV_WILLNEED = 3
        POSIX_SPAWN_CLOSE = 1
        POSIX_SPAWN_DUP2 = 2
        POSIX_SPAWN_OPEN = 0
        PRIO_PGRP = 1
        PRIO_PROCESS = 0
        PRIO_USER = 2
        P_ALL = 0
        P_NOWAIT = 1
        P_NOWAITO = 1
        P_PGID = 2
        P_PID = 1
        P_PIDFD = 3
        P_WAIT = 0
        RTLD_DEEPBIND = 8
        RTLD_GLOBAL = 256
        RTLD_LAZY = 1
        RTLD_LOCAL = 0
        RTLD_NODELETE = 4096
        RTLD_NOLOAD = 4
        RTLD_NOW = 2
        RWF_APPEND = 16
        RWF_DSYNC = 2
        RWF_HIPRI = 1
        RWF_NOWAIT = 8
        RWF_SYNC = 4
        R_OK = 4
        SCHED_BATCH = 3
        SCHED_FIFO = 1
        SCHED_IDLE = 5
        SCHED_OTHER = 0
        SCHED_RESET_ON_FORK = 1073741824
        SCHED_RR = 2
        SEEK_CUR = 1
        SEEK_DATA = 3
        SEEK_END = 2
        SEEK_HOLE = 4
        SEEK_SET = 0
        SPLICE_F_MORE = 4
        SPLICE_F_MOVE = 1
        SPLICE_F_NONBLOCK = 2
        ST_APPEND = 256
        ST_MANDLOCK = 64
        ST_NOATIME = 1024
        ST_NODEV = 4
        ST_NODIRATIME = 2048
        ST_NOEXEC = 8
        ST_NOSUID = 2
        ST_RDONLY = 1
        ST_RELATIME = 4096
        ST_SYNCHRONOUS = 16
        ST_WRITE = 128
        TMP_MAX = 238328
        WCONTINUED = 8
        WEXITED = 4
        WNOHANG = 1
        WNOWAIT = 16777216
        WSTOPPED = 2
        WUNTRACED = 2
        W_OK = 2
        XATTR_CREATE = 1
        XATTR_REPLACE = 2
        XATTR_SIZE_MAX = 65536
        X_OK = 1
        __all__ = ['altsep', 'curdir', 'pardir', 'sep', 'pathsep', 'linesep', ...
        altsep = None
        confstr_names = {'CS_GNU_LIBC_VERSION': 2, 'CS_GNU_LIBPTHREAD_VERSION'...
        curdir = '.'
        defpath = '/bin:/usr/bin'
        devnull = '/dev/null'
        environ = environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VER...IRECTORYP...
        environb = environ({b'SHELL': b'/bin/bash', b'NV_LIBCUBLAS_...CTORYPRE...
        extsep = '.'
        linesep = '\n'
        name = 'posix'
        pardir = '..'
        pathconf_names = {'PC_ALLOC_SIZE_MIN': 18, 'PC_ASYNC_IO': 10, 'PC_CHOW...
        pathsep = ':'
        sep = '/'
        supports_bytes_environ = True
        sysconf_names = {'SC_2_CHAR_TERM': 95, 'SC_2_C_BIND': 47, 'SC_2_C_DEV'...

    FILE
        /usr/lib/python3.11/os.py
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":17,\"status\":\"ok\",\"timestamp\":1740855786164,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="4bshNDbdNU4j" outputId="0dfa9b38-b0b8-4fe7-cdf6-cc7532753bab"}
``` python
print("Does exist a file named 'filename.png'?", os.path.isfile('../lena_mod.png'))
```

::: {.output .stream .stdout}
    Does exist a file named 'filename.png'? False
:::
::::

::: {.cell .markdown id="655VVJuZ4idj"}
Connect the Notebook to a Google Drive account
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":52222,\"status\":\"ok\",\"timestamp\":1740855838387,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="JNMNR9YA4AtS" outputId="59f38a7b-fb35-4191-f948-7f7ec5a8ce5d"}
``` python
from google.colab import drive
drive.mount('/content/drive')
```

::: {.output .stream .stdout}
    Mounted at /content/drive
:::
::::

::: {.cell .markdown id="psmGfJx84hmM"}
Now go to the appropriate folder on your google drive. Note: you may need to change the folder name, depending on where on your drive you have the data files.
:::

::: {.cell .code id="oMOLvTtH4dih"}
``` python
import os
os.chdir('/content/drive/MyDrive/Didattica/ML/Exercises/Exercise00')
```
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":296,\"status\":\"ok\",\"timestamp\":1740855839700,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="0SaggIORDlVA" outputId="fc8e1683-cd54-4851-c5e9-a4482e71eb49"}
``` python
!ls -a
```

::: {.output .stream .stdout}
    mnist  mnist.zip  Numpy.ipynb  OtherPackage.ipynb  Python.ipynb
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":4,\"status\":\"ok\",\"timestamp\":1740855839705,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="pV-8qLJ9D3mx" outputId="99962ad0-74f2-4c3a-ce2b-9ee63d1ebcec"}
``` python
os.listdir()
```

::: {.output .execute_result execution_count="22"}
    ['mnist', 'mnist.zip', 'Python.ipynb', 'Numpy.ipynb', 'OtherPackage.ipynb']
:::
::::

::: {.cell .markdown id="PRyrcx3a46zp"}
\#Dealing with the mnist dataset
:::

::: {.cell .code id="LRcWC-uk40OJ"}
``` python
from matplotlib import pyplot as plt

def plot_digit(img):
    ''' WRITE YOUR CODE HERE '''
```
:::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\",\"height\":430}" executionInfo="{\"elapsed\":2357,\"status\":\"ok\",\"timestamp\":1740855842064,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="zFD38TZ146F5" outputId="b5c933fb-18df-4c23-a2c3-384c80b6441c"}
``` python
# Open the image
img = np.asarray(Image.open('mnist/training/0/51.png'))
img_rows, img_cols = img.shape

plot_digit(img)
```

::: {.output .display_data}
![](43acbfc87e1bcfeda178cdd3f14b8f6ab9c89780.png)
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" executionInfo="{\"elapsed\":6,\"status\":\"ok\",\"timestamp\":1740855842064,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="qjS_CumiNU4k" outputId="a13ee173-a2cc-4142-ccb4-7cd7b0635584"}
``` python
from glob import glob
help(glob)
```

::: {.output .stream .stdout}
    Help on function glob in module glob:

    glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)
        Return a list of paths matching a pathname pattern.
        
        The pattern may contain simple shell-style wildcards a la
        fnmatch. Unlike fnmatch, filenames starting with a
        dot are special cases that are not matched by '*' and '?'
        patterns by default.
        
        If `include_hidden` is true, the patterns '*', '?', '**'  will match hidden
        directories.
        
        If `recursive` is true, the pattern '**' will match any files and
        zero or more directories and subdirectories.
:::
::::

:::: {.cell .code colab="{\"base_uri\":\"https://localhost:8080/\"}" collapsed="true" executionInfo="{\"elapsed\":1085,\"status\":\"ok\",\"timestamp\":1740855843144,\"user\":{\"displayName\":\"Diego GRAGNANIELLO\",\"userId\":\"02712514618197687193\"},\"user_tz\":-60}" id="kSGbJBP45PNR" outputId="31b94cc6-5b71-4d38-fcaf-5ae413eeeef9"}
``` python
# get all the mnist file paths
''' WRITE YOUR CODE HERE '''


# print results
''' WRITE YOUR CODE HERE '''
```

::: {.output .stream .stdout}
    Found 100 files:

    00) mnist/training/0/1.png
    01) mnist/training/0/51.png
    02) mnist/training/0/34.png
    03) mnist/training/0/37.png
    04) mnist/training/0/21.png
    05) mnist/training/1/6.png
    06) mnist/training/1/8.png
    07) mnist/training/1/23.png
    08) mnist/training/1/3.png
    09) mnist/training/1/14.png
    10) mnist/training/2/28.png
    11) mnist/training/2/76.png
    12) mnist/training/2/5.png
    13) mnist/training/2/16.png
    14) mnist/training/2/25.png
    15) mnist/training/3/7.png
    16) mnist/training/3/10.png
    17) mnist/training/3/30.png
    18) mnist/training/3/27.png
    19) mnist/training/3/12.png
    20) mnist/training/4/53.png
    21) mnist/training/4/20.png
    22) mnist/training/4/26.png
    23) mnist/training/4/2.png
    24) mnist/training/4/9.png
    25) mnist/training/5/47.png
    26) mnist/training/5/65.png
    27) mnist/training/5/35.png
    28) mnist/training/5/11.png
    29) mnist/training/5/0.png
    30) mnist/training/6/18.png
    31) mnist/training/6/39.png
    32) mnist/training/6/13.png
    33) mnist/training/6/36.png
    34) mnist/training/6/32.png
    35) mnist/training/7/38.png
    36) mnist/training/7/42.png
    37) mnist/training/7/52.png
    38) mnist/training/7/29.png
    39) mnist/training/7/15.png
    40) mnist/training/8/55.png
    41) mnist/training/8/31.png
    42) mnist/training/8/17.png
    43) mnist/training/8/41.png
    44) mnist/training/8/46.png
    45) mnist/training/9/22.png
    46) mnist/training/9/19.png
    47) mnist/training/9/43.png
    48) mnist/training/9/4.png
    49) mnist/training/9/33.png
    50) mnist/testing/0/10.png
    51) mnist/testing/0/28.png
    52) mnist/testing/0/25.png
    53) mnist/testing/0/13.png
    54) mnist/testing/0/3.png
    55) mnist/testing/1/2.png
    56) mnist/testing/1/5.png
    57) mnist/testing/1/29.png
    58) mnist/testing/1/31.png
    59) mnist/testing/1/14.png
    60) mnist/testing/2/47.png
    61) mnist/testing/2/1.png
    62) mnist/testing/2/38.png
    63) mnist/testing/2/43.png
    64) mnist/testing/2/35.png
    65) mnist/testing/3/51.png
    66) mnist/testing/3/30.png
    67) mnist/testing/3/32.png
    68) mnist/testing/3/18.png
    69) mnist/testing/3/44.png
    70) mnist/testing/4/19.png
    71) mnist/testing/4/24.png
    72) mnist/testing/4/4.png
    73) mnist/testing/4/6.png
    74) mnist/testing/4/27.png
    75) mnist/testing/5/45.png
    76) mnist/testing/5/23.png
    77) mnist/testing/5/15.png
    78) mnist/testing/5/52.png
    79) mnist/testing/5/8.png
    80) mnist/testing/6/54.png
    81) mnist/testing/6/11.png
    82) mnist/testing/6/22.png
    83) mnist/testing/6/21.png
    84) mnist/testing/6/50.png
    85) mnist/testing/7/34.png
    86) mnist/testing/7/17.png
    87) mnist/testing/7/36.png
    88) mnist/testing/7/26.png
    89) mnist/testing/7/0.png
    90) mnist/testing/8/61.png
    91) mnist/testing/8/128.png
    92) mnist/testing/8/84.png
    93) mnist/testing/8/110.png
    94) mnist/testing/8/134.png
    95) mnist/testing/9/7.png
    96) mnist/testing/9/20.png
    97) mnist/testing/9/12.png
    98) mnist/testing/9/16.png
    99) mnist/testing/9/9.png
:::
::::

::: {.cell .code id="lkepf1ZMNU4k"}
``` python
# Write the code to load one MNIST sample in two numpy array:
# image of shape (28, 28) containing the image data (cast to float)
# label of shape (1, 1) or (1, ) or an integer value containing the image label (an integer in the range [0, ..., 9])

def load_sample(file_path):

    ''' WRITE YOUR CODE HERE '''

    return image, label
```
:::

::: {.cell .code id="JWOuIWr_NU4k"}
``` python
# Write the code to load several MNIST samples in two numpy array:
# X of shape (50, 28, 28) containing the image data (cast to float)
# y of shape (50, 1) or (50, ) containing the image label (an integer in the range [0, ..., 9])

def load_samples(file_paths):
    data = [load_sample(p) for p in file_paths]

    ''' WRITE YOUR CODE HERE '''

    return X, y
```
:::

::: {.cell .code id="m1wag97_NU4k"}
``` python
# Use the previously defined functions to load all the MNIST training data
''' WRITE YOUR CODE HERE '''
```
:::
