def extendList(val, list=[]):
    list.append(val)
    return list

print(extendList(10, []))
print(extendList(20, []))
print(extendList(123))
print(extendList('a'))