a =  int(input(" Please write two different number as a: "))
b = int(input(" Please write two different number as b: "))
def my_function(a,b):
     multi = a*b
     return multi

def return_42(a,b):
    result = my_function(a,b)
    return result

result = return_42(a,b)
print(f"   The result is {result} value. ")


def say_hello(name, surname):
     print(f"Hello {name} {surname}!")

say_hello(surname="Bob", name="Smith")  #postitional arguments.