import sys
from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

from models import Test, ColumnProperty
from views import TestView, ColumnPropertiesView

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'mysql://testuser:avbtsUF3-6_8_Fgzo_W-@localhost/foobar'

db = SQLAlchemy(app)
admin = Admin(app, name='fooadmin')

admin.add_view(TestView(Test, db.session))
admin.add_view(ColumnPropertiesView(ColumnProperty, db.session))


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except (IndexError, ValueError):
        port = 5000

    app.run(port=port, debug=True)
