# a mode : append mode

fh = open("file2.txt", 'at')
fh.write("\nThis content has been written using 'a' mode.\n")
fh.write("\n'a' mode is used to add new content at the end of a file.\n")
fh.write("GoodBye")

fh.close()

# if a file doesn't exist, it creates the one.
fh = open("file3.txt", 'at')
fh.write("This content has been created using 'a' mode.\n")
fh.write("'a' mode creates the file if th file doesn't exists.\n")
fh.write("GoodBye")

fh.close()