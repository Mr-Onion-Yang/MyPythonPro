# -*- coding: utf-8 -*-
"""
-------------------------------------------------
 1、QApplication
QApplication类管理GUI程序的控制流和主要设置，是基于QWidget的，为此特化了QGuiApplication的一些功能，处理QWidget特有的初始化和结束收尾工作。
对于使用了Qt的任何GUI程序来说，不管何时何地有多少个Window，但只有一个QApplication对象，如果不是基于QWidget的程序，相应的则使用QGuiApplication，后者不依赖于Widget特有的库。
有些程序是不使用GUI的，通过命令行参数执行不同的任务而不用手动设置，这时使用QCoreApplication就够了，避免初始化不必要的GUI资源。

上面提到了只能有一个QApplication实例，其实就是Singleton模式，对象指针通过instance()静态函数获取，或者使用等效的qApp宏。QApplication的主要职责如下：
1、使用用户的桌面设置进行初始化，这些设置如palette()、font()、doubleClickInterval()，然后跟踪这些属性的变化，如用户通过某种配置面板修改了全局桌面设置。
2、处理事件，从窗口系统接收事件并派发到相应的Widget，使用sendEvent()和postEvent()函数可以派发事件。
3、处理命令行参数，设置内部状态。
4、定义GUI外观，外观由QStyle对象包装，运行时通过setStyle()函数进行设置。
5、设置颜色分配规则，对应的函数为setColorSpec()。
6、本地化字符串，函数为translate()。
7、提供了一些有用的对象，如desktop()、clipboard()函数。
8、知道Widget及Window，相应的函数为widgetAt()、topLevelWidgets()、closeAllWindows()。
9、管理鼠标光标，函数为setOverrideCursor()。
从上面可以看出，QApplication作了许多初始化工作，因此在任何其它的UI对象创建之前必须先创建QApplication对象，而且还可以通过命令行参数设置一些内部状态。

2、QGuiApplication
QApplication继承自QGuiApplication，后者是基于非QWidget的，提供了会话管理，用户退出时可以友好地终止程序，如果终止不了还可以取消对应的进程，甚至是保存程序的所有状态用于将来的会话，相关函数为isSessionRestored()、sessionId()、commitDataRequest()、saveDataRequest()。

3、QCoreApplication
QGuiApplication继承自QCoreApplication，后者不包括UI，一大核心功能是提供了event loop，这些event可以来自操作系统，如timer、网络事件，以及其它来源的event都可以被收发。调用exec()函数进入event loop，直到quit()函数调用时才退出，退出时发送aboutToQuit()信号，等同于exit(0)函数，sendEvent()函数立即处理事件，postEvent()函数把事件放入消息队列以等待后续处理，处于消息队列的的event还可以通过removePostedEvent()和sendPostedEvent()进行删除和立即处理。
与程序路径相关的有两个函数applicationDirPath()和applicationFilePath()，另外一个是库相关的，函数为libraryPaths()、setLibraryPaths()、addLibraryPath()、removeLibraryPath()，以及QLibrary类。
国际化、翻译相关的函数为translate()，以及installTranslator()和removeTranslator()。
获取命令行参数使用函数arguments()，专门处理命令行参数的类为QCommandLineParser。
为了保证兼容性，还要适当的设置语系setLocale()。
-------------------------------------------------
"""

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("社会我顺哥,人狠话不多")
window.resize(500, 500)
window.move(400, 200)

label = QLabel(window)
label.setText("Hello Sz")
label.move(200, 200)

window.show()

sys.exit(app.exec_())





