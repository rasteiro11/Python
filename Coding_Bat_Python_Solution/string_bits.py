def string_bits(str):
    final = ""
    for i in range(0, len(str)):
        if i % 2 == 0:
            final = final + str[i]

    return final


print(string_bits("Hello"))
print(string_bits("Hi"))
print(string_bits("Heeololeo"))