dict1 = {"brand": "Ford",
         "model": "Mustang",
         "year": 2016,
         "price": 50000}

print(dict1)
print(len(dict1))
print(type(dict1))

for x in dict1.keys():
    print(x)

for x, y in dict1.items():
    print(x, y)

print(dict1["brand"])

