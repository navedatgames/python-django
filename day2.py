list = [1,2,3]
print(list)
print(type(list))

# #dictinaries
# obj = {"name":'test',"age":22}
# print(obj["name"])

# #conditions

# age = 18
# if(age>=18):
#     print('he can vote')
# else:
#     print("he can't vote")


# #Loops
# # for i in range(5):
# #     print(i)


# #functions

# def sum(a,b):
#     return a+b

# print(sum(1,3))

# #list
# users = ["Amit", "Rahul", "Sara"]

# users.pop()

# for i in users:
#     print(i)

#let build a task manager cli

# tasks = []

# def add_tasks(task):
#     tasks.append(task)

# def show_tasks():
#     for i in tasks:
#         print(i)

# add_tasks("get up")
# add_tasks("write code")
# add_tasks("sleep")

# show_tasks()

# name = 'coding'
# print(f'hello {name}') # new way


# condition using and operator 

# email = 'test@yopmail.com1'
# pasword = '123'

# if email == 'test@yopmail.com' and pasword == '123':
#     print('login succes')
# else: 
#     print('login failed')

# # assingnement
# name = input("Enter your name")
# age = int(input('Enter your age'))
# sal = int(input("Enter you sal"))

# print(f'Hi, {name} your age is {age} and salary is {sal} and in 5 years your salry will be {sal*1.5}')

# array of data's

users = [
    {"id": 1, "name": "Amit"},
    {"id": 2, "name": "Rahul"},
    {"id": 3, "name": "Sara"}
]

# conditions and loops 
for i in users:
    if(i["id"]==2):
        print(i["name"])

# if we want to just get name and store in names

names = [user["name"] for user in users]
print(names)

active_users = [
    {"id": 1, "name": "Amit", "is_active": True},
    {"id": 2, "name": "Rahul", "is_active": False},
    {"id": 3, "name": "Sara", "is_active": True},
]

# filtering 
filtered = [user for user in active_users if user["is_active"]== True and user["id"] ==1]
print(filtered)

tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Build API", "completed": True},
    {"id": 3, "title": "Learn Django", "completed": False},
]

count = 0
for task in tasks:
    if(task["completed"] != True):
        count = count +1

print(count)