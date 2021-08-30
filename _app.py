import sys
import os
import time
import multiprocessing
from signal import SIGTERM

from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk

import webbrowser

from app import app_proxy as app

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)

    return os.path.join(os.path.abspath("."), relative_path)

#assets = os.path.join(sys._MEIPASS, 'assets')
#assets = 'assets'
#assets = os.path.abspath('.')

# sys.path.insert(0, sys._MEIPASS)  # will this add libs full depth?
assets = resource_path('assets')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8000/')


def restart_server():
    # restarts the app
    pass


def connect_to_server(address):
    # connect to someone elses server
    pass


class GUI:
    """

    This application is just a tkinter launcher.

    It's aim will be to show the status of conneted server or servers.

    and have buttons to restart the server or open the browser.

    """

    def __init__(self, root):
        self.root = root
        self.currFile = ''
        self.root.wm_title('Game Server')
        self.visible = False
        self.autoshow = False

        # creating a menu instance
        menu = Menu(self.root)
        self.root.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Open", command=open_browser)
        file.add_command(label="Close", command=self.close)
        menu.add_cascade(label="File", menu=file)

        game = Menu(menu)
        game.add_command(label="Open Browser", command=open_browser)
        game.add_command(label="restart server", command=restart_server)
        game.add_command(label="Restart Server", command=self.toggle_visible)
        # edit.add_command(label="Auto Show", command=self.toggle_autoshow)
        menu.add_cascade(label="Game", menu=game)

        self.f = Frame(self.root, height=30)
        self.f.pack(fill=BOTH, expand=True)
        
        self.newOpen = ttk.Button(self.f, text='Open', command=open_browser)
        self.newOpen.pack()
        # self.newOpen.pack(side=RIGHT)

        self.vis = StringVar()
        self.vis.set( "Always Visible:" + str(self.visible))
        b1 = ttk.Button(self.f, textvariable=self.vis, command=self.toggle_visible)
        b1.pack(side='top', anchor=N)
        # b1.grid(row=0, column=0)
        
        self.shw = StringVar()
        self.shw.set( "Auto Show:" + str(self.autoshow))
        b2 = ttk.Button(self.f, textvariable=self.shw, command=self.toggle_autoshow)
        b2.pack(side='top', anchor=N)
        # b2.grid(row=0, column=0)

        self.f2 = Frame(self.root, height=30)
        self.f2.pack(fill=BOTH, expand=True)

        # self.showbut = ttk.Button(self.f2, text='Show', command=self.show_text)
        # self.showbut.pack()
        # self.showbut.pack_forget()

        self.img = PhotoImage(file=f'{assets}/blurry.gif')
        self.imgl = ttk.Label(self.f2, image=self.img)#.pack()
        self.imgl.pack(fill=BOTH, expand=True)
        # self.f2.pack_forget() # hides the image


    def toggle_visible(self):
        self.visible = not self.visible
        self.vis.set( "Always Visible:" + str(self.visible))


    def toggle_autoshow(self):
        self.autoshow = not self.autoshow
        self.shw.set( "Auto Show:" + str(self.autoshow))


    def close(self, ):
        self.root.destroy()


def has_focus(window):
    # returns None if the window does not have focus
    return window.focus_displayof()


root=Tk()
root.geometry("300x400")
gui=GUI(root)


global __once # TODO - don't need now. was 
__once = False
def __main_app_launcher():
    global __once
    if __once:
        return
    __once = True
    root.mainloop()



class AppProxy:

    def __init__(self):
        self._loop = None
        self._process = None

    def run(self):
        # print('proxy run')
        # mp = multiprocessing.get_context("fork")
        from multiprocessing import Process
        # multiprocessing.set_start_method("spawn", force=True)
        self._process = Process(target=self._run)
        self._process.daemon = True
        self._process.start()

    def _run(self):
        # print("Starting main app")
        app.run()

    def stop(self):
        # os.kill(self._process.pid, SIGTERM)
        # print("Stopping main app")
       #  self._process.join()
       #  self._process.terminate()
       pass


if __name__ == '__main__':
    multiprocessing.freeze_support()
    a = AppProxy()
    a.run()
    #exec(open('app.py').read())
    __main_app_launcher()
    while True:
        test=1
   # a.stop()
