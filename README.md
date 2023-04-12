# Recipe app web
A simple web application for cooking recipes
# To run
Before anything you must to install all the libs.
```
pip install -r requirements.txt
```
After that, you must define a few env variables.
```
export SECRET_KEY='Your secret key'
export DATABASE_URI="postgresql://username:password@host:port/database_name"
export FLASK_APP=app
```
If you want to run the project in debug mode and development mode, you must to create these env variables.
```
export FLASK_DEBUG=true
export FLASK_ENV=development
```
Finally run the app.
```
flask run
```
# MuckUps
https://app.moqups.com/h3IlkiaF2mpUWPfcLvkJuiiinSAJSUTE/view/page/a013e980c
