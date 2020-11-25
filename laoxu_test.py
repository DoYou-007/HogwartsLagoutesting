a = {'name': 'idoxu', 'sex1': 'male', 'age1': 30}

b = {'name': 'idoxu1', 'sex': 'male', 'age': 30}


# d = eval(a)
# e = str(b)
# print(d,type(d))
# print(e,type(e))

# a.update(b)
# print(a)

def total(a: dict, b: dict):
    for key, value in b.items():
        if key in a.keys():
            a[key] = [a[key], b[key]]
        else:
            a[key] = value
    return a


print(total(a, b))
