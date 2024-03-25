###필요한 모듈 불러오기
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    ###창 구성요소
    def initUI(self): #self는 MyApp객체
        self.setWindowTitle('My First Application') #창 제목 설정
        self.move(300, 300) #위젯의 위치
        self.resize(400, 200) #위젯의 크기
        self.show() #위젯을 화면에 띄어줌

if __name__ == '__main__': #__name__은 현재 모듈의 이름이 저장되는 내장 변수
   app = QApplication(sys.argv) #어플리케이션의 객체 생성 
   ex = MyApp()
   sys.exit(app.exec_())
'''만약 'moduleA.py'라는 코드를 import해서 예제 코드를 수행하면 
__name__ 은 'moduleA'가 됩니다. 그렇지 않고 코드를 직접 실행한다면 
__name__ 은 __main__ 이 됩니다. 
따라서 이 한 줄의 코드를 통해 프로그램이 직접 실행되는지 혹은 모듈을 통해 실행되는지를 확인합니다.'''