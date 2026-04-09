# *args multiple positional arg 
#when we don't know how many inputs will come  

def add_numbers(*args):
    print(args)
    return sum(args)

print(add_numbers(1,2,3,4))

def create_tags(*tags):
    return list(tags)

print(create_tags("python", "django", "api"))

# **kwargs used when input has dynamic key value pairs

def create_user(**kwargs):
    print(kwargs)

create_user(name='naved',age=28,address='delhi')

# combines both 

def test(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

test(1, 2, 3, name="Naved",age=22)

