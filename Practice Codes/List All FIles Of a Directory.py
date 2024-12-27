#How to list all files of a directory in python
from os import listdir #Used to list all entrys in a specific directory
from os.path import isfile , join#

file_list = [f for f in listdir('/Users') if isfile(join('/Users',f))]



'''listdir('/Users'): This function call retrieves a list of all entries (both files and directories) in the /Users directory.
for f in listdir('/Users'): This iterates over each entry f returned by listdir.
join('/Users', f): This combines the directory path (/Users) with the filename (f) to create the full path to the file.
isfile(join('/Users', f)): This checks if the full path corresponds to a file. Only entries that are files will pass this check.
The resulting list comprehension creates a list of all files in the /Users directory and assigns it to file_list.'''