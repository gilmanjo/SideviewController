import constants
from package.mainwindow import MainWindow
from PyQt4 import QtGui
import sys


def main():
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(
        QtGui.QIcon(constants.DIR_ICON + constants.ICON_LOGO_SMALL)
    )
    main_win = MainWindow()
    sys.exit(app.exec_())


# idiomatic wrapper
def run():
    main()


if __name__ == '__main__':
    main()
