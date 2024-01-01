from GUI_Source import *
from Browser_SavePoint import *

class BrowserMem_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Initialize basic UI elements
        self.setWindowTitle(TXT_TITLE)
        self.setFixedSize(WIDTH, HEIGHT)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self.savepoint_list = QListWidget()
        starting_savepts = parse_json_savepoints(FILENAME_SAVEPT)
        for savept in starting_savepts:
            self.savepoint_list.addItem("{0} ({1} tabs)".format(savept[IND_ID], savept[IND_NTABS]))
        self.savepoint_list.setFixedSize(int(0.95*WIDTH), int(0.75*HEIGHT))
        self.generalLayout.addWidget(self.savepoint_list)


        self.restore_del_btns = QHBoxLayout()
        self.restoreBtn = QPushButton("Restore Currently Selected Savepoint")
        self.restoreBtn.clicked.connect(lambda: restore_savepoint(FILENAME_SAVEPT, self.savepoint_list.currentItem().text(), self, self.savepoint_list))
        self.restore_del_btns.addWidget(self.restoreBtn)

        self.delBtn = QPushButton("Delete Currently Selected Savepoint")
        self.delBtn.clicked.connect(lambda: delete_savepoint(FILENAME_SAVEPT, self.savepoint_list.currentItem(), self.savepoint_list, self))
        self.restore_del_btns.addWidget(self.delBtn)

        self.generalLayout.addLayout(self.restore_del_btns)

        self.inputForm = QHBoxLayout()
        
        self.inputForm.addWidget(create_label("Name For New Savepoint: ", LEFT, LBL_FONT, LBL_SIZE))
        self.idLineEdit = QLineEdit()
        self.inputForm.addWidget(self.idLineEdit)

        self.addSavepointBtn = QPushButton("Add New Savepoint")
        self.addSavepointBtn.clicked.connect(lambda: create_savePoint(self.idLineEdit.text(), self.savepoint_list, self))
        self.inputForm.addWidget(self.addSavepointBtn)

        self.generalLayout.addLayout(self.inputForm)

        # print(self.savepoint_list.currentItem())

        self.show()