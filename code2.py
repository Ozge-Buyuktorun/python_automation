# numbers = [4,6,8,9,12]
# doubled = [x * 2 for x in numbers] #short write method

# print(doubled)

friends = ["Özge", "Mert", "Berk", "Özgür", "Özlem"]
start= [friend for friend in friends if friend.startswith("Ö")]


# for friend in friends:
#     if friend.startswith("Ö"):
#         start.append(friend)
print(start)