from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import sys
import os


import os
import random
from json import load
from dataclasses import dataclass, asdict, field
from sanic import Sanic
from sanic import response
# from sanic_session import Session, InMemorySessionInterface

from domonic.html import *
from domonic.CDN import *

# assets = os.path.join(sys._MEIPASS, 'assets')
assets = 'assets'
# sys.path.insert(0, sys._MEIPASS)  # will this add libs full depth?


app = Sanic(name='Test packaging sanic')
app.static('/assets', './assets')

@app.route('/')
async def play(request):
    return response.html(str("HI"))


# if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8000, debug=True)
