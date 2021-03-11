def sleep_in(weekday, vacation):
    if not weekday or vacation:     # weekday == False or vacation == True // return True
        return True
    else:
        return False


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))


def sleep_in2(weekday, vacation):
    if (weekday == False) or (vacation == True):
        return True
    else:
        return False


print(sleep_in2(False, False))
print(sleep_in2(True, False))
print(sleep_in2(False, True))


def sleep_in3(weekday, vacation):
    if weekday == False:
        return True
    if vacation == True:
        return True
    else:
        return False


print(sleep_in3(False, False))
print(sleep_in3(True, False))
print(sleep_in3(False, True))