# Package...

## Mucking around with pyinstaller. 

This test tries to achieve 2 things:

1. create an 'app launcher' with tkinter, which can open the browser or restart a self contained server.

	- solves the issue of a users not knowing localhost:5000 and saving to having to provide a server

2. Use Github actions to run pyinstaller and build app/exe files for linux/mac/windows. which then uploads them to the release page

	- solves the issue of making bundles per platform. i.e. linux/mac/windows (as you can't make an exe from a mac for example)


It seeks to solve these things by using pyinstaller to bundle the python interpretter and a sanic server.


# how it works

\_app.py is the tkinter wrapper it loads the app.py file and runs it.

currently it expects the app.py to have this in the app.py to run it. but that may change.

```
	class Run():
	    def run(self):
	    	# put your initilising code here
	        app.run(host='127.0.0.1', port=8000, debug=False) # warning debug True will create 2 tkinter windows

	app_proxy = Run()
```

so if you replace the bottom of you file to init from that instead of a main it should run.


# building

All the commands to build it are in the Makefile. i.e.

```
make mac

make win

make linux
```

the .spec files have been modified to include from venv. They are absolute so will need changing for the machine they run on.

(they are currenty modded/hardcoced to be the basepaths of the github actions machines)


# Pipeline

Uses github actions to publish the apps. It can be run manually from the actions page.

At the moment there's a bug and you have to delete the release manually to create a new one.

Running it will create the apps and push them into the release page and downloadables.

if you click on the releases page there will be an _app.zip file for each platform (at mo only mac. as i got the dir wrong)

So that means in theory all you have to do to generate an app. Is clone this repo. Swap the app.py for your own. 

then replace the bottom of the new app.py file to init via the expected proxy method shown above rather than via a __main__

map in any assets to the respective .spec files. and anything new to the requirements.txt

then tag it or run from the actions page and it will build all the app versions.


# Summary

what we have so far

- a working publish to mac app with pyinstaller, using tkinter as 'app launcher' and bundling a server and python interpretter

- a working exe pipeline - ish. it creates a folder with everything in seems to run the exe the same as would a mac. but the mac seems to be better at hiding all the included files.

- both will seem to need another kind of 'app installer' step.

- is now pushing built zips to the release page. you can download and run them and they work. however they don't have 'app installers'


## NOTES BELOW ARE ABOUT BUILDING LOCALLY. YOU CAN IGNORE IF YOU WANT TO RELY ON THE GITHUB ACTIONS (which is the overall point of this repo)

# notes

- boot time seems slow. (several secs+) (would it be faster w/o interpretter?)

- remember asset base paths need changing when building vs when running locally.
```
	assets = os.path.join(sys._MEIPASS, 'assets')
	#assets = 'assets'
```

- debug mode in servers will create 2 tkinter windows as it reloads the \_app.py



# notes - linux

```
cd /Desktop/projects/package

python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt

```

on linux the binaries for tkinter are not included in the python library like they are with mac and windows.

So as well as the libs in the requirements, you have to also manually install it's required binaries with apt-get rather than pip.

sudo apt-get install python3-tk

after which the compiled programme will work the same way as it did on mac and windows.

(TODO - can that step be part of the app installer?)

# notes - mac

not having a console when launching on mac. see last few responses here: https://github.com/pyinstaller/pyinstaller/issues/3275

- At the moment I'm flicking between machines. while in flux this version was last building locally on commit 7.


# notes - windows

- you CAN'T create a windows .exe from a mac

- At the moment I'm flicking between machines. while in flux this version was last building locally on commit 8

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

WARNING. i was getting lots of windows spawning until I added this.

multiprocessing.freeze_support()


# Issues / Bugs

I've noticed using multiprocessing can spawn lots of tkinter windows if it throws errors. so be careful. This should have been resolved. Ideally I'd use the bundled interpretter to call the neighbouring file so will keep investigating.



# TODO
- See if can setup github actions to do the builds for all 3 platforms so you don't have to switch machines.
- A 'downloads' page for the various versions
- a script to zip the binaries and a read me etc.
- makefile script to autoupdate app name etc
- App icon and app name should be changeable in the .spec files. at mo it still calls them _app
- TODO - try to get the BASEPATHS for the spec files and build time.
