list_ = ['invoker is best mider ']
for i in list_:
    b = i.split()
    max_ = b[0]
    for x in b:
        if len(max_) < len(x):
            max_ = x
print(max_) 

