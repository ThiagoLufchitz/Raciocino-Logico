# def A(x,y,z):
#     x[y] = z
#     return x
# def B(x,y):
#     del x[y]
#     return x
# def C(x,y):
#     for i, j in x.items():
#         if j[0] == y:
#             return j[1]
#     return

# agenda = { 1:["maria","(41) 3271-3000"],
#           2:["joao","(41) 3271-4000"],
#           3:["jose","(41) 3271-5000"]}

# a,b,c = ["juca","(41) 3271-6000"],3,4 

# agenda= A(agenda,b,a)
# print(agenda)
# agenda = A(agenda,c,a)
# print(agenda)
# agenda = B(agenda, b-1)
# print(agenda)
# aux = C(agenda,a[0])

# print(aux)

# dict1 = {1:"a",2:"b",3:"c"}
# dict2 = {"key4":"d", "key5":"e"}
# dict3 = {"f": "f"}

# del dict1[1]
# print(dict1)

# dict3["f"] = 4
# print(dict3)
# dict3["f"] = "d"
# print(dict3)
# print(dict2)

val = 0

while val < 5:
    print(val)
    val = val + 1
print(val)
for i in (1,2,3,4):
    val = val + 2
    print(val)
print(val)