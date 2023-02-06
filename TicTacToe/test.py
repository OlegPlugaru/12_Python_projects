name = "Jab,rils"
name = name.lower()
print(name)
name = name.upper()
print(name)

name = name.split(",")
print(name)

name = "I like the space ship"
does = name.__contains__('the')
print(does)

if "the" in name:
    print(does)