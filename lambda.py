def double(x):
    return x*2

sequence = [1,3,5,7,9]
doubled = [double(x) for x in sequence] #list comprehensions.
# doubled = map(lambda x:x*2,sequence)

print(doubled)




# print((lambda x,y : x+y)(5,7)) #lambda function
