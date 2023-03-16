def both(*args, **kwargs):  #args and kwargs unlimitted value can be collacted.
    print(args)
    print(kwargs)

both(1,3,5, name="Bob", age=25)

#args collects the args 1,3,5. and then kwargs collects name and age dictionaries.

# def named(**kwargs):  #this keyword is collecting dictionary and save one parameter in it. the normal parameters does not colllect the dictionary for this reason this type code is good.
#     print(kwargs)

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# print_nicely(name="Bob", age = 25)