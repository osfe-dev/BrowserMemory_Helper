# Definitions for various imports/constants

# Imports
from PyQt6.QtWidgets import (
    QApplication, 
    QLabel, 
    QMessageBox,
    QWidget,
    QMainWindow, 
    QGridLayout, 
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QComboBox,
    QFrame,
    QSizePolicy,
    QDialog,
    QDialogButtonBox,
    QSpacerItem,
    QRadioButton,
    QCheckBox,
    QStackedWidget,
    QListWidget,
)
from PyQt6 import (
    QtGui, 
    QtWidgets
)
from PyQt6.QtCore import (
    Qt,
    QUrl,
    QTimer,
    QSize,
)
from PyQt6.QtGui import (
    QPixmap,
    QPalette, 
    QFont,
    QPainter,
    QBrush,
    QPen,
    QFontMetrics,
    QPainterPath,
    QColor,
)
from PyQt6.QtMultimedia import (
    QSoundEffect,
    QMediaPlayer,
    QAudioOutput
)

import os, sys, time

# Some generally-applicable UI Functions
def create_label(text, alignment, font, size):
    label = QLabel()
    label.setText(text)
    label.setFont(QFont(font, size))
    label.setAlignment(alignment)
    return label


# Various Constant Definitions
# Dimensions
WIDTH       =   500
HEIGHT      =   600
LINE_WIDTH  =   1
IMG_WIDTH   =   int(0.4*WIDTH)
IMG_HEIGHT  =   int(0.25*HEIGHT)

# Font
TITLE_FONT  =   'Helvetica'
TITLE_SIZE  =   24
LBL_FONT    =   'Helvetica'
LBL_SIZE    =   12
FORM_FONT   =   'Helvetica'
FORM_SIZE   =   8
HEADING_SZ  =   16

# Alignment flags
LEFT    =   Qt.AlignmentFlag.AlignLeft
CENTER  =   Qt.AlignmentFlag.AlignCenter
RIGHT   =   Qt.AlignmentFlag.AlignRight

# Colors for various buttons/fields
LTBLUE  =   "#b8e0f5"
LTTAN   =   "#faf2cd"
LTGRAY  =   "#E6E6E6"
LTGRAY2 =   "#E0E0E0"
BEXP_G  =   "#02F902"
DARK_G  =   "02DB02"

# Colors to be passed to QtQui.Color(R,G,B)
COL_LTGRAY      =   (212,212,212)
COL_WHT         =   (0,0,0)
COL_BEXP_GREEN  =   (2,249,2)

# Specific colors for various types of elements
SEP_COL     =   COL_WHT

# Misc Constants
DELAY           =   500     # ms
ODDS_OF_FUN     =   25      # The odds of having fun
WIN_SEL_DELAY   =   5       # delay in seconds for user to select chrome window to create savepoint for
AUTOGUI_SLEEP   =   0.1     # seconds
AUTOGUI_MINISLP =   0.075
URL_ATTEMPTS    =   4       # Number of times program will attempt to copy URL

# Return values
SUCCESS     =   0
FAILURE     =   -1

# Indices for values in tuple
IND_ID      =   0
IND_NTABS   =   1

# Misc Messages/Titles
TXT_TITLE       =   "Chrome Browser Memory"
FILENAME_SAVEPT =   'savepoints.json'
APP_ICON        =   'AppIcon'

# Dialog Messages
WELCOME         =   """"""
WIN_SEL_CREAT   =   """You are about to create a new browser savepoint!
After closing this pop-up, you will have 5 seconds to select a browser window, 
after which the program will attempt to create a savepoint using the currently selected chrome window.
Please wait for the savepoint to appear in the list before clicking off of the chrome window."""
WIN_SEL_RESTORE =   """You are about to restore a browser savepoint!
After closing this pop-up, you will have 5 seconds to select a browser window,
after which the program will restore the savepoint in the currently selected chrome window.
If you have multiple chrome profiles and you're restoring a window that relies on being signed in to a 
specific account, make sure to select a chrome window that is signed in to that account."""
WIN_SEL_BTN     = "I'm ready to select a chrome window"
CONFIRM_DEL     = """Warning! You are about to permanently delete the savepoint \"{0}\".
Do you still want to delete it?"""
CONFIRM_BTN     = "Yes, delete this savepoint."
REFUSE_BTN      = "No, do not delete"
BAD_FORMATTING  = """Sorry, savepoint names cannot include any of the following characters:
? ! @ # $ % ^ & * ( ) [ ] { } / \\
Please try again"""
ACCEPT_BTN      = """Fine, I'll try again :("""

