#Local variable is preferred in higher position than global variable

n = 1 #global variable

def fn():
    n = 5        #local variable
    print('in', n)

fn()

print('out', n)



n = 1  # global variable

def fn():
    global n
    n = 5  # local variable
    print('in', n)


fn()

print('out', n)
