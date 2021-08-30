clean:
	rm -r dist/
	rm -r build/
	rm -r __pycache__/

#cleanwin:
#	rmdir dist/
#	rmdir build/
#	rmdir __pycache__/


mac:
	pyinstaller --noconsole --onefile --add-data 'assets:assets' --windowed mac.spec
# 	pyinstaller --onefile --add-data 'assets:assets' --paths=/Users/byteface/Desktop/apptest/venv/lib/python3.9/site-packages/websockets --windowed app.spec
#	pyinstaller --onefile --add-data 'assets:assets' --windowed _app.spec

win:
	pyinstaller --onefile --windowed win.spec

lin:
	pyinstaller --onefile --add-data 'assets:assets' --windowed linux.spec

deploy:
	echo 'where to?'
