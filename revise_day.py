# how to take input from user
# how to collect multiple errors and return them in a response

name = input('Enter your name: ')
age = int(input('Enter your age: '))
email = input('Enter your email: ')
print(len(name))
# if len(name) > 2 and '.' in email:
#     response = {
#         'status': 'success',
#         'message': 'You are eligible to access the content.'
#     }
# else:
#     response = {
#         'status': 'error',
#         'message': 'You are not eligible to access the content.'
#     }

# print(f'Hello, {name}! You are {age} years old.')
# print(response)

# muliple errors
errors = []
if(len(name) <= 2):
    errors.append('Name must be more than 2 characters.')


if age < 18:
    errors.append('You must be at least 18 years old.')

if '@' not in email and '.' not in email:
    errors.append('Email must contain @ symbol.')
if(len(errors) > 0):
    response = {
        'status': 'error',
        'message': errors
    }
else:
    response = {
        'status': 'success',
        'message': 'You are eligible to access the content.'
    }

print(response)