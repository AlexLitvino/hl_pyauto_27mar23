import requests

url = 'https://gorest.co.in/public/v2/users'
headers = {"Accept":"application/json",
           "Content-Type": "application/json",
           "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}

# response = requests.get(url=url, headers=headers)
# print(response)
# print(response.status_code)
# # print(response.json())
# # print(response.content)
# # print(response.text)
# print(response.cookies)


# url = 'https://google.com'
# response = requests.get(url=url, headers=headers)
# print(response)
# print(response.status_code)
# print(response.json())
# #print(response.content)
# #print(response.text)
# # print(response.cookies)
# # print()
# # for cookie in response.cookies:
# #     print(cookie)



# #url = 'https://gorest.co.in/public/v2/users?gender=female&status=inactive'
# url = 'https://gorest.co.in/public/v2/users.xml'
# #params = {'gender': 'female', 'status': 'inactive'}
# params = [('gender', 'female'), ('status', 'inactive')]
# headers = {"Accept": "application/json",
#            "Content-Type": "application/json",
#            "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# response = requests.get(url=url, headers=headers, params=params)
# print(response.status_code)
# # print(response.json())
# # print(len(response.json()))
# print(response.text)


# url = 'https://gorest.co.in/public/v2/users/3271089'
#
# headers = {"Accept": "application/json",
#            "Content-Type": "application/json",
#            "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# response = requests.get(url=url, headers=headers)
# print(response.status_code)
# print(response.json())
# print(len(response.json()))


# url = 'https://gorest.co.in/public/v2/users/'
#
# headers = {"Accept": "application/json",
#            "Content-Type": "application/json",
#            "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# user = {'name': 'Aleksey L2', 'email': 'qwerty3@test.com', 'gender': 'male', 'status': 'inactive'}
#
# response = requests.post(url=url, headers=headers, json=user)
# print(response.status_code)
# print(response.headers)
# print(response.json())


# url = 'https://gorest.co.in/public/v2/users/3271825'
#
# headers = {"Accept": "application/json",
#            "Content-Type": "application/json",
#            "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# user = {'name': 'Aleksey L333'}
#
# response = requests.put(url=url, headers=headers, json=user)
# print(response.status_code)
# print(response.headers)
# #print(response.json())

# url = 'https://gorest.co.in/public/v2/users/3271825'
#
# headers = {"Accept": "application/json",
#            "Content-Type": "application/json",
#            "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}
#
# response = requests.delete(url=url, headers=headers)
# print(response.status_code)
# print(response.headers)
# print(response.json())



# url = 'https://gorest.co.in/public/v2/users'
#
# headers = {"Accept": "application/json",
#            "Content-Type": "application/json",
#            "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c",
#             "Access-Control-Request-Method": "DELETE",
#             "Access-Control-Request-Headers": "origin, x-requested-with",
#             "Origin": "https://gorest.co.in"
#            }
#
# response = requests.options(url=url, headers=headers)
# print(response.status_code)
# print(response.headers)

