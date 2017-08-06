from flask.views import MethodView
from flask import render_template

from app import app


class DaidiView(MethodView):

    def get(self):
        return "Hello"

app.add_url_rule('/', view_func=DaidiView.as_view('daidi'))
