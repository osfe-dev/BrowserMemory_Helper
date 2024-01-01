import webbrowser
from GUI_Source import *
import subprocess, os, sys, platform, errno, winreg, re
from time import sleep
import warnings
warnings.simplefilter("ignore", UserWarning)
sys.coinit_flags = 2
import pywinauto as winauto
import pyautogui as autogui
from tkinter import Tk
import shutil

global confirm
confirm = 0

# Dialog that displays a message telling the user to select a window
class WindowSelectionDialog(QDialog):
    def __init__(self, window_msg, confirm_btn_msg, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        # Create welcome message
        self.label = QLabel()
        self.label.setText(window_msg)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        # Create confirmation button
        startBtn = QPushButton(confirm_btn_msg)
        startBtn.clicked.connect(self.close)
        self.layout.addWidget(startBtn)

        self.setLayout(self.layout)
        self.setWindowTitle("Select Window!")

# Dialogue that asks for a confirmation
class ConfirmationDialog(QDialog):
    def __init__(self, confirm_msg, confirm_btn_text, refuse_btn_text, confirm, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()

        # Create welcome message
        self.label = QLabel()
        self.label.setText(confirm_msg)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.ret_btns = QHBoxLayout()

        # Create confirmation button
        confirm_btn = QPushButton(confirm_btn_text)
        confirm_btn.clicked.connect(self.confirm)
        self.ret_btns.addWidget(confirm_btn)

        # Create refusal button
        refuse_btn = QPushButton(refuse_btn_text)
        refuse_btn.clicked.connect(self.refuse)
        self.ret_btns.addWidget(refuse_btn)

        self.layout.addLayout(self.ret_btns)

        self.setLayout(self.layout)
        self.setWindowTitle("Confirmation")

    def confirm(self):
        global confirm
        confirm = 1
        self.close()

    def refuse(self):
        global confirm
        confirm = 0
        self.close()

# Creates a save point of the currently active chrome window
# Creates a corresponding file named after the given id
def create_savePoint(id, list, main_window):
    if(len(id) < 1):
        return FAILURE
    
    chars = set('?!@#$%^&*()}{[]/\\')
    if any((c in chars) for c in id):
        try_again_dlg = WindowSelectionDialog(BAD_FORMATTING, ACCEPT_BTN)
        try_again_dlg.exec()
        return FAILURE

    # generate list of URL strings of currently active chrome window
    win_sel_dlg = WindowSelectionDialog(WIN_SEL_CREAT, WIN_SEL_BTN, main_window)
    win_sel_dlg.exec()
    sleep(WIN_SEL_DELAY)
    win_sel_dlg.close()
    autogui.hotkey('ctrl', '1')     # Opens first tab

    baseURL = get_url()
    urls = []
    urls.append(baseURL)            # Get URL of first tab

    next_tab()
    newURL = get_url()
    while(newURL != baseURL):
        urls.append(newURL)
        next_tab()
        newURL = get_url()
    
    # Done grabbing URLs, write JSON to output and add as list item
    f = open(FILENAME_SAVEPT, 'a')
    f.write(generate_json(id, urls))
    f.close()
    # print(generate_json(id, urls))
    list.addItem("{0} ({1} tabs)".format(id, len(urls)))

def restore_savepoint(savepoints_file, list_text, main_window, qlist):
    # Check if anything is even selected
    if(qlist.currentItem() == None):
        return FAILURE    

    ind_nTabStart = list_text.find("(")
    id = list_text[:ind_nTabStart-1]
    nTabs = int(list_text[ind_nTabStart+1:-6])
    urls = get_urls_from_id(savepoints_file, id, nTabs)

    win_sel_dlg = WindowSelectionDialog(WIN_SEL_RESTORE, WIN_SEL_BTN, main_window)
    win_sel_dlg.exec()
    sleep(WIN_SEL_DELAY)
    win_sel_dlg.close()
    for i in range(len(urls)):
        webbrowser.open_new_tab(urls[i])

# Deletes a savepoint corresponding to given id
def delete_savepoint(savepoints_file, list_item, qlist, main_window):
    # Check if anything is seven selected
    if(qlist.currentItem() == None):
        return FAILURE

    list_text = list_item.text()
    ind_nTabStart = list_text.find("(")
    id = list_text[:ind_nTabStart-1]
    nTabs = int(list_text[ind_nTabStart+1:-6])

    # Confirm that user really wants to delete item
    confirm_dlg = ConfirmationDialog(CONFIRM_DEL.format(id), CONFIRM_BTN, REFUSE_BTN, main_window)
    print(confirm)
    confirm_dlg.exec()
    print(confirm)
    if(confirm == 0):
        return FAILURE

    json_endpts = find_json_endpoints(savepoints_file, id, nTabs)
    if(json_endpts[0] == -1 or json_endpts[1] == -1):
        return
    
    # Rewrite file, replacing lines
    f = open(savepoints_file, 'r')
    lines = f.readlines()
    f.close()

    f = open(savepoints_file, 'w')
    for i in range(len(lines)):
        if((i < json_endpts[0]) or (i > json_endpts[1])):
            f.write(lines[i])
    f.close()
    qlist.takeItem(qlist.currentRow())
    return

# Finds start and end line for json object
def find_json_endpoints(savepoints_file, id, nTabs):
    f = open(savepoints_file, 'r')
    lines = f.readlines()
    f.close()

    start = end = -1
    i = 0
    while(i < len(lines)):
        if(lines[i].lstrip() == "{\n"):
            if(lines[i+1].lstrip()[7:-3] == id):
                # Found it!
                start = i
                end = i+6+nTabs
                return (start, end)
            else:
                i += 1
        else:
            i += 1
    return (start, end)

# generates a json string with a given id & list of URLs
def generate_json(id, urls):
    return "{{\n\t\"id\": \"{0}\",\n\t\"len\": {1},\n\t\"urls\": \n{2},\n}},\n".format(id, len(urls), generate_array_json(urls, 2))

# creates list of tuples containing (id, nTabs) pair for each savepoint
def parse_json_savepoints(savepoints_file):
    f = open(savepoints_file, 'r')
    lines = f.readlines()
    f.close()

    savepts = []
    i = 0
    while(i < len(lines)):
        if(lines[i].lstrip() == "{\n"):
            # Start of new savepoint
            # Grab ID
            i += 1
            new_id = lines[i].lstrip()[7:-3]

            # Grab length
            i += 1
            nTabs = int(lines[i].lstrip()[7:-2])

            # Add tuple
            savepts.append((new_id, nTabs))

            # Skip to next line
            i += (5+nTabs)
        else:
            i += 1
    f.close()
    return savepts

# Parses json file looking for specific savept
# Returns array of urls
def get_urls_from_id(savepoints_file, id, nTabs):
    f = open(savepoints_file, 'r')
    lines = f.readlines()

    urls = []
    i = 0
    while(i < len(lines)):
        if(lines[i].lstrip() == "{\n"):
            if(lines[i+1].lstrip()[7:-3] == id):
                # Found it!
                i += 5      # Skip to start of urls
                for j in range(nTabs):
                    urls.append(lines[i+j].lstrip()[1:-3])
                return urls
            else:
                i += 1
        else:
            i += 1

# returns string with proper indentation for array
def generate_array_json(array, indentation):
    json_arr = ("\t" * indentation) + "[\n"
    for element in array:
        json_arr += ("\t" * (indentation+1)) + "\"" + element + "\",\n"
    json_arr += ("\t" * indentation) + "]"
    return json_arr


# parses json file and returns list of urls corresponding to given id
def get_urls(id):
    return

# move over to next tab in current browser window
def next_tab():
    autogui.hotkey('ctrl', 'tab')

# grabs url of current tabe
def get_url():
    autogui.hotkey('ctrl', 'r')
    autogui.hotkey('f6')            # Highlights url
    autogui.hotkey('ctrl', 'c')     # Copy url
    return Tk().clipboard_get()