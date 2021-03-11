def string_splosion(str):
    refactor = ""
    for i in range(len(str)+1):
        refactor = refactor + str[:i]
    return refactor


print(string_splosion("code"))
print(string_splosion('abc'))
print(string_splosion('ab'))