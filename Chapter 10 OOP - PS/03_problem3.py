class Dummy:
    a = ""


obj = Dummy()
print(obj.a, type(obj.a))
obj.a = 0
print(obj.a, type(obj.a))
