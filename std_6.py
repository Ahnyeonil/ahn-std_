# 상속 - 기존의 클래스를 그대로 사용하기 위해서
class FourCal:
    def __init__(self, first, second):      # 생성자
        self.first = first
        self.second = second
    def setdata(self, first, second):       # self 는 함수 호출할때의 a
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(5, 7)
print(a.add())

# 부모 함수를 덮는것 = 오버라이딩

#객체변수
class FourCal2:
    first = 2
    second = 3
    def setdata(self, first, second):       # self 는 함수 호출할때의 a
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

aa = FourCal2()
print(aa.first)
print(aa.second)

class Family:
    lastname = "Ahn"

Family.lastname = "Park"        # 클래스 밖에서 바꿀 수 있음
print(Family.lastname)
ln = Family()
print(ln.lastname)

# 모듈 - 미리 만들어 놓은 .py 파일 (함수, 변수, 클래스) - 사용