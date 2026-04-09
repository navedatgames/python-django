# name = 'test'
# print(f'Hello {name}')


# age =18

# def check_el(age):
#     if age>=18:
#         return 'valid'
#     else:
#         return 'invalid'
    
# print(check_el(age))

# default param at last of function 
# def check(name,role='admin')

tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Build API", "completed": False},
]
def add_task(task):
    tasks.append(task)

def get_task():
    return tasks

def mark_complete(task_id):
    for task in tasks:
        if(task_id == task["id"]):
            task["completed"] = True

add_task({"id": 3, "title": "new", "completed": False})

def get_completed_tasks():
    return [task for task in tasks if task['completed']]

mark_complete(1)
print(get_completed_tasks())