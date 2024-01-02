@ECHO OFF

rem Cleanup Releases folder
del ./Releases/new_release.zip
del -r ./Releases/new_release

rem Build new EXE
pyinstaller --onefile --distpath ./ BrowserMemory_Helper.py 

rem Create new zip named new_release.zip in the Releases folder
Tar -a -cf ./Releases/new_release.zip BrowserMemory_Helper.exe savepoints.json AppIcon.ico

rem Cleanup working directory
del BrowserMemory_Helper.exe


PAUSE