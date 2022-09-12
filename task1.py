op = ["--x", 'x++', "x++"]
x = 0
for i in op:
    if i == '--x':
        x = x - 1
        print(x)
    elif i == 'x++':
        x = x + 1
        print(x)
print(x)        