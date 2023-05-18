# MALE = "male"
# FEMALE = "female"
#
# # color
# RED = "red"

WELCOME_SCREEN_NEXT_BUTTON = ""



import enum

#@enum.unique
class StatusCode(enum.IntEnum):
    OK = 200
    SUCCESSFUL = 200
    CREATED = 201
    NOT_FOUND = 404

code1 = StatusCode.OK
if StatusCode.NOT_FOUND == code1:
    print("Equal")

print(StatusCode.OK.name)
print(StatusCode.OK.value)
print(StatusCode.SUCCESSFUL == StatusCode.OK)

print(StatusCode.OK > StatusCode.CREATED)

"""
import configparser
[Testing]
base_url = http://google.com
"""