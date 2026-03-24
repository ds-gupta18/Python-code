# comma separated key-value pairs enclosed within {}
# {key1:value1, key2:value2, ......}

groceries = {'milk': 60, 'biscuits': 20, 'rice': 90, 'bread': 30}
print(groceries)
print(type(groceries))
print(len(groceries))
print(groceries['milk'])

# Dict are mutable
groceries['milk'] = 65 #updates the value
print(groceries)

#addinng new key-pair
groceries['Egg'] = 10
print(groceries)



