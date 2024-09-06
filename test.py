import os

uid="mob"
safe_name="test"
filename = f"/tmp/${uid}/${safe_name}"

os.makedirs(os.path.dirname(filename), exist_ok=True)

f = open(filename, "w")
f.write("This has been written to")
f.close()


g = open(filename, "r")
print(g.read())


