#list 
# users = ["Amit", "Rahul", "Sara"]
# print(users[-2])

# how stored in backend
# users = [
#     {"id": 1, "name": "Amit", "is_active": True},
#     {"id": 2, "name": "Rahul", "is_active": False},
#     {"id": 3, "name": "Sara", "is_active": True},
# ]

# #loops
# # for i in users:
# #     print(i['name'])

# count = 0
# #FILTERS
# for i in users:
#     if i["is_active"]:
#         count +=1
#         print(i["name"])

# print(count)

# # pro level
# titles = [user["name"] for user in users ]
# print(titles)

# # to append 
# users.append()

#dic
user = {"name":'naved'}

print(user.get("name"))
print(user.get("age", 0))      # Default value
print(user)

#add update
user["name"] = "khan"
user["email"] = 'test@yopmail.com'

print(user)

# del
del user["name"]
print(user.items())

# loops
for key, val in user.items():
    print(key,val)

users = [
    {"id": 1, "name": "Amit", "is_active": True},
    {"id": 2, "name": "Rahul", "is_active": False},
    {"id": 3, "name": "Sara", "is_active": True},
]




