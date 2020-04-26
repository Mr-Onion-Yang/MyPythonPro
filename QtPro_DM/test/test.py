
#导入控件包
from PyQt5.Qt import *

import sys

#1、创建一个应用程序对象

app = QApplication(sys.argv)

#2、控件的操作
window = QWidget()

window.setWindowTitle("小书精灵")

print(window.x())
print(window.y())
print(window.pos())
print(window.geometry())  #获取整个控件的坐标到内容的大小
print(window.rect())
print(window.frameSize())
print(window.frameGeometry())

window.setMinimumSize(400, 400)
window.move(500, 500)
window.adjustSize()



#展示空间
window.show()

#3、应用程序执行，进入到消息循环队列
sys.exit(app.exec_())