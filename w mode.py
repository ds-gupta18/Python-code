# w mode : open the file for writing. Overwrites the file

fh = open("file1.txt", 'wt')   #changes the content of file1 (overwrites)
fh.write("This file is overwritten using 'w' mode in Python.\n")
fh.write("Have a nice day!")
fh.close()

#create a new file, if a file does not exist.
fh = open("file2.txt", 'wt')   #changes the content of file1 (overwrites)
fh.write("This file is created using 'w' mode in Python.\n")
fh.write("Have a nice day!")
fh.close()