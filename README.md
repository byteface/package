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

- At the moment I'm flicking between machines. while in flux this version was last building on commit 7.


# notes - windows

- you CAN'T create a windows .exe from a mac

TODO - do a windows build

I'm not a windows native so will try and spell this out. mainly for myself.

using cmd prompt. remember its dir(not ls) and cd.

```
cd \Users\bytef\Desktop\projects\package

python3 -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

```

now 'make' wont run without stuff installed. remember it's bimbows. (you can just run the pyinstaller command manually that is in that makefile)

https://chocolatey.org/install

in the start menu type powershell. right click on it and choose 'run as admin'

then to paste stuff from that link into powershell. you have to click on the little icon top left and go edit>paste

```
choco install make

cd \Users\bytef\Desktop\projects\package

venv\Scripts\Activate.ps1
```

you should now be able to run make win in powershell (not working exe yet. DONT RUN IT!!!)

however that won't be any good for a github action. so will need to change that to something else.

delete the /build and /dist folders manually before each build on windows.

It doesn't bundle the files the same way it does on mac with same settings. so still need to change some paths etc in the .spec file. The exe I'm expecting to be much larger. unless you create an .exe package/intaller for windows as another step that wraps this exe and all the needed files?.

the exe currently spawns lots of windows so don't run it. sortin a mulitprocessing issue. I can get it to work on windows. tkinter and sanic and the game all as they were on the mac just on the cmd without an exe. so now just need to resovle the multi windows popping up when it's made into an exe. I don't seem to get a good console log of what's go on there. I thought it was related to incorrect asset paths or something hasn't copied over?.


*edit?... after writing all that. it just seems to be working fine. the exe is making. without spawning lots of windows. 

it could have been me tinkering before falling asleep or due to this addition

multiprocessing.freeze_support()

anyways. so now i need to push this. and pull on the mac and see if it works on both without having to change it.


# Summary

what we have so far

- a working publish to mac app with pyinstaller, using tkinter as 'app launcher' and bundling a server and python interpretter

- a working exe pipeline - ish. it creates a folder with everything in seems to run the exe the same as would a mac. but the mac seems to be better at hiding all the included files.

- both will seem to need another kind of 'app installer' step.


# TODO
- See if can setup github actions to do the builds for all 3 platforms so you don't have to switch machines.
- A 'downloads' page for the various versions
- a script to zip the binaries and a read me etc.
- makefile script to autoupdate app name etc
- App icon and app name should be changeable in the .spec files. at mo it still calls them _app