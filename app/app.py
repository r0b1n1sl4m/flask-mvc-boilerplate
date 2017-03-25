from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from inc.db import db
# Import routes
from routes.home_routes import HomeRoutes

app = Flask(__name__)
app.config.from_object('settings.Config')

# initialization
db.init_app(app)

# migration
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# adding routes
app.add_url_rule('/', view_func=HomeRoutes.as_view('home'), methods=['GET',])

#run
if __name__ == '__main__':
	app.run(host='localhost')
	# manager.run()