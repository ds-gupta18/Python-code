"""
Opening a file in  python : open(file_name, mode_to_open)
modes: r(read), w(write), x(create), a(append), t(text file), b(binary file)
rt is th default mode
"""

file_handler = open("practice.txt", 'rt')
print(file_handler)
#Read operation

#Closing a file
file_handler.close()
print(file_handler)
