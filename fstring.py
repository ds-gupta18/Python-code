name = "John"
age = 20
language = "Python"
hours = 3

print(name, "is", age, "years old.")
print(name, "is", age, "years old. He studies", language, hours, "hours a day.")

#using f-string
print(f"{name} is {age} years old. He studies {language} hours a day.")

sub1 = 78
sub2 = 87
sub3 = 83

print(f"{name} scored {sub1 + sub2 + sub3} marks in total.")

percent = (sub1 + sub2 + sub3) / 3
print(f"{name} got {percent}%.")