# Dictionary and loops

"""
We have the following dictionary containing details:
user = {
    "user_name" : "my_user",
    "password" : "test@123",
    "email" : "my_use@example.com"
    "address" : "ABC road, 1111111",
    "country" : "Australia"
}
Delete the sensitive information from the dictionary present in the list
sensitive_info = ["password", "address"]
"""

user = {
    "user_name": "my_user",
    "password": "test@123",
    "email": "my_use@example.com",
    "address": "ABC road, 1111111",
    "country": "Australia"
}
# sensitive_info = ["password", "address"]

# for i in sensitive_info:
#     user.pop(i)
#
# print(user)

# # fetch deleted key
# sensitive_info = ["password", "address"]
# for i in sensitive_info:
#     print(f"Key: {i}, Value: {user[i]}")
#     user.pop(i)
#
# print(user)

#fetching a key not present in the dictionary
sensitive_info = ["password", "address", "Phone"]

for i in sensitive_info:
    if i in user:
        print(f"DELETED => Key: {i}, Value: {user[i]}")
        user.pop(i)
    else:
        print(f"{i} not present, cannot delete!")
print(user)
