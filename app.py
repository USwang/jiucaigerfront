
from flask import Flask, render_template, request
import config
from exts import db
from flask_migrate import Migrate
from models import Stockdata

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():  # put application's code here
    # lies = db.session.query(Stockdata).get(1)
    lies = db.session.query(Stockdata).filter_by(SECURITY_CODE='000001').first()
    codename = lies.SECURITY_NAME_ABBR
    context = {
        "codename": codename
    }
    return render_template('front/index.html', **context)


if __name__ == '__main__':
    app.run()
