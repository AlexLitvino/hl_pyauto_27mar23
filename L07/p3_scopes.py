"""
LEGB (LNGB)
Local
Enclosed (Non-local)
Global
Built in
"""

# #a = "sddsds 34ewfwf dssdf"
# #a = [1, 2, 4]
# a = 34
# def func():
#     #a = "add fdffa ettgetgwww"
#     #a.split()
#     #a.append(121212)
#     global a
#     a += 3
#     print(f"a in func: {a}")
# print(f"Global a: {a}")
# func()
# print(f"Global a: {a}")
#
# is_first_test = True
#
# def start():
#     if is_first_test:
#         print("Sleep")
#     global is_first_test
#     is_first_test = False

a = 111
print(len([3,3,4]))
def external():
    a = 222
    print(a)
    #print(len([3, 3, 4]))
    len = 555
    def internal():
        nonlocal a
        print(len)
        #print(len([3, 3, 4]))
        #a = 333
        a += 100
        print(a)
    internal()
    print(a)

external()
print(a)
print(len([3, 3, 4]))