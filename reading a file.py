file_handler = open("practice.txt","rt")

# # 1.Read operation
# # read() : reads the contents of the file as string
# content = file_handler.read()
#
# # closing a file : close()
# file_handler.close()
#
# print(content)
# print(type(content))

# # 2.Read operation (fixed number of characters)
#
# content = file_handler.read(10)  #reads 1st 10 characters of file
#
# # closing a file : close()
# file_handler.close()
#
# print(content)
# print(type(content))

# # 3. Reading a line
#
# line1 = file_handler.readline()
# line2 = file_handler.readline()
# line3 = file_handler.readline()
# line4 = file_handler.readline()   #empty string : reached EOL
#
# file_handler.close()  # returns line with next line (\n)
#
# print(f" line1 : {line1}")
# print(f" line2 : {line2}")
# print(f" line3 : {line3}")
# print(f" line4 : {line4}")


# 4. Reading multiples lines at once : readlines()
lines = file_handler.readlines()

file_handler.close()

print(f'lines: {lines}')
print(type(lines))

for line in lines:
    print(line.rstrip('\n'))


