r"C:\temp"


import re

string = "Hello, hello, hello, how low?"
pattern = r"\b[a-zA-Z]{3}\b"

result = re.findall(pattern, string)
#print(result)

# re_obj = re.compile(pattern)
# result = re_obj.findall(string)
# print(result)


text = """
<link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
<link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
<link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
"""

# pattern = r'href=".+"'
# result = re.findall(pattern, text)
# print(result)
#
# pattern = r'href="(.+)"'
# result = re.findall(pattern, text)
# print(result)

# pattern = r'rel="(.+)" href="(.+)"'
# result = re.findall(pattern, text)
# print(result)


# pattern = r'rel="(.+)" href="(.+)"'
# result = re.search(pattern, text)
# print(result)
# print(result.group())

str = "4,4,[2,7,3]"
result = re.split("[\[,\]]", str)
print(result)

# text = """Line1
# Line2 ПРивет
# Line3
# """
# result = re.findall(r"\b\w*\b", text, flags=re.ASCII | re.IGNORECASE)
# print(result)
# print([i for i in result if i])
# print(list(filter(None, result)))

# TODO: do something
# FIXME: fix it
# HELPME

