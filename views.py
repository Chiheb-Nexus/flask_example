#
# Main app
#

from flask import jsonify
from flask.views import MethodView
import models
from main import app


@app.route('/', methods=['GET'])
def index():
    """Index"""
    return '<center><b>Hello {user}!</b></center>'.format(
        user=models.User.query.first().username
    )


class IndexView(MethodView):
    """Class based views in Flask"""

    def get(self):
        """GET method"""
        return jsonify({
            'user': models.User.query.first().username.upper(),
            'password': None
        })


app.add_url_rule('/index/', view_func=IndexView.as_view('index2'))
