import std_6    # 가져옴
# 전체가 실행됨
# if __name__ == "__main__": 기존 함수에 포함시켜야됨
# 현재 실행하는 파일이 메인이어야만 실행되는 부분
# 다른 경로에 있는거 가져올 시
# import sys
# sys.path.append("경로")

# 패키지 = 라이브러리랑 비슷 - 모듈을 여러개 모아둔것
#__init__.py --> 패키지 구성시 설정파일 3.3버전 이후에는 사용안해도됨
# from 패키지 - 파일 import 함수명 as 사용가능
# 예 : from game import league of legend as lol
#__all__ == import * 를 하기위해서 init 파일에 __all__에 설정을 해줘야됨