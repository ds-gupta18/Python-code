#Definning the function
def greeting_someone():
    print("Hello, Good morning!")
    print("It's a beautiful day")

#Calling the function
greeting_someone()
greeting_someone()

#Using arguments:
def greeting_someone(name):
    print(f"Hello {name}, Good morning!")
    print("It's a beautiful day")

greeting_someone('Mark')
greeting_someone('John')

def even_odd(number) :
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(10)
even_odd(11)
even_odd(99)
even_odd (100)


def add (num1, num2):
    result = num1 + num2
    print(f"Result: {result}")

add (10,3)
add(9 , -4)
