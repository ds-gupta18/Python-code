import re

s1 = "python is a programming Language. python3.13 is the current version."

#[A-Z], [a,z]
pat = r"[a-z][a-z]"
match_obj = re.search(pat, s1)
print(match_obj)

pat = r"[A-Z][a-z][a-z]"
match_obj = re.search(pat, s1)
print(match_obj)

#\d and \D
#\d matches 1 digit character. it is similar to [0-9]
pat = r"[a-z][a-z][a-z]\d"
match_obj = re.search(pat, s1)
print(match_obj)

#\D matches 1 NON-digit character. it is similar to [0-9]
pat = r"[a-z][a-z][a-z]\D"
match_obj = re.search(pat, s1)
print(match_obj)

#\s, \S
#\s - matches aby whitespace character, tab and new line
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat, s1)
print(match_obj)

s2 = """Hi there
We are learning Python
"""
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat, s2)
print(match_obj)

#\S - opposite of \s. matches any character except space, \t, \n
pat = r"[a-z][a-z][a-z]\S"
match_obj = re.search(pat, s2)
print(match_obj)

#\w - matches [a-z], [A-Z], [0-9]
pat = r"[a-z][a-z][a-z]\w"
match_obj = re.search(pat, s2)
print(match_obj)

# \W - opposite of \w. matches a char except [a-z], [A-Z], [0-9]
pat = r"[a-z][a-z][a-z]\W"
match_obj = re.search(pat, s2)
print(match_obj)