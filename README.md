
Packaging...


requirement

A solution that can bundle tkinter, a server and some assets.

Has some options and a floating panel to launch a browser window or can install launch another app/exe.


scripts may be required to add app icons

make file all the steps




# looks like assets will need to use a method to get a relative base path

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    (return os.path.join(base_path, relative_path)



as well as a command to copy assets to the install

  https://github.com/ciscomonkey/flask-pyinstaller




Also you CANT create a windows exe from mac. so will have to see if same command runs on windows to build .exe



A 'downloads' page for the various versions

a script to zip the binaries and a read me etc.



*note. i still didn't see where it put the copied files/folders - so not simple to edit after building.



can you make it a git repo with actions that does the buiding for you?


notes on app bundles
https://github.com/pyinstaller/pyinstaller/issues/3275