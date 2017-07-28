
# i = 0
# numbers = []
#
# while i < 6:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#
#     i += 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is %d" % i)
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)


def while_function(count, step_length):
    i = 0
    numbers = []

    while i < count:
        print("At the top i is %d" % i)
        numbers.append(i)

        i += step_length
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")
    for num in numbers:
        print(num)


print("this is a while-loop test.")
count = int(input("input what count loop you want? "))
step_length = int(input("input what's the step-length you want? "))
while_function(count, step_length)