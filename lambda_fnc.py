# Lambda/Anonymous function : passing argument & expression in single line

def add(a):
    return a + 1
res = add(1)
print(res)

#syntax : lambda argument : expression

func = lambda a : a + 1
res = func(1)
print(res)


def add(a, b):
    return a + b
res = add(8,10)
print(res)

fnc = lambda a, b: a + b
result = add(8,10)
print(result)