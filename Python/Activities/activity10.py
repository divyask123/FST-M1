num_tuple = (100, 200, 330, 460, 550)
print("Given list is ", num_tuple)

print("Elements that are divisible by 5:")
for num in num_tuple:
    if (num % 5 == 0):
        print(num)