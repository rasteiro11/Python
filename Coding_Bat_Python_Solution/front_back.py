def front_back(str):
    if len(str) <= 1: # "" ; "a"
        return str
    if len(str) == 2: # "ab"
        return str[1] + str[0]
    else: # "code"
        return str[len(str) - 1] + str[1:len(str)-1] + str[0]


print(front_back("code"))
print(front_back("a"))
print(front_back("ab"))


