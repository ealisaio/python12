# def cube(n):
#     return n*n*n
# lam = lambda n : n*n*n
# print("this is using normal function", cube(5))
# print("this is lambda function", lam(6))

# gs = lambda a,b : a if a>b else b
# print(gs(1,2))

# Decorator implimentation
"""def check_age(func):
     def wrapper(age):
        if age >= 18:
            print("Age checked:you are old enough to vote")
            return func(age)
        else:
            print("age checked: you cannot vote")
     return wrapper
def age_show(age):
    print("voting system check")
decorated_function = check_age(age_show)
print(decorated_function(20))
print()"""


# Decorator function
def check_age(func):
     def wrapper(age):
        if age >= 18:
            print("Age checked:you are old enough to vote")
            return func(age)
        else:
            print("age checked: you cannot vote")
     return wrapper
@check_age
def age_show(age):
    print("voting system check")
age_show(20)
# decorated_function = check_age(age_show)
# print(decorated_function(20))
print() 

        

