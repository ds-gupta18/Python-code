try:
    with open("my_file.txt", 'rt') as fh:
        data = fh.read()

    print(data)
except FileNotFoundError as file_err:
    print("File you are trying to open doesn't exist")
    print(file_err)

#else: block will be executed when there's no any error in try block
else:
    print(data)


try:
    with open("file1.txt", 'rt') as fh:
        data = fh.read()

except FileNotFoundError as file_err:
    print("File you are trying to open doesn't exist")
    print(file_err)
else:
    print(data)


import io
try:
    fh = open("my_file10.txt", 'wt')
    data = fh.read()
    fh.close()

except FileNotFoundError as file_err:
    print("File you are trying to open doesn't exist")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)
finally:                   #always executed
    print("finally block")



import io
try:
    fh = open("my_file10.txt", 'wt')
    fh.read("Hello")

except FileNotFoundError as file_err:
    print("File you are trying to open doesn't exist")
    print(file_err)
except io.UnsupportedOperation as io_err:
    print(io_err)
else:
    print("else block")
    print(data)
finally:
    print("finally block")
    fh.close()
