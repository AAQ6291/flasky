import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app, Todo=Todo)


if __name__ == '__main__':
    manager.run()
