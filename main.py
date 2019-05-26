#
# Main APP
#

from flask import Flask
from config import DevConf


app = Flask(__name__)
app.config.from_object(DevConf)

PORT = 8000
HOST = '127.0.0.1'


if __name__ == '__main__':
    # Making Flask act like an MVC framework
    from views import *  # noqa: F401,F403
    app.run(
        host=HOST,
        port=PORT
    )
