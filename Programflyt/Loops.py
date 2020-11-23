


'''my_list = [1, 2, 3, 4, 5]
for element in my_list:
    print(element)





max_iterations = 10
iteration = 0
while True:
    print("Iteration: " + str(iteration))
    if iteration > max_iterations:
        break
    iteration += 1

'''


'''
# Gang sammen alle partall fra 1 - 10
total = 1
for i in range(1, 10):
    if i % 2 != 0:
        continue
    total *= i
print(total)

'''



start = 5
stop = 10
step = 1

my_range = range(stop)
for i in my_range:
    print(i)