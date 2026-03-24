import re

s1 = "Python is a programming language"

pat = r"[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj)

# ^ (caret) - looks in the starting of the string
pat = r"^[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj)

# $ (dollar) - looks in the end of the string
pat = r"[a-z]{8}$"
match_obj = re.search(pat, s1)
print(match_obj)

#group - ()
emails = "abc_123@example.com random words and characters. x1y2z3.abc.edu"
pat = r"[com]"
match_obj = re.search(pat, emails)
print(match_obj)
