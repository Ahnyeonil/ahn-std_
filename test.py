print("for")
for i in range(8):
    print(str(i+2) + "단")
    for j in range(9):
        print(str(i+2) + " * " + str(j+1) + " = " + str((i+2)*(j+1)), end=" ")
    print("")

i = 2
print("while")
while i < 10:
    j = 1
    print(str(i) + "단")
    while j < 10:
        print(str(i) + " * " + str(j) + " = " + str(i * j), end=" ")
        j = j + 1
    i = i + 1
    print("")

# 리스트
x = [5,2,3,4]
y = ["g", "b", "a", "d"]

print(x[2])
print(y)

num_ele = len(x)
print(num_ele)

z = sorted(y)
print(y)
print(z)

for n in y:
    print(n)

print(x.index(3))
if 3 in x:
    print(x)

# 튜플
q = (3,2,3,4)
w = ("q", "w", "e", "r")

print(q)
print(w)

# 딕셔너리
a = {"name" : "Ahn", "age" : 29}

print(a)
print(a["name"])
print(a["age"])

for key in a:
    print(key)