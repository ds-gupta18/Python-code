# x mode => create a file

fh = open("file1.txt", 'xt')  #xt by default

# Writing into a file
# write(content)
fh.write("This file is created using 'x' mode in Python.\n")
fh.write("Next line.")

# Closing a file
fh.close()
fh = open("file.txt", 'xt')
# fh.write("Test content") - gives error
#Any operation after closing a file isn't allowed
# If a file that we are creating already exists, that file can't be recreated again
