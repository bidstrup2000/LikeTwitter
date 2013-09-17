﻿## This is a test tasks (Not for usage)

### Getting Started
Test consist 9 different tasks which covers all Django development routine.

### Installation

1. You have to clone test app:

	git clone https://github.com/bidstrup2000/LikeTwitter.git

2. Create environment and activate it:

    cd LikeTwitter
    virtualenv .env
    source .env/Scripts/activate

3. Install other packages

	pip install -r requirements.txt
	
4. Install Python Image Library

	http://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe

5. Migrate to Django database

	python manage.py syncdb --noinput
    python manage.py migrate LikeTwitter
	
6. Run web development server

	python manage.py runserver


### Run automated tests

Run command: manage.py test notes

### Run manual tests

Run command: "manage.py runserver 127.0.0.1:8000" (local development server will run at port:8000).
Type "127.0.0.1:8000" at address bar of your browser. (You can type "127.0.0.1:8000/notes" too.)
Main page of application will appear.
To find note - type "127.0.0.1:8000/notes/[id_of_note]"
To run admin interfase - type "127.0.0.1:8000/admin"
If you want to add book, you can do this via admin interface ("127.0.0.1:8000/admin")
