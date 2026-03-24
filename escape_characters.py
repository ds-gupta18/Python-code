# \n - new/next line
# \t - tab
# \\ - backslash
# \' - inserts a single quote inside a single-quoted string

# \n
print("Hello everyone. \nHow old are you?")

#\t
print("John 20")   #space dist
print("John\t20")  #tab dist

#\\
#print("new\old")   #printed with warning
print("new\\old")   #printed without any warning

#\'
#print('This is Python's class')  #error
print('This is Python\'s class')
print("This is Python's class")

#\"
#print("He says,"we are learning Pyton"") #error
print("He says,\"we are learning Pyton\"")
