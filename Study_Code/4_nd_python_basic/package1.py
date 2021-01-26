# <패키지>
# travel 패키지 안의 모듈들 가져옴

# import travel.Thailand # 모듈이나 패키지만 임포트 가능 / 함수나 클래스명은 안됨!
# trip_to = travel.Thailand.ThailandPackage()
# trip_to.detail()

from travel.Thailand import ThailandPackage
trip_tp = ThailandPackage()
trip_to.detail()

# from travel import Vietnam
# trip_to = Vietnam.VietnamPackage()
# trip_to.detail()

# < __all__ >
# from travel import * # 임포트 되길 원하는 것만 공개하고 아닌 것은 비공개로 처리 가능.
# trip_to = Thailand.ThailandPackage()
# trip_to.detail()  