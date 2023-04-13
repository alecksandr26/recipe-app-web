# To connect to the postgres db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# For the database
db = SQLAlchemy()

# For migrates
migrate = Migrate()
