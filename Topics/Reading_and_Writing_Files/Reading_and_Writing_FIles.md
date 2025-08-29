# Topic: Reading and Writing Files

## 📖 Theory - 

### Automate the Boring Stuff - TextBook

#### **Files and File Paths**

- A file has two key properties, file name and path

#### **The Current Working Directory**

```python
>>>from pathlib import Path
>>>import os
>>>Path.cwd()
>>>WindowsPath('C:/Users/Andre/Documents/ICT145_Python_Programmming_for_Everyone/Github_Repo_Python_Learning_Log/python-learning-log/Topics/Input_Validation/mini_projects')
>>>os.chdir("C:\\Windows\\System32")
>>>WindowsPath('C:/Windows/System32')
```
- There is not pathlib function for changing the working directory.
- The os.getcwd() function is the older way of getting the current working directory as a string.

#### The Home Directory
- To get a Path object of the home folder by calling Path.home()
```python
>>>Path.home()
>>>WindowsPath('C:/Users/Andre')
```

#### Absolute vs. Relative Paths
- There are two ways to specify a file path
  - An *absolute path*, which always begins with the root folder
  - A *relative path*, which is relative to the program's current working directory
- THere are also the dot(.) and dot-dot(..) folders. These are special names that can by used in a path
  - A single period for a folder is shorthand for "this directory"
  - Two periods means "the parent folder"

#### Creating New Folders Using the os.makedirs() Function
- Your programs can create new directories with the os.makedirs() function
```python
>>>import os
>>>os.mkdirs("C:\\delicious\\walnut\\waffles")
```
- To make a directory from a Path object, call the mkdir() method
```python
from pathlib import Path
Path(r"C:\Users\Al\spam").mkdir()
```
- mkdir() can only make one directory at a time, to make multiple directories use mkdirs()

#### Handling Absolute and Relative Paths
- Caling he is_absolute() method on a Path object will return True if it represents an 
absolute path or False if it represents a relative path.

#### The File Reading and Writing Process
- The read_text() method returns a string of the full contents of a text file
- The write_text() method creates a new text file (or overwrites an existing one)
with the string passed to it

#### Opening Files with the open() Function
- the open() function returns a File object
- 

#### Saving Variables with the shelve Module


