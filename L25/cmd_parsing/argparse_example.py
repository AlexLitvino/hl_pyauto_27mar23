import argparse

parser = argparse.ArgumentParser(prog="Calculator")
#parser.add_help('Program to add two numbers')

#parser.add_argument('counter', help='Counter')
parser.add_argument('--a', help='First number, float', default=0, type=float)
parser.add_argument('--b', help='Second number, float', default=0, type=float)
parser.add_argument('--method', '-m', help='Method, string', default='', type=str, dest='qqq')

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', action='store_true')
group.add_argument('-q', action='store_true')

args = parser.parse_args()
# print(args)
# print(type(args.a))
#print(args.counter)
# print(args.a)
# print(args.b)
a = args.a
b = args.b
#print(args.__dict__['a'])

if args.v:
    print("V")
    print(f"{a} + {b} = {a + b}")
elif args.q:
    print("Q")
    print(a+b)
else:
    print(f"{a} + {b} = {a + b}")
# print(args.__dict__)
# print(args.qqq)
# print(args.method)


