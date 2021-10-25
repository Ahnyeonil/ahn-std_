# 튜플
# 리스트와 흡사 - 튜플은 고정 ( Cont ) -> read만 가능
from typing import Union


tup = (1,2,"a","b")
print(tup)
print(tup.count(2))
print(tup.index(2))
# 튜플 전체 변경 가능

# 딕셔너리 - hash, map, object, json
# key, value 존재 (key 값 중복 안됨)
dic = {'name':'Ahn', 'age':'29'}
print(dic['name'])
dic_a = {1: 'a'}
dic_a['name'] = "Ahn"       # key, value 입력시 새로 추가
print(dic_a)
del dic_a[1]                # del - key 값 이용하여 삭제
print(dic_a)
dic_a['age'] = 29
dic_a['adr'] = "korea"
dic_a_key = dic_a.keys()    # key 값
print(dic_a_key)
dic_a_val = dic_a.values()  # value 값
print(dic_a_val)
# ex
for k in dic_a_key:
    print(k)
for v in dic_a_val:
    print(v)
dic_a_item = dic_a.items()  # dic 값
print(dic_a_item)
print(dic_a.get("age")) # key 값으로 value 구하기  
print(dic_a.get("a"))   # 없으면 none
print(dic_a.get("a", "존재하지 않는 값")) # default 설정
print("age" in dic_a)   # key 값 존재 여부
print("Ahn" in dic_a)   # key 값 존재 여부

# 집합 - 원소 고유 -> 중복, 순서가 없음 (set 과 동일)
set_a = set([1,2,3])
set_aa = {1,2,3}
print(set_a)
print(set_aa)
# 예시 ( 리스트의 중복 제거 가능)
ex_list = [1,1,2,2,3,4,4,5,5,5,5]
ex_newList = list(set(ex_list))
print(ex_list)
print(ex_newList)

set_1 = set([1,2,3,4,5,6])
set_2 = set([4,5,6,7,8,9])
print(set_1 & set_2)        # 겹치는 값 (교집합)
print(set_1.intersection(set_2))    # 겹치는 값 (교집합)
print(set_1 - set_2)                # set_1에만 존재하는 값 (차집합)
print(set_1.difference(set_2))      # set_1에만 존재하는 값 (차집합)
print(set_1 | set_2)        # 전체 값 (합집합)
print(set_1.union(set_2))   # 전체 값 (합집합)

set_1.add(7)        # 값 추가
print(set_1)
set_1.update([8,9,10,11])     # 여러 값 추가 (중복 입력시 중복값은 제외하고 추가)
print(set_1)
set_1.remove(7)         # 값 삭제
print(set_1)

# 불 - 참/거짓
# 문자열 - "A" -> True
# 문자열- "" -> False
# 문자열 값 존재 유무에  따라 True, False
# 리스트, 튜플, 딕셔너리 동일
# 숫자 1 = 참, 0 = 거짓
# None = 거짓
bool_1 = True
bool_2 = False
if bool_1:
    print("bool_1 : TRUE")
else:
    print("bool_1 : FALSE")

if bool_2:
    print("bool_2 : TRUE")
else:
    print("bool_2 : FALSE")

if "hello":         # 참(문자열 존재)
    print("hello")  # 출력

list_a = [1,2,3,4]
while list_a:       # list 존재하지 않을때까지 반복
    list_a.pop()
    print(list_a)

# 변수
# 파이썬에서 사용하는 변수는 객체를 가리키는 것
# pythontutor.com 참고 - 시각적으로 흐름을 보여줌

a = [1,2,3]
b = a
print(a)
print(b)
a[0] = 4
print(a)
print(b)
# a가 b에 복사가 아니라 같은 주소의 값을 바라보고 있는것

print(id(a))        # 주소값
print(id(b))        # 주소값

print(a is b)       # 같은 주소값 바로보고 있는지 여부 (true or false)

# 복사방법 copy() - 슬라이싱과 동일 (값을 복사함) (기본적으로는 주소를 복사)
# 새로운 메모리에 저장
b = a[:]            # 슬라이싱 하여 하나씩 넣어줌
a[0] = 1
print(a)            # 슬라이싱하여 따로 값을 넣어줌으로써 다르게 출력
print(b)

print(id(a))        # 주소값이 다름
print(id(b))        # 주소값이 다름

tup_a, tup_b = ('python', 'life')
# (tup_a, tup_b) 와 동일
#['python', 'life'] 와 동일
# a = b = 'hello'

print(tup_a)
print(tup_b)

# 다른 언어에서 변수 바꾸는법
python_a = 3
python_b = 5
print(python_a)
print(python_b)
tmp = python_b
python_b = python_a
python_a = tmp
print(python_a)
print(python_b)
# 파이썬
py_a = 3
py_b = 5
print(py_a)
print(py_b)
#변경
py_a, py_b = py_b, py_a
print(py_a)
print(py_b)