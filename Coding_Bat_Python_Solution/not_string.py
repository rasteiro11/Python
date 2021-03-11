def not_string(str):
    if str[:3] == "not":
        return str
    else:
        return "not " + str

print(not_string("not candy"))
print(not_string("hot"))

      #012345
str = "not Danilo"
print(str[0:2])
print(str[:3])
print(str[:2])
print(str[0])
print(str[2])
print(len(str))
print(str[0:3])

def not_string(str):
    if 'not' not in str[:3]:
        return 'not ' + str
    else:
        return str


