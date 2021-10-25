#함수
def sum(a, b):
    result = a + b
    return result

# *
def sum_reandom(*args):     # * 갯수 마음대로
    result = 0
    for i in args:
        result = result + i
    return result
print(sum_reandom(1,2,3,4,5,6))

# **
def print_keyword(**kwargs):        # ** key, value
    info = ''
    for k in kwargs.keys():
        if(k == 'name'):
            info = info + "My Name is " + kwargs.get('name')
    return info
print(print_keyword(name="Ahn", age="29"))

# return 여러개
def sum_mul(a,b):       # 리턴여러개 가능(index로 값 가져올 수 있음)
    return a+b,a*b
print(sum_mul(1,2)[0])

# 파라미터 설정
def info(name, age, man=True):                  # default 값 설정 가능
    print("나의 이름은 " + name + " 입니다.")
    print("나이는 " + str(age) + "살입니다.")
    if man:
        print("남자입니다.")
    elif man == True:
        print("남자입니다!")
    else:
        print("남자가 아닙니다.")
info("Ahn", 29)
info("Ahn", 29, True)
info("Ahn", 29, False)

# global
glo = 1
def glob():
    global glo      # 전역변수로 설정
    glo = glo + glo
    return glo
glo = glob()
print(glo)

# lambda
def lam_add(a,b):
    return a+b
add = lambda a,b: a+b
print(add(1,2))
# List에서 lambda
myList = [lambda a, b : a + b, lambda a, b : a * b]
print(myList[0](1, 2))
print(myList[1](32, 0))

#입력, 출력
inner = input("아무거나 입력하세요 : ")
print("life", "is", "too short")        # ,를 넣으면 띄어쓰기 // 없으면 붙여서 출력0

for i in range(10):
    print(i, end=(' '))     # end는 문자 나눌때
print("\n")

#파일 쓰기 "w"쓰기, "r"읽기, "a"추가하기
f = open("새파일.txt", "w",  encoding="UTF-8")
for i in range(11):
    data = str(i) + "번쨰 줄입니다.\n"
    f.write(data)
f.close()

#파일 읽기 한줄
ff = open("새파일.txt", "r", encoding="UTF-8")
line = ff.readline()
print(line)
ff.close()

#파일 읽기 여러줄
fff = open("새파일.txt", "r", encoding="UTF-8")
while True:
    line_ = fff.readline()
    if not line_: break
    print(line_.strip("\n"))
fff.close()