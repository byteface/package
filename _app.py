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
from sanic_session import Session, InMemorySessionInterface

from domonic.html import *
from domonic.CDN import *
from domonic.javascript import setTimeout, clearTimeout
from domonic.javascript import setInterval, clearInterval

global MAINLOOP_INT_ID
MAINLOOP_INT_ID = None
import threading



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
root.geometry("500x800")

gui=GUI(root)

def main():
    if MAINLOOP_INT_ID is not None:
        clearInterval( MAINLOOP_INT_ID )
    root.after(1000, lambda: check())
    root.mainloop()


# if __name__=='__main__':
#     sys.exit(main())



# import sys
# sys.path.insert(0, '../..')

# import os
# import random
# from json import load
# from dataclasses import dataclass, asdict, field
# from sanic import Sanic
# from sanic import response
# from sanic_session import Session, InMemorySessionInterface

# from domonic.html import *
# from domonic.CDN import *

#  TO run this :
#  pip3 install sanic
#  pip3 install sanic-session

app = Sanic(name='Hangman')
app.static('/assets', './assets')

session = Session(app, interface=InMemorySessionInterface())

# create a template
page_wrapper = lambda content : html(
            head(
                script(_src="https://code.jquery.com/jquery-3.5.1.min.js"),
                link(_rel="stylesheet", _type="text/css", _href=CDN_CSS.MVP),
                script(_type="text/javascript").html(
                """
                document.addEventListener('keydown', send_keypress);
                function send_keypress(event) {
                    $.get('/move?letter='+event.key, function(response){
                        $("#game").html(response);
                    });
                };
                """
                )
            ),
            body(
                str(content)
            ))


def get_word():
    wordArray = 'Adult Aeroplane Air Aircraft Carrier Airforce Airport Album Alphabet Apple Arm Army Baby Baby Backpack Balloon Banana Bank Barbecue Bathroom Bathtub Bed Bed Bee Bible Bible Bird Bomb Book Boss Bottle Bowl Box Boy Brain Bridge Butterfly Button Cappuccino Car Carpet Carrot Cave Chair Chess Board Chief Child Chisel Chocolates Church Church Circle Circus Circus Clock Clown Coffee Comet Compact Disc Compass Computer Crystal Cup Cycle Data Base Desk Diamond Dress Drill Drink Drum Dung Ears Earth Egg Electricity Elephant Eraser Explosive Eyes Family Fan Feather Festival Film Finger Fire Floodlight Flower Foot Fork Freeway Fruit Fungus Game Garden Gas Gate Gemstone Girl Gloves God Grapes Guitar Hammer Hat Hieroglyph Highway Horoscope Horse Hose Ice Insect Jet fighter Junk Kaleidoscope Kitchen Knife Leather jacket Leg Library Liquid Magnet Man Map Maze Meat Meteor Microscope Milk Milkshake Mist Money $$$$ Monster Mosquito Mouth Nail Navy Necklace Needle Onion PaintBrush Pants Parachute Passport Pebble Pendulum Pepper Perfume Pillow Plane Planet Pocket Potato Printer Prison Pyramid Radar Rainbow Record Restaurant Rifle Ring Robot Rock Rocket Roof Room Rope Saddle Salt Sandpaper Sandwich Satellite School Sex Ship Shoes Shop Shower Signature Skeleton Slave Snail Software Solid Space Shuttle Spectrum Sphere Spice Spiral Spoon Spot Light Square Staircase Star Stomach Sun Sunglasses Surveyor Swimming Pool Sword Table Tapestry Teeth Telescope Television Tennis racquet Thermometer Tiger Toilet Tongue Torch Torpedo Train Treadmill Triangle Tunnel Typewriter Umbrella Vacuum Vampire Videotape Vulture Water Weapon Web Wheelchair Window Woman Worm'.lower().split()
    word = random.choice(wordArray)
    return word


def display_hangman(tries):
    stages = [
    "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="
    ] 
    return stages[tries]


@dataclass
class GameData:
    word : str = None
    guessed : bool = False
    guessed_letters : list = field(default_factory=list)
    guessed_words : list  = field(default_factory=list)
    tries : int = 6


class Game(object):
    """ Hangman. The data is stored on a session """
    def __init__(self, request=None):
        self.state = GameData()
        if request is not None:
            if not request.ctx.session.get('game'):
                request.ctx.session['game'] = asdict(self.state)
            else:
                data = request.ctx.session.get('game')
                self.state.word = data['word']
                self.state.guessed = data['guessed']
                self.state.guessed_letters = data['guessed_letters']
                self.state.guessed_words = data['guessed_words']
                self.state.tries = data['tries']


@app.route('/move')
async def move(request):
    game = Game(request)  # recover the game from the session
    guess = request.args['letter'][0]
    word_completion = "_" * len(game.state.word)

    board = div()
    if not game.state.guessed and game.state.tries > 0:
        if guess in game.state.guessed_letters:
            board.appendChild( div("You already guessed the letter ", guess) )

        elif guess not in game.state.word:
            board.appendChild( div(b(guess), " is not in the word."))
            game.state.tries -= 1
            game.state.guessed_letters.append(guess)

        else:
            board.appendChild(div(f"You guessed the letter '{guess}' correctly!"))
            game.state.guessed_letters.append(guess)

            word_completion = list("_" * len(game.state.word))
            for i, w in enumerate(game.state.word):
                if w in game.state.guessed_letters:
                    word_completion[i] = w

            if "_" not in word_completion:
                game.state.guessed = True

    if game.state.guessed == True:
        board.appendChild(div("Nice one!, you guessed it. You win."))
    elif game.state.tries < 1:
        board.appendChild(div(f"Out of tries. The word was {game.state.word}. Maybe next time!"))

    page = div(
        div(f"Length of the word: {len(game.state.word)}"),
        div(f"Tries Left: {game.state.tries}"),
        pre(display_hangman(game.state.tries)),
    )

    word_completion = list("_" * len(game.state.word))
    for i, w in enumerate(game.state.word):
        if w in game.state.guessed_letters:
            word_completion[i] = w

    # TODO - div('To Play Again Type (Y/N)')
    page.appendChild(" ".join(word_completion))
    page.appendChild(board)
    request.ctx.session['game'] = asdict(game.state) # update the session
    return response.html(str(main( str(page), _id="game")))


@app.route('/')
@app.route('/play')
async def play(request):

    # create a new game based on this session
    request.ctx.session['game'] = None
    game = Game(request)
    game.state.word = get_word() # get a random word to start playing with
    request.ctx.session['game'] = asdict(game.state)

    intro = header(
        h1("HANGMAN!"),
        div("Can you guess the word? type a letter using the keyboard to guess."),
        main(_id="game")
    )
    return response.html(str(page_wrapper(intro)))


def serve():
    app.run(host='127.0.0.1', port=8000, debug=True)


if __name__ == '__main__':
    t1 = threading.Thread(target=serve).start()
    # setTimeout( serve, 10000 )  # tyr to run it on a thread
    # clearInterval( someid )  # only run it once
    main()
    # MAINLOOP_INT_ID = setInterval( main, 5000 )  # tyr to run it on a thread
    # clearInterval( MAINLOOP_INT_ID )  # only run it once
    # app.run(host='127.0.0.1', port=8000, debug=True)