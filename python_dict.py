def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)
            


a = {'a':{'b':{'c':'d'}}}

for key, value in recursive_items(a):
    print(key, value)
