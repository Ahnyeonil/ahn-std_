# 예외처리
# try : 오류가 발생할 수 있는 구문
# except Exception as e : 오류 발생
# else : 오류 발생하지 않음
#finally : 무조건 마지막에 실행

try:
    4/0
except Exception as e:
    print(e)
else:
    data = 4/1
    print(data)
finally:
    print("__나누기__")

# 무조건 에러남 ( 자식 클래스에서 변형하여 사용 하도록 )
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

class Duck(Bird):
    pass

eagle = Eagle()
eagle.fly()

duck = Duck()
duck.fly()

# 내장함수
# 예 : print(), abs() 등등
# print() - 출력
# abs() - 절대값
# all() - 모두 참인지
# any() - 하나라도 참이 있는가
# chr() - ASCII 코드를 입력받아 문자로 출력
# dir() - 리스트에서 쓸 수 있는 명령어 모음
# divmod() - 몫과 나머지를 튜플 형태로 돌려줌
# divmod() - 몫과 나머지를 튜플 형태로 돌려줌
# enumerate() - 열거하다 (list를 index,value 형태로)
# eval() - 실행 후 결과값을 돌려줌
# filter() - 함수를 참인것만 남겨줌 (ex- list[-1,0,1,2,-2] 를 filter(양수만 뽑는 함수(리스트)) 실행시키면 1,2만 남음)
# id() - 주소값
# input() - 사용자 입력 받는 함수
# int() - 문자열을 10진수로
# len() - 문자열 길이
# list() - 문자열 리스트로 변환
# map() - 각 요소가 수행한 결과를 돌려줌
# max() - 최대값
# min() - 최소값
# open() - 파일열기
# pow() - 제곱한 결과값 반환
# range() - 범위
# round() - 반올림
# sorted() - 정렬
# str() - 숫자 문자열로
# tuple() - 튜플로 변환
# type() - 타입을 출력
# zip() - 자료형을 묶어주는 역할

#  외장함수 - 라이브러리에서 가져오는 함수 (import 해서 사용)
# time() - 시간
# time.sleep() - 시간 대기
# random() - 랜덤값