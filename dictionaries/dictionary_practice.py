x = {
    "a": {
        "b": [
            {"c": "Hello!"}
        ]
    }
}
print(x["a"]["b"][0]["c"])

y = dict(a_string = 900, b = 2, c = 3)

for key in y:
    print(key, end = ", ")
    print(y[key])

print()
for value in y.values():
    print(value)

print()
for key,value in y.items():
    print(key, end = ", ")
    print(value)