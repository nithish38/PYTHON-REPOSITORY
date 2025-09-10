d={"Eno":3872,"Ename":"Minato"}
print(d)
print(d["Eno"])
print(d["Ename"])
print(d.get("Ename"))
d["Ename"]="nithish"
print(d)
d=[age]=18
print(d)
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,value)
d.pop("Ename")
print(d)
d.popiteam()
print(d)
d.clear()
print(d)