import re

message = "The current Python version is 3.13. Other previous versions are 3.12, 3.11, 3.10"

pattern = r"[a-z]{4}"     #r"[a-z][a-z][a-z][a-z]"
match_obj = re.search(pattern, message)
print(match_obj)

pattern = r"[A-Z][a-z]{5}"
match_obj = re.search(pattern, message)
print(match_obj)

pattern = r"[A-Z][a-z]{2,5}"     #between 2 & 5 character
match_obj = re.search(pattern, message)
print(match_obj)


# (+)- matches 1 or more repetitions of the prev pattern
pattern = r"[A-Z][a-z]+"
match_obj = re.search(pattern, message)
print(match_obj)

# (?) - 0 or 1 repetitions of the previous pattern
pattern = r"[A-Z][a-z]?"     #r"[a-z][a-z][a-z][a-z]"
match_obj = re.search(pattern, message)
print(match_obj)

# (*) - 0 or more repetitions of the previous pattern
pattern = r"[A-Z][a-z]*"     #r"[a-z][a-z][a-z][a-z]"
match_obj = re.search(pattern, message)
print(match_obj)