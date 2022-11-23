## Dictionaries nothing buth json Object
# point = {"x": 1, "y": 2}
point = dict(x=1, z=3)
print(point)
print("z", point["z"])
print("x", point.get("x", 10)) # 1
print("a", point.get("a", 10)) # 10, as a not exist

if "a" in point:
    print("a", point["a"])
else:
    print("x", point["x"])
 
atupples = point.items() # dict_items([('x', 1), ('z', 3)])
print(atupples)