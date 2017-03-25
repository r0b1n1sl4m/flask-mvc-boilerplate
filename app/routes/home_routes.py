from flask.views import MethodView
from flask import render_template
#import models
from models.home_model import HomeModel

class HomeRoutes(MethodView):
	def get(self):
		return render_template('home.html', credit='RobinIslam.me')