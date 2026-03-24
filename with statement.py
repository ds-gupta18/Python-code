fh = open("practice.txt", 'rt')
contents = fh.read()
fh.close()               #manually needs to be closed
print(contents)

#using with() : ensures automatically closing of file
with open("practice.txt", 'rt') as fh:
    contents = fh.read()

print(contents)

with open("practice2.txt", 'xt') as fh:
    fh.write("New file creation\n")
    fh.write("Bye")
