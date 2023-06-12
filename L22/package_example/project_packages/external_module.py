import sys

print(sys.path)
# sys.path.append(r'/home/olytvynov/Projects/HL/hl_pyauto_27mar23')
# print(sys.path)

#from project_packages.internal.internal_functions import add_q
from project_packages.internal.internal_functions import add_q, mlp_q
#import project_packages.internal.internal_functions as p

print(add_q())
print(mlp_q)
