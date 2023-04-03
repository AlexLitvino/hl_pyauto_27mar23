# i = 5.5
# while i >= 0:
#     print(i)
#     i -= 1
# print("END")

# import time
# i = 1
# while True:
#     print(i)
#     i += 1
#     #time.sleep(0.5)
#     if i > 7:
#         break
# else:
#     print("In else")


# i = 5.5
# while i >= 0:
#     print(i)
#     i -= 1
#     if i > 3:
#         break
# else:
#     print("In else")
# print("END")


while True:
    n = input("Enter n")
    if n == 'q':
        break
    elif n == '':
        continue
    try:
        print(int(n) * int(n))
    except ValueError:
        print("Enter int value")

print("END")