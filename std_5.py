#Immutable(변하지않는 - 정수, 실수, 문자열, 튜플), Mutable(변하는 - 리스트, 딕셔너리, 집합)

#클래스 - 중복되는 변수, 함수를 위해 선언
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

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
    def minus(self):
        result = self.first - self.second
        return result
a = FourCal(5, 7)
print(a.add())
print(a.minus())