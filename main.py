import urllib.request

req = urllib.request.urlopen('https://ghibliapi.herokuapp.com/species').read()

# byte -> str
str_req = req.decode()

# 種族 "Cat" に関するデータを先頭にする
length1 = str_req.find('"Cat"')
str_req = str_req[length1:]

# 要素 "films" に関するデータのみを抽出
length2 = str_req.find('"films"')
length3 = str_req.find('}')
length4 = len(str_req)
number_del = length3 - length4
str_req = str_req[:number_del]
str_req = str_req[length2:]
print(str_req)


