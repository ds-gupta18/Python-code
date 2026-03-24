import re

message = "The current Python version is 3.13. Other versions are 3.12, 3.11, 3.10"

match_object = re.search("[0-9][0-9]", message)  #[0-9}{0-9}- 2 consecutive digit
print(match_object)

match_object = re.search("[0-9][0-9]", "House number : 251/A")
print(match_object)

match_object = re.search("[0-9][0-9][0-9]", "House number : 251/A")
print(match_object)

# DOT (.) - matches any character except new line character(\n)

match_object = re.search("[0-9].[0-9][0-9]", message)
print(match_object)

match_object = re.search("[0-9].[0-9]", message)
print(match_object)

match_object = re.search("[0-9].[0-9]", "House number : 251/A")
print(match_object)

message_1 = "The year is 2026"
match_object = re.search("[0-9].[0-9][0-9]", message_1)
print(match_object)

match_object = re.search("[0-9][.][0-9][0-9]", message_1)
print(match_object)

match_object = re.search("[0-9][.][0-9][0-9]", message)
print(match_object)
