from GUI_Source import *
from BrowserMem_GUI import *
import ctypes

def main():
    app = QApplication([])
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(TXT_TITLE)

    app_icon = QtGui.QIcon()
    app_icon.addFile(APP_ICON)
    app.setWindowIcon(app_icon)

    window = BrowserMem_Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
