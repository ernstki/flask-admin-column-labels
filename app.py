import sys
from flask import Flask
from flask_admin import Admin, AdminIndexView


from models import Test, ColumnProperty
from views import TestView, ColumnPropertiesView
from extensions import db

app = Flask(__name__)
cfg = {}

# a very robust .ini parser ;) --see sample_config.ini
with open('config.ini') as f:
    for line in f.readlines():
        line = line.replace(' ', '').replace('\t', '').strip()
        if not line or line.startswith('#'): continue
        cfg.update([tuple(line.split('='))])

# app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = \
        "mysql://{user!s}:{password!s}@{host!s}/{database!s}".format(**cfg)

db.init_app(app)

admin = Admin(app, name="{}-admin".format(cfg['database']),
              index_view=AdminIndexView(name='Admin Home', url='/'),
              template_mode='bootstrap3')

admin.add_view(TestView(Test, db.session))
admin.add_view(ColumnPropertiesView(ColumnProperty, db.session))


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except (IndexError, ValueError):
        port = 5000

    app.run(port=port, debug=True)
