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
- You can save variables in Python programs to binary shelf files using the shelve module
This way your programs can restore data to variables from the hard drive
- For example if you ran a program and entered some configuration settings, you
can save those settings to a shelf file and then have the program load them the
next time it is run
```python
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ["Zophie", "Pooka", "Simon"]
>>> shelfFile["cats"] = cats
>>> shelfFile.close()
```
- You have to pass the open() shelf method filenames as strings. You can't pass it Path object
- Shelf values don't have to be opened in read or write mode - they can do both once opened.
```python
>>> import shelve
>>> shelfFile = shelve.open("mydata")
>>> type(shelfFile)
<class 'shelve.DbfilenameShelf'>
>>> shelfFile["cats"]
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()
```
- Just like dictionaries, shelf values have keys() and values() methods that will return list-like values of the keys and values in the shelf.
- Since these methods return list-like values instead of true lists, you should pass them to the list function to get them in list form

#### Saving Variables with the pprint.pformat() Function

#### The shutil Module (Shell Utility)

The shutil module has functions to let you copy, move, rename and delete files in python programs

#### Copying Files and Folders

- Calling the shutil.copy(source, destination) will copy the file at the path source 
to the folder destination. (Both source and destination can be strings or Path objects)
- If destination is a filename, it will be used as the new name of the copied file.
- The function returns a string or Path object of the copied file
- shutil.copytree() will copy an entire folder and ever folder and file contained in it
  - shutil(source, destination), source and destination are both strings. The function returns a string of the path of the copied folder

#### Moving and Renaming Files and Folders

- Calling shutil.move(source, destination) will move the file or folder at the path
  *source* to the path *destination* and will return a string of the absolute path of the new location
- the destination path can also specify a filename, to move and rename the file
- The folders that make up the destination must already exist or python with throw an exception.

#### Permanently Deleting Files and Folders

- You can delete a single file or single empty folder with functions in the OS module, whereas
  to delete a folder and all of its contents, you use the shutil module
- Calling os.unlink(*path*) will delete the file at *path*
- Calling os.rmdir(*path*) will delete the folder at *path*. This folder must be empty of any files or folders
- Calling shutil.removetree(*path*) will remove the folder at *path*, and all files and folders it contains will also be deleted

#### Safe Deletes with the send2trash Module

#### Walking a Directory Tree

#### Compressing Files with the zipfile Module
- Python programs can create and open (or extract) ZIP files using functions in the zipfile module.
- Reading ZIP Files
  - to read the contents of a ZIP file, first you must create a ZipFile object
  - to create a ZipFile object, call the zipfile.ZipFile() function, passing it a string of the .ZIP file's filename
  - zipfile is the name of the python module and ZipFile() is that name of the function
- Extracting from ZIP Files
  - the extractall() method for ZipFile objects extract all the files and folders from a zip file
    from a ZIP file into the current working directory
  - the extract() method for ZipFile objects extract a single file from the ZIP file.
- Creating and Adding to ZIP files
  - to create your own compressed ZIP files, you must open the ZipFile object in *write mode* by passing 'w' as the second argument
  - When you pass a path to the write() method of a ZipFile object, python will compress the file at that path and add it into the ZIP file. The write() method's first argument is a string of the filename to add. The second argument is the *compression type* parameter, which tells the computer what algorithm it should use to compress the files.