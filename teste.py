lista = ['7', '9', '6', '5', '9', '10', '7', '8', '10', '7',
         '7', '6', '6', '10', '6', '6', '7', '10', '9', '10',
         '7', '8', '10', '9', '8']

dic = {}

for item in lista:
    if item not in dic:
        dic[item] = 1
    else:
        dic[item] = dic[item] + 1

print(dic)