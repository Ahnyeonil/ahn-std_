# 조건문
money = True
if money:       # 들여쓰기 맞춰야됨
    print("택시")
else:
    print("도보")

# 비교
a_if = 1
b_if = 2
if a_if > b_if:
    print("a_if!")
else:
    print("b_if")
# and or
a_or = 1
b_or = 2
if 1 == a_or or b_or == 1: # or == |
    print("same")
else:
    print("dif")
if 1 == a_or & b_or == 1: # and == &
    print("same")
else:
    print("dif")
# in
a_in = 1
if a_in in[2,3]:
    print("in")
else:
    print("not in")
# pass
if True:
    pass
else:
    print("false")
# elif
a_elif = 2  # else if -> elif
if a_elif < 0:
    print("-")
elif a_elif == 1:
    print("1")
elif a_elif == 2:
    print("2")
else:
    print("3")
# 조건부 표현식
score = 70
message = "success" if score >= 60 else "failure"
print(message)

# 반복문
# while
count = 0
while count < 10:
    print("count는 " + str(count))
    if count > 5:
        print("count는 추가됩니다 " + str(count))
        count = count + 1
        if count == 8:
            print("count는 " + str(count) + "입니다.")
            break
    else:
        count = count + 2
# for
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for i,j in a:
    print(i)
    print(j)

# range
sum = 0
for i in range(1, 11):   # range -> 1이상 11미만
    sum = sum + i
    print(sum)
print("결과물은 " + str(sum))

# 구구단
for i in range(2, 10):
    print(str(i) + "단")
    for j in range(1, 10):
        print(i*j, end=" ")
    print(" ")

# 리스트 내포
# 따로 공부