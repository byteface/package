# Bundle...


## Mucking around with pyinstaller. 


This test tries to create an 'app launcher' with tkinter, which can open the browser or restart a self contained server.

Uses pyinstaller to bundle the python interpretter and a sanic server.


# how it works

\_app.py is the tkinter wrapper it loads the app.py file and runs it.

currently it expects the app.py to have this in the app.py to run it. but that may change.

```
	class Run():
	    def run(self):
	        app.run(host='127.0.0.1', port=8000, debug=False) # warning debug True will create 2 tkinter windows

	app_proxy = Run()
```


# building

All the commands to build it are in the Makefile. i.e.

```
make mac
```

the .spec files have been modified to include from venv. They are aboslute so will need changing for your machine.



# notes

- boot time seems slow (several secs) (would it be faster w/o interpretter?)

- remember asset base paths need changing when building vs when running locally
```
	assets = os.path.join(sys._MEIPASS, 'assets')
	#assets = 'assets'
```

- debug mode in servers will create 2 tkinter windows as it reloads the \_app.py



# notes - mac

not having a console when launching on mac. see last few responses here: https://github.com/pyinstaller/pyinstaller/issues/3275



# notes - windows

- you CAN'T create a windows .exe from a mac

TODO - do a windows build



# TODO
- See if can setup github actions to do the builds for all 3 platforms so you don't have to switch machines.
- A 'downloads' page for the various versions
- a script to zip the binaries and a read me etc.
- makefile script to autoupdate app name etc