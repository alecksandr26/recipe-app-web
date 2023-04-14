# Recipe app web
A simple web application of cooking recipes
# To run
Before anything you must to install all the libs in a new [env](https://docs.python.org/3/library/venv.html) of python.
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
Before running everything try to migrate and upgrade the schema of the database, `flask-migrate` uses Alembic.
```
flask db init
flask db migrate
flask db upgrade
```
After that now you must create the models in your database.
```
flask models create
```
Finally run the app.
```
flask run
```
# MuckUps
These are the mockups of the app.

https://app.moqups.com/h3IlkiaF2mpUWPfcLvkJuiiinSAJSUTE/view/page/a013e980c
# Todo
1. Create the tests for the login and signup pages
2. Finshing with the models
3. Try to upload the whole backup of the database
4. Create the navbar of the home
5. Start with css styling
