# 숫자

a = 3
b = 4
print(a+b)      # 더하기
print(a*b)      # 곱하기
print(3/4)      # 나누기
print(3 % 4)    # 나머지
print(3 ** 4)   # 제곱

# 문자열

# \n    : 문자열 안에서 줄 바꿈
# \t    : 문자열 안에서 탭 사용
# \\    : 문자열 안에서 \ 사용
# \'    : 문자열 안에서 ' 사용
# \"    : 문자열 안에서 " 사용
aa = "Python'''' is'''' map''''.''''"
bb = 'Python\'\'\'\' is\'\'\'\' map\'\'\'\'.\'\'\'\''
cc = """Python
is
map"""      # """, ''' 문자열 입력한대로 출력
dd = "Python"
ee = " is map"
print(aa)
print(bb)
print(cc)
print(dd + ee)

# 인덱싱, 슬라이싱

index_a = "Life is too short, you need Python."
print(index_a)
print(index_a[1])       # 인덱스
# 슬라이싱 ([x:y:z]) - x : 시작(이상) y : 끝(미만) z : 간격
print(index_a[0:8])     # 슬라이싱 - 0부터 8전까지
print(index_a[::2])     # 간격 2로

count = 33
cnt = "print : " + str(count)   # str + int 안됨
print(cnt)
print(index_a)

# 문자열 자료형
str_arr = "Python"
print(str_arr.find('P'))    # find (문자 없을시 -1)
print(str_arr.index('P'))   # index (문자 없을시 error)
print(str_arr.find('p'))
print(str_arr.index('n'))
str_join = ",".join("abcd")     # ,를 구분으로 abcd 삽입
print(str_join)                 # 결과(a,b,c,d)
str_lo = "lower"
str_up = str_lo.upper()            # 소문자 -> 대문자로 // lower 대문자 -> 소문자로
print(str_lo)
print(str_up)
str_st = " strip "
str_stp = str_st.strip()            # strip -> 공백제거
print(str_st)
print(str_stp)
str_rep = "a is A, b is B"
str_replace = str_rep.replace("a", "에이")  # replace 문자열 치환
str_replace = str_rep.replace("b", "비")
print(str_rep)
print(str_replace)
str_spl = "a,b,c,d"
str_split = str_spl.split(",")      # 해당 문자로 문자열을 나눔 - 기본값() 공백으로
print(str_split)

# 리스트
str_list = ["apple", "bdd", "bdd", "chovy", "dove", "effort"]
print(str_list)
print(str_list[0])
print(str_list[0] + str_list[1])
str_list.append("faker")        # append 맨뒤 추가
print(str_list)
print(str_list.reverse)         # reverse 뒤집기
str_list.insert(2, "teddy")     # insert 해당 인덱스에 값 추가
print(str_list)
str_list.remove("bdd")          # remove 해당 값 삭제
print(str_list)
str_list.pop()                  # pop 마지막 삭제
print(str_list)
str_count = str_list.count("dove")  # 해당 값의 갯수
print(str_count)
str_list.extend(["keria", "oner"])
print(str_list)

del str_list[0]                 # 0번 삭제
print(str_list)