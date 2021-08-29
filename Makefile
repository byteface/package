clean:
	rm -r dist/
	rm -r build/

mac:
	pyinstaller --onefile --add-data 'assets:assets' --windowed mac.spec
# 	pyinstaller --onefile --add-data 'assets:assets' --paths=/Users/byteface/Desktop/apptest/venv/lib/python3.9/site-packages/websockets --windowed app.spec

win:
	pyinstaller --onefile --add-data 'assets:assets' --windowed win.spec

lin:
	pyinstaller --onefile --add-data 'assets:assets' --windowed linux.spec


deploy:
	echo 'where to?'
