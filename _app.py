from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import sys
import os


# import os
import random
from json import load
from dataclasses import dataclass, asdict, field
from sanic import Sanic
from sanic import response
from sanic_session import Session, InMemorySessionInterface

from domonic.html import *
from domonic.CDN import *
from domonic.javascript import setTimeout, clearTimeout
from domonic.javascript import setInterval, clearInterval

# global MAINLOOP_INT_ID
# MAINLOOP_INT_ID = None
# import threading

# import multiprocessing
# from multiprocessing.pool import ThreadPool as Pool



assets = os.path.join(sys._MEIPASS, 'assets')
# assets = 'assets'
sys.path.insert(0, sys._MEIPASS)  # will this add libs full depth?


def open_browser():
    webbrowser.open_new('http://127.0.0.1:8000/')


def restart_server():
    # restarts the app
    pass


def connect_to_server(address):
    # p2p connect to someone elses server
    pass



class GUI:
    """

    This application opens a single file in Read Only. (but you can still hi-lite)

    If you navigate away from the file the screen will blur so the text cannot be seen.

    Auto Show : When selecting the app it can show the content immediately or wait for you to press the show button.
    Always Visible : Doesn't go into hide mode

    """

    def __init__(self, root):
        self.root = root
        self.currFile = ''
        self.root.wm_title('No file currently open')
        self.visible = False
        self.autoshow = False
        self.counter = 10

        # creating a menu instance
        menu = Menu(self.root)
        self.root.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Open", command=self.openFile)
        file.add_command(label="Close", command=self.close)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Always Visible", command=self.toggle_visible)
        edit.add_command(label="Auto Show", command=self.toggle_autoshow)
        menu.add_cascade(label="Options", menu=edit)

        game = Menu(menu)
        game.add_command(label="Open Browser", command=open_browser)
        game.add_command(label="restart server", command=restart_server)
        menu.add_cascade(label="Options", menu=game)

        view = Menu(menu)
        view.add_command(label="Show", command=self.show_text)
        view.add_command(label="Hide", command=self.hide_text)
        menu.add_cascade(label="Options", menu=view)

        self.f = Frame(self.root, height=30)
        self.f.pack(fill=BOTH, expand=True)
        
        self.newOpen = ttk.Button(self.f, text='Open', command=lambda: self.openFile())
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

        self.text = Text(self.f, height=20, width=50)
        # self.scroll = Scrollbar(self.root, command=self.text.yview)
        # self.text.configure(yscrollcommand=self.scroll.set)
        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        # self.text.pack(side=RIGHT, fill=Y)

        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'


        self.f2 = Frame(self.root, height=30)
        self.f2.pack(fill=BOTH, expand=True)

        self.showbut = ttk.Button(self.f2, text='Show', command=self.show_text)
        self.showbut.pack()
        # self.showbut.pack_forget()

        self.img = PhotoImage(file=f'{assets}/blurry.gif')
        self.imgl = ttk.Label(self.f2, image=self.img)#.pack()
        self.imgl.pack(fill=BOTH, expand=True)
        # self.imgl.pack_forget()

        self.f2.pack_forget()

        self.button_countdown()


    def toggle_visible(self):
        self.visible = not self.visible
        self.vis.set( "Always Visible:" + str(self.visible))


    def toggle_autoshow(self):
        self.autoshow = not self.autoshow
        self.shw.set( "Auto Show:" + str(self.autoshow))


    def openFile(self):
        inp = self.text.get(1.0, END)
        self.file_opt['title']='Open'
        self.currFile = fd.askopenfilename(**self.file_opt)
        if self.currFile:
            # self.text.config(state=NORMAL)
            f = open(self.currFile,'r')
            # self.text.delete(0.0)
            inp = self.text.insert(1.0, f.read())
            self.root.wm_title(self.currFile)
            # self.text.config(state=DISABLED)

            self.newOpen.pack_forget()
            f.close()


    def button_countdown(self):
        # checks every second to update the counter and hide the page
        print(self.counter)
        if self.counter > 0:
            if self.autoshow:
                self.show_text()
            self.counter -= 1
            msg = f"This content will hide in {str(self.counter)} seconds"
            self.root.wm_title(msg)
        else:
            # self.close()
            self.hide_text()

        self.root.after(1000, lambda: self.button_countdown())


    def close(self, ):
        self.root.destroy()


    def show_text(self):
        self.f.pack(fill=BOTH, expand=True)
        # self.scrollable_body.pack()
        # if self.imgl
        # self.imgl.pack_forget()
        self.f2.pack_forget()
        

    def hide_text(self):
        if self.visible:
            return
        self.f.pack_forget()
        # self.scrollable_body.pack_forget()
        self.f2.pack(fill=BOTH, expand=True)
        # self.showbut.pack()


def has_focus(window):
    return window.focus_displayof()    # returns None if the window does not have focus

def check():
    if not has_focus(root):
        print('its not in fucking focus')
    else:
        print('Its in fucking focus')
        if gui.autoshow:
            gui.show_text()
        gui.counter = 3
    root.after(100, lambda: check())


root=Tk()
root.geometry("400x500")

gui=GUI(root)

def main():
    root.after(1000, lambda: check())
    root.mainloop()


import multiprocessing
import os
import time
from signal import SIGTERM
from app import app_proxy as app


class AppProxy:

    def __init__(self):
        self._loop = None
        self._process = None

    def run(self):
        mp = multiprocessing.get_context("fork")
        self._process = mp.Process(target=self._run)
        self._process.daemon = True
        self._process.start()

    def _run(self):
        print("Running other app")
        app.run()

    def stop(self):
        os.kill(self._process.pid, SIGTERM)
        print("Stopping other app")
        self._process.join()
        self._process.terminate()


if __name__ == '__main__':
    a = AppProxy()
    a.run()
    main()
    a.stop()